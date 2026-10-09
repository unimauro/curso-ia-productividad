> Prompt usado en clase el jueves 8 de octubre de 2026: bot de ventas con IA conectado a un número de Twilio desde una app de Lovable (Casas para Gatos). Lo usamos porque la conexión con Kapso falló en vivo. AI Productivity Engineering, eIA.

Quiero complementar la aplicación existente de venta de casas para gatos agregando un **bot de ventas con IA conectado al número de Twilio que ya está configurado en el proyecto**.

IMPORTANTE:

* NO rehacer la aplicación existente.
* NO modificar funcionalidades que ya funcionan.
* Utilizar la infraestructura, autenticación, base de datos y componentes existentes siempre que sea posible.
* Primero revisar la arquitectura actual del proyecto, las tablas existentes y la integración actual con Twilio antes de crear nuevos componentes.
* La funcionalidad debe quedar integrada dentro del Admin existente.

## 1. OBJETIVO

Quiero que el número de Twilio funcione como un **asistente comercial automático para vender casas para gatos**.

Cuando una persona escriba al número de WhatsApp/SMS conectado a Twilio:

1. Twilio recibe el mensaje.
2. El mensaje llega al backend de la aplicación.
3. La IA analiza la intención del cliente.
4. La IA responde automáticamente.
5. La respuesta debe tener como máximo **2 líneas**, ser natural y comercial.
6. La conversación debe quedar registrada.
7. El número del cliente debe quedar asociado a un Lead.
8. El Admin debe mostrar el lead y toda su conversación.
9. La IA debe intentar convertir la conversación en una oportunidad de venta.

## 2. FLUJO COMERCIAL

El bot debe comportarse como un vendedor, no como un chatbot genérico.

Debe intentar obtener progresivamente:

* Nombre del cliente.
* Producto/casa para gato de interés.
* Cantidad.
* Ciudad/distrito.
* Si desea delivery.
* Si desea comprar ahora o está cotizando.
* Teléfono/WhatsApp, obtenido automáticamente desde Twilio cuando esté disponible.
* Cualquier otra información necesaria para cerrar la venta.

NO debe hacer todas las preguntas juntas.

Debe mantener una conversación natural.

Ejemplo:

Cliente:
"Hola, cuánto cuesta la casa grande?"

Bot:
"¡Hola! 😊 La casa grande cuesta S/ XXX. ¿Quieres que te muestre los modelos disponibles?"

Cliente:
"Sí"

Bot:
"Perfecto 😺 Tenemos varios modelos. ¿La buscas para un gato o para más de uno?"

Cliente:
"Para dos"

Bot:
"¡Perfecto! Tenemos una opción ideal para dos gatos. ¿En qué distrito estás para calcularte el delivery?"

## 3. RESPUESTAS DE LA IA

Las respuestas deben:

* Ser máximo de 2 líneas.
* Ser cortas y comerciales.
* Sonar humanas.
* Utilizar español.
* Ser amigables.
* No inventar precios, productos, stock o promociones.
* Utilizar únicamente información existente en la base de datos/productos.
* No utilizar respuestas excesivamente largas.
* Evitar lenguaje demasiado formal.
* Utilizar emojis moderadamente.
* Hacer una sola pregunta principal por mensaje cuando sea necesario.

La IA debe priorizar:

1. Responder la pregunta.
2. Detectar intención de compra.
3. Obtener información faltante.
4. Recomendar un producto.
5. Llevar al cliente hacia la compra.

## 4. DETECCIÓN DE INTENCIÓN

La IA debe clasificar cada mensaje/conversación con una intención:

* CONSULTA
* INTERESADO
* COTIZACION
* INTENCION_COMPRA
* COMPRA
* DELIVERY
* POSTVENTA
* RECLAMO
* OTRO

También debe calcular un estado comercial del Lead:

* NUEVO
* CONTACTADO
* INTERESADO
* CALIENTE
* CONVERTIDO
* PERDIDO

Cuando el cliente muestre intención clara de compra, marcar automáticamente el lead como **CALIENTE**.

Ejemplos de señales:

