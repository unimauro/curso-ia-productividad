// API de ventas de Distribuidora Andina (empresa ficticia).
// Copia este archivo en tu repositorio como api/resumen.js y publícalo en Vercel.
// Ejemplos:
//   /api/resumen                     -> resumen del año
//   /api/resumen?mes=12              -> diciembre
//   /api/resumen?region=Norte&mes=9  -> Norte en setiembre
//   /api/resumen?vendedor=Ana%20Quispe
const DATOS = "https://unimauro.github.io/curso-ia-productividad/material/ventas-2025.json";
let cache = null;

export default async function handler(req, res) {
  res.setHeader("Access-Control-Allow-Origin", "*");
  try {
    if (!cache) cache = await (await fetch(DATOS)).json();
    const q = req.query || {};
    const filtros = ["mes", "region", "canal", "vendedor", "proveedor", "categoria"];
    const filas = cache.filter(v => filtros.every(f => !q[f] || String(v[f]).toLowerCase() === String(q[f]).toLowerCase()));
    const suma = (rows, k) => rows.reduce((a, v) => a + v[k], 0);
    const agrupar = (k) => {
      const g = {};
      for (const v of filas) g[v[k]] = (g[v[k]] || 0) + v.venta;
      return Object.entries(g).map(([nombre, venta]) => ({ nombre, venta: Math.round(venta) })).sort((a, b) => b.venta - a.venta);
    };
    const venta = suma(filas, "venta"), margen = suma(filas, "margen");
    const vencido = suma(filas.filter(v => v.estado_pago === "Vencido"), "venta");
    res.status(200).json({
      empresa: "Distribuidora Andina S.A.C. (ficticia)",
      filtros: Object.fromEntries(filtros.filter(f => q[f]).map(f => [f, q[f]])),
      pedidos: new Set(filas.map(v => v.pedido)).size,
      venta: Math.round(venta),
      margen: Math.round(margen),
      margen_pct: venta ? Math.round(margen / venta * 1000) / 10 : 0,
      vencido_por_cobrar: Math.round(vencido),
      por_mes: agrupar("mes").sort((a, b) => a.nombre - b.nombre),
      por_region: agrupar("region"),
      por_canal: agrupar("canal"),
      top_productos: agrupar("producto").slice(0, 5),
    });
  } catch (e) {
    res.status(500).json({ error: "No se pudieron leer los datos", detalle: String(e) });
  }
}
