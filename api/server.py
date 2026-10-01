"""API mínima del curso (solo biblioteca estándar).

POST /vote              {token, answers}  -> 201 | 409 si ese dispositivo ya votó
GET  /results           (X-Admin-Key) -> totales por pregunta y respuestas abiertas
GET  /plazo?tarea=s1    -> fecha límite de entrega (público)
POST /entrega           {tarea, email, nombre, grupo, texto, enlace, archivo:{nombre,tipo,b64}} -> 201 | 403 fuera de plazo
GET  /entregas?tarea=s1 (X-Admin-Key) -> todas las entregas (todas las versiones)
GET  /archivo?id=N      (X-Admin-Key) -> archivo adjunto
GET  /health
POST /mcp               servidor MCP (Streamable HTTP, sin estado) con herramientas de ventas de la empresa ficticia
"""
import base64, csv, hashlib, hmac, io, json, os, re, sqlite3, time, uuid, urllib.request
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

DB = os.environ.get("DB_PATH", "/data/votos.db")
ADMIN_KEY = os.environ["ADMIN_KEY"]
ALLOWED = set(os.environ.get("ALLOWED_ORIGINS", "https://unimauro.github.io").split(","))
SALT = os.environ.get("IP_SALT", "sal")
MAX_PER_IP = int(os.environ.get("MAX_PER_IP", "80"))
# Fechas límite en UTC. Por defecto: sesión 1 hasta el jueves 1 de octubre de 2026, 6:59 p. m. de Lima (23:59 UTC).
PLAZOS = json.loads(os.environ.get("PLAZOS", '{"s1": "2026-10-01T23:59:00Z"}'))
FILES = os.environ.get("FILES_DIR", "/data/archivos")
MAX_FILE = 10 * 1024 * 1024
EXT_OK = {"pdf", "xlsx", "xls", "csv", "docx", "doc", "pptx", "txt", "md", "png", "jpg", "jpeg", "zip"}
EMAIL = re.compile(r"^[^@\s]{1,64}@[^@\s]{1,190}\.[a-zA-Z]{2,}$")

def db():
    c = sqlite3.connect(DB)
    c.execute("CREATE TABLE IF NOT EXISTS votos (token TEXT PRIMARY KEY, ip TEXT, ts INTEGER, answers TEXT)")
    c.execute("""CREATE TABLE IF NOT EXISTS entregas (id INTEGER PRIMARY KEY AUTOINCREMENT, tarea TEXT, email TEXT, nombre TEXT,
                 grupo TEXT, texto TEXT, enlace TEXT, archivo_nombre TEXT, archivo_tipo TEXT, archivo_path TEXT, ts INTEGER, ip TEXT)""")
    return c

def plazo(tarea):
    p = PLAZOS.get(tarea)
    return datetime.strptime(p, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc).timestamp() if p else None


# ---------------- MCP: ventas de Distribuidora Andina (datos ficticios) ----------------
DATA_URL = "https://unimauro.github.io/curso-ia-productividad/material/"
_cache = {}

def _cargar(nombre):
    c = _cache.get(nombre)
    if c and time.time() - c[0] < 600:
        return c[1]
    raw = urllib.request.urlopen(DATA_URL + nombre, timeout=20).read().decode("utf-8")
    data = json.loads(raw) if nombre.endswith(".json") else list(csv.DictReader(io.StringIO(raw)))
    _cache[nombre] = (time.time(), data)
    return data

FILTROS = ["mes", "region", "canal", "vendedor", "proveedor", "categoria"]

def resumen_ventas(args):
    filas = [v for v in _cargar("ventas-2025.json") if all(not args.get(f) or str(v[f]).lower() == str(args[f]).lower() for f in FILTROS)]
    def agrupar(k):
        g = {}
        for v in filas:
            g[v[k]] = g.get(v[k], 0) + v["venta"]
        return sorted(({"nombre": n, "venta": round(x)} for n, x in g.items()), key=lambda r: -r["venta"])
    venta = sum(v["venta"] for v in filas); margen = sum(v["margen"] for v in filas)
    desc = {}
    for v in filas:
        d = desc.setdefault(v["vendedor"], [0, 0]); d[0] += v["descuento"]; d[1] += 1
    return {
        "empresa": "Distribuidora Andina S.A.C. (ficticia, datos 2025 inventados para práctica)",
        "filtros": {f: args[f] for f in FILTROS if args.get(f)},
        "pedidos": len({v["pedido"] for v in filas}), "venta": round(venta), "margen": round(margen),
        "margen_pct": round(margen / venta * 100, 1) if venta else 0,
        "vencido_por_cobrar": round(sum(v["venta"] for v in filas if v["estado_pago"] == "Vencido")),
        "por_mes": sorted(agrupar("mes"), key=lambda r: int(r["nombre"])), "por_region": agrupar("region"),
        "por_canal": agrupar("canal"), "por_vendedor": agrupar("vendedor"), "top_productos": agrupar("producto")[:5],
        "descuento_promedio_por_vendedor_pct": {k: round(x[0] / x[1] * 100, 1) for k, x in desc.items()},
    }