"Lo quiero"
"Cómo pago?"
"Quiero comprar"
"Me lo puedes enviar?"
"Quiero ese modelo"
"Cuánto sale con delivery?"
"Cómo hago para pedirlo?"

## 5. LEADS

Crear o reutilizar una entidad de Lead existente.

Cada Lead debe tener como mínimo:

* id
* nombre
* teléfono
* canal
* producto_interes
* cantidad
* ciudad
* distrito
* estado
* intención
* score
* fecha_primer_contacto
* fecha_ultimo_contacto
* resumen_conversacion
* created_at
* updated_at

El teléfono debe ser el identificador principal para evitar crear duplicados.

Si el número ya existe:

* No crear otro Lead.
* Continuar la conversación existente.
* Actualizar la información del Lead.

Si el número no existe:

* Crear automáticamente un nuevo Lead.

## 6. REGISTRO DE CONVERSACIONES

Guardar absolutamente todos los mensajes.

Crear o reutilizar una estructura tipo Conversation:

* id
* lead_id
* phone_number
* channel
* status
* started_at
* last_message_at

Y una estructura Message:

* id
* conversation_id
* lead_id
* direction
* sender
* message
* message_type
* ai_generated
* intent
* created_at

Valores de direction:

* INBOUND
* OUTBOUND

Valores de sender:

* CUSTOMER
* AI
* ADMIN

Cada mensaje recibido desde Twilio debe registrarse.

Cada respuesta enviada por Twilio también debe registrarse.

Debe ser posible reconstruir la conversación completa en orden cronológico.

## 7. INTEGRACIÓN CON TWILIO

Utilizar el número de Twilio que YA está configurado en el proyecto.

No crear un número nuevo.

Implementar/verificar un webhook para recibir mensajes entrantes.

Ejemplo conceptual:

POST /api/twilio/webhook

El webhook debe:

1. Validar la solicitud de Twilio cuando sea posible.
2. Obtener:

   * número del cliente
   * número Twilio
   * mensaje
   * MessageSid
   * fecha/hora
3. Buscar el Lead por número.
4. Crear Lead si no existe.
5. Buscar/crear Conversation.
6. Guardar el mensaje entrante.
7. Enviar el contexto relevante a la IA.
8. Obtener la respuesta de la IA.
9. Guardar la respuesta.
10. Enviar la respuesta mediante Twilio.
11. Actualizar el Lead.

Evitar respuestas duplicadas utilizando el MessageSid de Twilio como identificador/idempotency key.

## 8. IA

Utilizar la capacidad de IA disponible actualmente en Lovable/proyecto.

NO agregar un proveedor externo si Lovable ya tiene una integración de IA funcional.

Crear un prompt interno para el agente comercial.

Contexto que debe recibir la IA:

* Datos del cliente.
* Historial reciente de conversación.
* Productos disponibles.
* Precio.
* Stock/disponibilidad.
* Información de delivery.
* Promociones vigentes.
* Estado actual del Lead.

La IA debe devolver estructuradamente:

{
"reply": "respuesta de máximo 2 líneas",
"intent": "INTERESADO",
"lead_status": "CALIENTE",
"product_id": "...",
"customer_name": "...",
"city": "...",
"district": "...",
"purchase_intent": true,
"summary": "..."
}

Si un campo no puede determinarse, dejarlo como null.

## 9. ADMIN

Agregar dentro del Admin una sección:

**Conversaciones / WhatsApp**

Debe permitir:

* Ver todos los leads.
* Buscar por teléfono.
* Buscar por nombre.
* Filtrar por estado.
* Filtrar por intención.
* Filtrar por fecha.
* Ver cantidad de conversaciones.
* Ver última interacción.
* Ver si la conversación está activa.
* Ver si la IA está habilitada.

Al seleccionar un Lead:

Mostrar:

### Información del Lead

* Nombre
* WhatsApp/teléfono
* Producto de interés
* Ciudad
* Distrito
* Estado
* Intención
* Score
* Fecha de primer contacto
* Último contacto

### Conversación

Mostrar la conversación como un chat:

Cliente:
"Hola, cuánto cuesta?"

IA:
"¡Hola! 😺 La casa cuesta S/ XXX. ¿Quieres que te muestre los modelos disponibles?"

