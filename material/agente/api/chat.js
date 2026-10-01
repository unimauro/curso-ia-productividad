// Agente "Analista Andina": conversa y consulta tu API de ventas como herramienta.
// Va en tu repositorio como api/chat.js, junto a api/resumen.js. Se publica en Vercel.
//
// Variables de entorno en Vercel (Settings → Environment Variables):
//   LLM_API_KEY   tu clave de OpenRouter (openrouter.ai/keys) o de NVIDIA (build.nvidia.com)
//   LLM_MODEL     un modelo que soporte herramientas. En OpenRouter, uno gratis termina en ":free"
//   LLM_BASE_URL  opcional. OpenRouter por defecto. Para NVIDIA: https://integrate.api.nvidia.com/v1
//   API_RESUMEN   opcional. Por defecto usa /api/resumen del mismo sitio.
const SISTEMA = `Eres "Analista Andina", el analista comercial de Distribuidora Andina S.A.C., una empresa ficticia de práctica.
Respondes en español, claro y breve, con cifras en soles (S/).
Para cualquier pregunta sobre ventas, márgenes, vendedores, regiones, canales, productos o cobranza, usa SIEMPRE la herramienta resumen_ventas. Nunca inventes cifras.
Si comparas periodos, consulta cada periodo por separado. Termina con una recomendación concreta cuando ayude.`;

const HERRAMIENTAS = [{
  type: "function",
  function: {
    name: "resumen_ventas",
    description: "Resumen de ventas 2025: venta, margen, pedidos, vencido por cobrar y desgloses por mes, región, canal y productos. Filtros opcionales.",
    parameters: {
      type: "object",
      properties: {
        mes: { type: "integer", description: "Mes de 2025, de 1 a 12" },
        region: { type: "string", description: "Lima, Norte, Sur o Centro" },
        canal: { type: "string", description: "Tienda, Mayorista, Online o WhatsApp" },
        vendedor: { type: "string", description: "Nombre completo del vendedor" },
        proveedor: { type: "string" },
        categoria: { type: "string", description: "Café y cacao, Granos andinos, Harinas y pastas, Bebidas, Snacks o Limpieza" },
      },
    },
  },
}];

export default async function handler(req, res) {
  res.setHeader("Access-Control-Allow-Origin", "*");
  res.setHeader("Access-Control-Allow-Headers", "Content-Type");
  if (req.method === "OPTIONS") return res.status(204).end();
  if (req.method !== "POST") return res.status(405).json({ error: "Usa POST" });
  const key = process.env.LLM_API_KEY, modelo = process.env.LLM_MODEL;
  if (!key || !modelo) return res.status(500).json({ error: "Falta configurar LLM_API_KEY o LLM_MODEL en Vercel" });
  const base = process.env.LLM_BASE_URL || "https://openrouter.ai/api/v1";
  const apiResumen = process.env.API_RESUMEN || `https://${req.headers.host}/api/resumen`;

  const historial = Array.isArray(req.body?.mensajes) ? req.body.mensajes.slice(-10) : [];
  const mensajes = [{ role: "system", content: SISTEMA }, ...historial.map(m => ({ role: m.role === "assistant" ? "assistant" : "user", content: String(m.content).slice(0, 2000) }))];
  const consultas = [];

  try {
    for (let paso = 0; paso < 5; paso++) {
      const r = await fetch(base + "/chat/completions", {
        method: "POST",
        headers: { "Authorization": `Bearer ${key}`, "Content-Type": "application/json" },
        body: JSON.stringify({ model: modelo, messages: mensajes, tools: HERRAMIENTAS, temperature: 0.2 }),
      });
      const j = await r.json();
      if (!r.ok) return res.status(502).json({ error: "El modelo no respondió", detalle: j.error?.message || j });
      const msg = j.choices?.[0]?.message;
      if (!msg) return res.status(502).json({ error: "Respuesta vacía del modelo" });
      mensajes.push(msg);
      if (!msg.tool_calls?.length) return res.status(200).json({ respuesta: msg.content, consultas });
      for (const tc of msg.tool_calls) {
        let args = {};
        try { args = JSON.parse(tc.function.arguments || "{}"); } catch (e) {}
        const url = new URL(apiResumen);
        for (const [k, v] of Object.entries(args)) if (v !== undefined && v !== null && v !== "") url.searchParams.set(k, v);
        consultas.push(url.search || "(todo el año)");
        const datos = await (await fetch(url)).text();
        mensajes.push({ role: "tool", tool_call_id: tc.id, content: datos.slice(0, 12000) });
      }
    }
    return res.status(200).json({ respuesta: "No pude terminar el análisis. Intenta con una pregunta más concreta.", consultas });
  } catch (e) {
    return res.status(500).json({ error: "Error del agente", detalle: String(e) });
  }
}