def entregas_proveedores(args):
    g = {}
    for c in _cargar("compras-proveedores-2025.csv"):
        if args.get("proveedor") and c["proveedor"].lower() != args["proveedor"].lower():
            continue
        d = g.setdefault(c["proveedor"], [0, 0, 0, 0])
        d[0] += 1; d[1] += c["a_tiempo"] == "Sí"; d[2] += int(c["dias_retraso"]); d[3] += float(c["monto"])
    return {"proveedores": [{"proveedor": p, "ordenes": x[0], "a_tiempo_pct": round(x[1] / x[0] * 100), "retraso_promedio_dias": round(x[2] / x[0], 1), "compras_soles": round(x[3])} for p, x in sorted(g.items())]}

STR = {"type": "string"}
TOOLS = [
    {"name": "resumen_ventas",
     "description": "Resumen de ventas 2025 de Distribuidora Andina S.A.C., una empresa ficticia de práctica: venta, margen, pedidos, vencido por cobrar y desgloses por mes, región, canal, vendedor y producto. Todos los filtros son opcionales.",
     "inputSchema": {"type": "object", "properties": {"mes": {"type": "integer", "minimum": 1, "maximum": 12, "description": "Mes de 2025, de 1 a 12"},
        "region": dict(STR, description="Lima, Norte, Sur o Centro"), "canal": dict(STR, description="Tienda, Mayorista, Online o WhatsApp"),
        "vendedor": dict(STR, description="Nombre completo del vendedor"), "proveedor": dict(STR, description="Nombre del proveedor"),
        "categoria": dict(STR, description="Café y cacao, Granos andinos, Harinas y pastas, Bebidas, Snacks o Limpieza")}}},
    {"name": "entregas_proveedores",
     "description": "Cumplimiento de entregas de los proveedores en 2025: órdenes, porcentaje a tiempo, retraso promedio en días y monto comprado.",
     "inputSchema": {"type": "object", "properties": {"proveedor": dict(STR, description="Opcional: nombre del proveedor")}}},
]
HANDLERS = {"resumen_ventas": resumen_ventas, "entregas_proveedores": entregas_proveedores}

def mcp_responder(msg):
    mid, method, params = msg.get("id"), msg.get("method"), msg.get("params") or {}
    if mid is None:
        return None  # notificación
    if method == "initialize":
        res = {"protocolVersion": params.get("protocolVersion", "2025-06-18"), "capabilities": {"tools": {"listChanged": False}},
               "serverInfo": {"name": "ventas-andina", "version": "1.0.0"},
               "instructions": "Datos ficticios de práctica del curso AI Productivity Engineering (eIA). Usa resumen_ventas para preguntas de ventas y entregas_proveedores para proveedores."}
    elif method == "ping":
        res = {}
    elif method == "tools/list":
        res = {"tools": TOOLS}
    elif method == "tools/call":
        fn = HANDLERS.get(params.get("name"))
        if not fn:
            return {"jsonrpc": "2.0", "id": mid, "error": {"code": -32602, "message": "herramienta desconocida"}}
        try:
            out = fn(params.get("arguments") or {})
            res = {"content": [{"type": "text", "text": json.dumps(out, ensure_ascii=False)}], "structuredContent": out, "isError": False}
        except Exception as e:
            res = {"content": [{"type": "text", "text": "Error al consultar los datos: " + str(e)}], "isError": True}
    else:
        return {"jsonrpc": "2.0", "id": mid, "error": {"code": -32601, "message": "método no soportado"}}
    return {"jsonrpc": "2.0", "id": mid, "result": res}