Cada mensaje debe mostrar:

* fecha/hora
* remitente
* contenido
* indicador de IA si corresponde

## 10. CONTROL MANUAL

Desde el Admin debe existir la posibilidad de:

* Activar/desactivar IA para un Lead.
* Responder manualmente.
* Tomar control de una conversación.
* Devolver la conversación a la IA.

Estados:

AI_ACTIVE
HUMAN_ACTIVE

Si un administrador responde manualmente:

* La IA debe dejar de responder automáticamente para esa conversación.
* El mensaje manual debe quedar registrado como ADMIN.

## 11. RESUMEN AUTOMÁTICO

La IA debe mantener un resumen corto de cada conversación.

Ejemplo:

"Cliente interesado en casa modelo Premium para 2 gatos. Vive en Miraflores. Preguntó por precio y delivery. Alta intención de compra."

Actualizar el resumen después de cada interacción relevante.

## 12. MÉTRICAS DEL ADMIN

Agregar un pequeño dashboard comercial:

* Leads recibidos hoy.
* Leads recibidos esta semana.
* Conversaciones activas.
* Leads interesados.
* Leads calientes.
* Ventas/conversiones.
* Tasa de conversión.
* Mensajes recibidos.
* Mensajes enviados por IA.
* Conversaciones atendidas por humano.

## 13. SEGURIDAD

Las credenciales de Twilio y cualquier API key deben permanecer exclusivamente en variables de entorno/secrets.

Nunca exponer:

* TWILIO_AUTH_TOKEN
* API keys
* credenciales
* secretos

en frontend, logs visibles o código cliente.

## 14. MANEJO DE ERRORES

Si la IA falla:

* Registrar el error.
* No perder el mensaje del cliente.
* Intentar enviar una respuesta fallback.

Ejemplo:

"¡Hola! 😊 Recibí tu mensaje. En un momento te ayudamos con tu consulta."

Si Twilio falla:

* Registrar el error.
* Mantener el mensaje almacenado.
* Permitir reintento.

Si el producto consultado no existe:

"No inventar información."

## 15. EXPERIENCIA DEL ADMIN

El objetivo es que un administrador pueda entrar y ver:

**Leads → Conversación → Información comercial → Estado → Acción**

Ejemplo:

Carlos
📱 +51XXXXXXXXX
🔥 CALIENTE
🏠 Casa Premium
📍 Miraflores
💰 Intención de compra

[Ver conversación]

Y debajo:

Cliente:
"Quiero comprar la grande"

IA:
"¡Excelente! 😺 La casa grande está disponible. ¿En qué distrito estás para calcularte el delivery?"

## 16. NO DUPLICAR INFORMACIÓN

Antes de crear tablas, endpoints o componentes:

1. Revisar si ya existe Lead.
2. Revisar si ya existe Customer.
3. Revisar si ya existe Conversation.
4. Revisar si ya existe Message.
5. Revisar la integración actual con Twilio.
6. Reutilizar estructuras existentes cuando sea posible.

Solo crear nuevas estructuras cuando realmente sean necesarias.

## 17. CRITERIO DE ÉXITO

La implementación se considera terminada cuando pueda hacer esta prueba:

1. Una persona escribe al número de Twilio.
2. El mensaje llega a la aplicación.
3. Se identifica/crea el Lead por número.
4. Se crea/recupera la conversación.
5. Se registra el mensaje.
6. La IA genera una respuesta comercial de máximo 2 líneas.
7. Twilio envía la respuesta.
8. La respuesta queda registrada.
9. El Lead se actualiza automáticamente.
10. Desde Admin puedo buscar el número.
11. Desde Admin puedo ver toda la conversación.
12. Desde Admin puedo ver el estado comercial del Lead.
13. Puedo tomar control manual de la conversación.
14. La IA deja de responder cuando un humano toma control.
15. No se generan Leads duplicados.
16. No se generan respuestas duplicadas ante reintentos de Twilio.

Antes de terminar, probar el flujo completo con al menos 3 números diferentes y documentar cualquier variable de entorno o configuración de Twilio que deba configurar manualmente.

No crear datos ficticios de producción ni reemplazar la configuración actual de Twilio.
