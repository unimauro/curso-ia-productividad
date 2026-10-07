// Bot de WhatsApp OFICIAL (WhatsApp Cloud API de Meta) con IA, para publicar en Vercel.
// Va en tu repositorio como api/webhook.js. En Meta, la URL del webhook es https://TU-PROYECTO.vercel.app/api/webhook
//
// Variables de entorno en Vercel (Settings → Environment Variables):
//   WHATSAPP_TOKEN   token de acceso de tu app en Meta for Developers (WhatsApp → API Setup)
//   PHONE_NUMBER_ID  identificador del número de prueba (WhatsApp → API Setup)
//   VERIFY_TOKEN     una palabra secreta que inventas y repites en Meta al configurar el webhook
//   LLM_API_KEY      tu clave de OpenRouter (openrouter.ai/keys) o de NVIDIA (build.nvidia.com)
//   LLM_MODEL        el modelo. En OpenRouter, uno gratis termina en ":free"
//   LLM_BASE_URL     opcional. OpenRouter por defecto. Para NVIDIA: https://integrate.api.nvidia.com/v1
//   CATALOGO_URL     opcional. Por defecto, el catálogo de práctica del curso
//   GRAPH_VERSION    opcional. Versión de la API de Meta, por defecto v23.0
//
// Reglas de Meta desde el 15 de enero de 2026: el bot debe atender TU negocio (productos, pedidos,
// citas, preguntas frecuentes). Un asistente de propósito general tipo ChatGPT no está permitido.
const CATALOGO = process.env.CATALOGO_URL || "https://unimauro.github.io/curso-ia-productividad/material/catalogo-2025.json";
const HUMANO = /asesor|humano|persona|hablar con alguien/i;

const sistema = catalogo => `Eres el asistente de WhatsApp de ${catalogo.empresa}.
Respondes en español, en máximo 4 líneas, con montos en soles (S/).
Solo hablas de este negocio: productos, precios, pedido mínimo, entregas, zonas, horario y medios de pago.
Usa SOLO estos datos. Si algo no está aquí, di que no tienes ese dato y ofrece un asesor. Nunca inventes precios, descuentos ni promociones.
Si te piden algo que no es del negocio, explica amablemente que solo atiendes consultas de la tienda.
Si el cliente quiere comprar, pide su nombre, negocio y distrito, y dile que un asesor confirmará el pedido.
DATOS:
${JSON.stringify(catalogo)}`;

async function enviar(para, texto) {
  const v = process.env.GRAPH_VERSION || "v23.0";
  const r = await fetch(`https://graph.facebook.com/${v}/${process.env.PHONE_NUMBER_ID}/messages`, {
    method: "POST",
    headers: { "Authorization": `Bearer ${process.env.WHATSAPP_TOKEN}`, "Content-Type": "application/json" },
    body: JSON.stringify({ messaging_product: "whatsapp", to: para, type: "text", text: { body: texto.slice(0, 4000) } }),
  });
  if (!r.ok) console.error("Meta rechazó el envío", r.status, await r.text());
}

async function responderConIA(pregunta) {
  const catalogo = await (await fetch(CATALOGO)).json();
  const r = await fetch((process.env.LLM_BASE_URL || "https://openrouter.ai/api/v1") + "/chat/completions", {
    method: "POST",
    headers: { "Authorization": `Bearer ${process.env.LLM_API_KEY}`, "Content-Type": "application/json" },
    body: JSON.stringify({ model: process.env.LLM_MODEL, temperature: 0.2, messages: [{ role: "system", content: sistema(catalogo) }, { role: "user", content: pregunta.slice(0, 1000) }] }),
  });
  const j = await r.json();
  if (!r.ok) throw new Error(j.error?.message || "El modelo no respondió");
  return j.choices?.[0]?.message?.content || "No pude responder ahora. Un asesor te escribirá pronto.";
}

export default async function handler(req, res) {
  // 1. Meta verifica tu webhook con un GET una sola vez.
  if (req.method === "GET") {
    const q = req.query || {};
    if (q["hub.mode"] === "subscribe" && q["hub.verify_token"] === process.env.VERIFY_TOKEN) return res.status(200).send(q["hub.challenge"]);
    return res.status(403).send("VERIFY_TOKEN incorrecto");
  }
  if (req.method !== "POST") return res.status(405).end();

  // 2. Cada mensaje del cliente llega como POST. Los avisos de entregado o leído se ignoran.
  const msg = req.body?.entry?.[0]?.changes?.[0]?.value?.messages?.[0];
  if (!msg) return res.status(200).json({ ok: true });
  if (msg.type !== "text") {
    await enviar(msg.from, "Por ahora solo leo mensajes de texto. ¿En qué te ayudo?");
    return res.status(200).json({ ok: true });
  }
  const texto = msg.text.body;
  try {
    // 3. Pase a humano: el bot no insiste si el cliente pide una persona.
    if (HUMANO.test(texto)) {
      console.log("PASE A HUMANO", msg.from, texto);
      await enviar(msg.from, "Claro. Un asesor te escribirá por aquí en horario de atención. Gracias por tu paciencia.");
    } else {
      await enviar(msg.from, await responderConIA(texto));
    }
  } catch (e) {
    console.error(e);
    await enviar(msg.from, "Tuve un problema para responder. Un asesor te escribirá pronto.");
  }
  return res.status(200).json({ ok: true });
}