class H(BaseHTTPRequestHandler):
    def _cors(self):
        o = self.headers.get("Origin", "")
        if o in ALLOWED:
            self.send_header("Access-Control-Allow-Origin", o)
            self.send_header("Vary", "Origin")
            self.send_header("Access-Control-Allow-Headers", "Content-Type, X-Admin-Key")
            self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")

    def _json(self, code, obj):
        body = json.dumps(obj, ensure_ascii=False).encode()
        self.send_response(code)
        self._cors()
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, *a):
        pass

    def do_OPTIONS(self):
        self.send_response(204); self._cors(); self.end_headers()

    def _admin(self):
        return hmac.compare_digest(self.headers.get("X-Admin-Key", ""), ADMIN_KEY)

    def _q(self, k):
        from urllib.parse import urlparse, parse_qs
        return (parse_qs(urlparse(self.path).query).get(k) or [""])[0]

    def do_GET(self):
        if self.path.startswith("/health"):
            return self._json(200, {"ok": True})
        if self.path.startswith("/mcp"):
            if "text/event-stream" in self.headers.get("Accept", "") or "text/html" not in self.headers.get("Accept", ""):
                return self._json(405, {"error": "Este es un servidor MCP: los clientes deben usar POST"})
            herramientas = "".join(f"<li><code>{t['name']}</code>: {t['description']}</li>" for t in TOOLS)
            html = f"""<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Servidor MCP · Ventas Andina</title><style>body{{font:16px/1.6 system-ui,sans-serif;max-width:720px;margin:40px auto;padding:0 16px;color:#101B3D}}
code{{background:#EEF4FF;padding:2px 6px;border-radius:6px}}.u{{background:#EEF4FF;padding:12px;border-radius:10px;font-family:monospace;word-break:break-all}}</style></head><body>
<h1>Servidor MCP · Ventas Andina</h1>
<p>Esta dirección funciona: es un <b>servidor MCP</b> del curso AI Productivity Engineering (eIA). No es una página para abrir en el navegador, sino para conectarla a una IA como Claude.</p>
<p class="u">https://ai.tunky.net/encuesta-api/mcp</p>
<h2>Cómo conectarlo en Claude</h2>
<ol><li>claude.ai → Configuración → Conectores → Agregar conector personalizado.</li><li>Nombre: Ventas Andina. URL: la de arriba.</li><li>En un chat nuevo, activa el conector y pregunta por las ventas.</li></ol>
<h2>Herramientas</h2><ul>{herramientas}</ul>
<p>Datos ficticios de práctica. Funciona con Claude gratis (1 conector personalizado). ChatGPT necesita plan Plus o superior.</p></body></html>"""
            body = html.encode()
            self.send_response(200); self.send_header("Content-Type", "text/html; charset=utf-8"); self.send_header("Content-Length", str(len(body))); self.end_headers(); self.wfile.write(body)
            return
        if self.path.startswith("/plazo"):
            t = self._q("tarea") or "s1"
            return self._json(200, {"tarea": t, "plazo": PLAZOS.get(t), "ahora": int(time.time())})
        if self.path.startswith("/entregas"):
            if not self._admin():
                return self._json(401, {"error": "clave incorrecta"})
            t = self._q("tarea") or "s1"
            rows = db().execute("SELECT id, email, nombre, grupo, texto, enlace, archivo_nombre, ts FROM entregas WHERE tarea=? ORDER BY ts", (t,)).fetchall()
            keys = ["id", "email", "nombre", "grupo", "texto", "enlace", "archivo", "ts"]
            return self._json(200, {"tarea": t, "plazo": PLAZOS.get(t), "entregas": [dict(zip(keys, r)) for r in rows]})
        if self.path.startswith("/archivo"):
            if not self._admin():
                return self._json(401, {"error": "clave incorrecta"})
            r = db().execute("SELECT archivo_nombre, archivo_tipo, archivo_path FROM entregas WHERE id=?", (self._q("id"),)).fetchone()
            if not r or not r[2] or not os.path.exists(r[2]):
                return self._json(404, {"error": "sin archivo"})
            data = open(r[2], "rb").read()
            self.send_response(200); self._cors()
            self.send_header("Content-Type", "application/octet-stream")
            self.send_header("Content-Disposition", "attachment; filename*=UTF-8''" + __import__("urllib.parse").parse.quote(r[0]))
            self.send_header("Content-Length", str(len(data))); self.end_headers(); self.wfile.write(data)
            return
        if self.path.startswith("/results"):
            if not hmac.compare_digest(self.headers.get("X-Admin-Key", ""), ADMIN_KEY):
                return self._json(401, {"error": "clave incorrecta"})
            rows = db().execute("SELECT ts, answers FROM votos ORDER BY ts").fetchall()
            totals, texts = {}, {}
            for ts, a in rows:
                for q, v in json.loads(a).items():
                    if isinstance(v, list):
                        for opt in v:
                            totals.setdefault(q, {}).setdefault(opt, 0); totals[q][opt] += 1
                    elif isinstance(v, str) and v.strip():
                        if q.startswith("t_"):
                            texts.setdefault(q, []).append(v.strip())
                        else:
                            totals.setdefault(q, {}).setdefault(v, 0); totals[q][v] += 1
            return self._json(200, {"votos": len(rows), "totales": totals, "textos": texts,
                                    "ultimo": rows[-1][0] if rows else None})
        self._json(404, {"error": "no encontrado"})

    def do_POST(self):
        if self.path.startswith("/mcp"):
            return self._mcp()
        if self.headers.get("Origin", "") not in ALLOWED:
            return self._json(403, {"error": "origen no permitido"})
        if self.path.startswith("/entrega"):
            return self._entrega()
        if not self.path.startswith("/vote"):
            return self._json(404, {"error": "no encontrado"})
        try:
            n = min(int(self.headers.get("Content-Length", 0)), 20000)
            data = json.loads(self.rfile.read(n))
            token = str(data["token"])[:64]
            answers = data["answers"]
            assert isinstance(answers, dict) and len(token) >= 16
            clean = {}
            for k, v in list(answers.items())[:30]:
                k = str(k)[:40]
                if isinstance(v, list):
                    clean[k] = [str(x)[:80] for x in v[:15]]
                else:
                    clean[k] = str(v)[:1000]
        except Exception:
            return self._json(400, {"error": "datos inválidos"})
        ip = self.headers.get("X-Forwarded-For", self.client_address[0]).split(",")[0].strip()
        iph = hashlib.sha256((SALT + ip).encode()).hexdigest()[:16]
        c = db()
        if c.execute("SELECT COUNT(*) FROM votos WHERE ip=?", (iph,)).fetchone()[0] >= MAX_PER_IP:
            return self._json(429, {"error": "demasiados votos desde esta red"})
        try:
            c.execute("INSERT INTO votos VALUES (?,?,?,?)", (token, iph, int(time.time()), json.dumps(clean, ensure_ascii=False)))
            c.commit()
        except sqlite3.IntegrityError:
            return self._json(409, {"error": "ya votaste"})
        self._json(201, {"ok": True})

    def _mcp(self):
        try:
            n = min(int(self.headers.get("Content-Length", 0)), 200000)
            body = json.loads(self.rfile.read(n))
        except Exception:
            return self._json(400, {"jsonrpc": "2.0", "id": None, "error": {"code": -32700, "message": "JSON inválido"}})
        if isinstance(body, list):
            out = [r for r in (mcp_responder(m) for m in body) if r]
        else:
            out = mcp_responder(body)
        if not out:
            self.send_response(202); self.end_headers(); return
        self._json(200, out)

    def _entrega(self):
        try:
            n = int(self.headers.get("Content-Length", 0))
            if n > MAX_FILE * 1.4 + 200000:
                return self._json(413, {"error": "el archivo supera 10 MB"})
            d = json.loads(self.rfile.read(n))
            tarea = str(d.get("tarea", "s1"))[:10]
            email = str(d.get("email", "")).strip().lower()[:254]
            nombre = str(d.get("nombre", "")).strip()[:120]
            grupo = str(d.get("grupo", "")).strip()[:120]
            texto = str(d.get("texto", "")).strip()[:20000]
            enlace = str(d.get("enlace", "")).strip()[:500]
        except Exception:
            return self._json(400, {"error": "datos inválidos"})
        lim = plazo(tarea)
        if lim is None:
            return self._json(400, {"error": "tarea desconocida"})
        if time.time() > lim:
            return self._json(403, {"error": "el plazo de entrega ya venció"})
        if not EMAIL.match(email) or not nombre:
            return self._json(400, {"error": "falta un correo válido o tu nombre"})
        if enlace and not re.match(r"^https?://", enlace):
            return self._json(400, {"error": "el enlace debe empezar con http:// o https://"})
        a = d.get("archivo") or {}
        path = aname = atype = None
        if a.get("b64"):
            aname = os.path.basename(str(a.get("nombre", "archivo")))[:150]
            ext = aname.rsplit(".", 1)[-1].lower() if "." in aname else ""
            if ext not in EXT_OK:
                return self._json(400, {"error": "tipo de archivo no permitido"})
            try:
                raw = base64.b64decode(a["b64"], validate=True)
            except Exception:
                return self._json(400, {"error": "archivo dañado"})
            if len(raw) > MAX_FILE:
                return self._json(413, {"error": "el archivo supera 10 MB"})
            os.makedirs(FILES, exist_ok=True)
            path = os.path.join(FILES, uuid.uuid4().hex + "." + ext)
            open(path, "wb").write(raw)
            atype = str(a.get("tipo", ""))[:100]
        if not (texto or enlace or path):
            return self._json(400, {"error": "envía un texto, un enlace o un archivo"})
        ip = self.headers.get("X-Forwarded-For", self.client_address[0]).split(",")[0].strip()
        iph = hashlib.sha256((SALT + ip).encode()).hexdigest()[:16]
        c = db()
        c.execute("INSERT INTO entregas (tarea,email,nombre,grupo,texto,enlace,archivo_nombre,archivo_tipo,archivo_path,ts,ip) VALUES (?,?,?,?,?,?,?,?,?,?,?)",
                  (tarea, email, nombre, grupo, texto, enlace, aname, atype, path, int(time.time()), iph))
        c.commit()
        return self._json(201, {"ok": True, "recibido": int(time.time())})

if __name__ == "__main__":
    ThreadingHTTPServer(("0.0.0.0", 8000), H).serve_forever()
