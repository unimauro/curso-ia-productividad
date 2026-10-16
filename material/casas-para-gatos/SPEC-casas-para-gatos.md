> Proyecto de práctica: landing de casas para gatos con cotización por IA y publicación en LinkedIn. Cambia TU_CORREO por tu correo de administrador. Si se te acaban los créditos, constrúyelo en el orden de la sección 23. AI Productivity Engineering, eIA.

CONSTRUIR MVP FUNCIONAL — LANDING + COTIZACIÓN IA + LINKEDIN

Quiero construir un MVP funcional y simple de una plataforma comercial para una empresa que vende CASAS PARA GATOS.

IMPORTANTE:
Optimiza el trabajo para consumir la menor cantidad posible de créditos de Lovable.

NO construir funcionalidades innecesarias.
NO construir múltiples roles.
NO construir un CRM complejo.
NO construir un sistema multi-tenant.
NO construir demasiadas pantallas.
NO crear funcionalidades que no sean necesarias para demostrar el flujo completo.

El objetivo es tener un MVP funcional end-to-end.

==================================================
OBJETIVO PRINCIPAL
==================================================

El sistema debe demostrar DOS FLUJOS conectados:

FLUJO A — MARKETING

Producto
→ IA genera publicación
→ IA genera imagen
→ Preview
→ Carlos aprueba
→ Publicar en LinkedIn
→ URL con tracking
→ visitante llega a landing
→ solicita cotización

FLUJO B — SALES

Landing
→ visitante ve productos
→ solicita cotización
→ se registra lead
→ IA interpreta necesidad
→ IA selecciona producto del catálogo
→ genera cotización
→ genera email HTML
→ programa email +4 minutos
→ envía email
→ registra resultado
→ Carlos ve todo el journey

El sistema debe conectar ambos flujos.

==================================================
1. ADMINISTRADOR
==================================================

Crear autenticación con Supabase.

ÚNICO usuario administrador inicial:

Email:
TU_CORREO

Este usuario debe tener rol:

admin

No crear sistema complejo de roles.

El administrador debe poder acceder a:

/admin

Si un usuario no autenticado intenta entrar a /admin, redirigir al login.

==================================================
2. LANDING
==================================================

Crear una landing moderna y responsive para:

CASAS PARA GATOS

Hero:

"El espacio perfecto para tu gato"

Subtítulo:

"Cuéntanos qué necesita tu gato y recibe una cotización personalizada."

Botón:

"Solicitar cotización"

Secciones:

- Hero
- Productos destacados
- Beneficios
- Cómo funciona
- CTA
- Footer

NO crear demasiadas secciones.

La prioridad es conversión.

==================================================
3. CATÁLOGO
==================================================

Crear solamente una tabla products.

Campos:

id
name
description
price
currency
image_url
features
tags
active
created_at

Crear 5 productos demo:

1. Casa Premium XL
2. Casa Comfort
3. Refugio Cozy
4. Cama Deluxe
5. Torre para Gatos

Usar precios y características reales de los datos demo.

El catálogo debe mostrarse en la landing.

El administrador debe poder:

- crear producto
- editar producto
- activar/desactivar producto

No crear todavía variantes complejas.

==================================================
4. FORMULARIO DE COTIZACIÓN
==================================================

Al hacer clic en:

"Solicitar cotización"

mostrar formulario:

Nombre
Apellido
Email
WhatsApp
Número de gatos
Tamaño de los gatos
Uso interior/exterior
Color preferido
Presupuesto
Comentarios

Agregar un campo grande:

"Cuéntanos qué necesitas"

Ejemplo:

"Tengo dos gatos grandes y quiero una casa gris para mi sala. Mi presupuesto es de 400 soles."

Al enviar:

crear customer/lead y quote_request.

Mostrar:

"Gracias. Estamos preparando tu cotización personalizada."

==================================================
5. DATABASE
==================================================

Mantener la base de datos SIMPLE.

Crear solamente estas tablas:

customers

quote_requests

products

quotes

quote_items

email_messages

marketing_posts

activity_logs

NO crear tablas innecesarias.

quote_requests debe almacenar:

customer_id
request_text
source
medium
campaign
content
status
ai_analysis
created_at

Esto permitirá saber si el lead llegó desde LinkedIn.

==================================================
6. IA PARA COTIZACIÓN
==================================================

Crear una Edge Function o servicio backend:

analyze-quote

La IA recibe:

- solicitud del cliente
- catálogo de productos activos

La IA debe identificar:

- cantidad de gatos
- tamaño
- uso
- color
- presupuesto
- necesidades

Luego recomendar productos existentes.

MUY IMPORTANTE:

La IA NO puede inventar:

- productos
- precios
- características
- stock

Los precios deben venir exclusivamente de products.

La IA debe devolver JSON estructurado.

Ejemplo:

{
  "needs": {
    "cats": 2,
    "size": "large",
    "usage": "indoor",
    "color": "gray",
    "budget": 400
  },
  "recommended_product_id": "..."
}

==================================================
7. GENERAR COTIZACIÓN
==================================================

Crear automáticamente una quote.

La cotización debe contener:

- producto
- cantidad
- precio
- total
- fecha
- validez

No permitir que la IA invente el precio.

El precio siempre debe venir de products.

Generar número:

QT-2026-0001

o equivalente.

==================================================
8. EMAIL HTML
==================================================

Después de crear la cotización:

generar un email HTML personalizado.

Debe contener:

- saludo
- explicación personalizada
- producto
- imagen
- características
- precio
- total
- botón "Ver cotización"
- datos de contacto

Ejemplo:

Hola Juan,

Gracias por contactarnos.

Por lo que nos comentaste, creemos que esta opción es ideal para tus gatos.

[IMAGEN]

Casa Premium XL

Precio:
S/ 349

Total:
S/ 369

[VER COTIZACIÓN]

Saludos,
Equipo Comercial

Crear una plantilla HTML simple y profesional.

La IA solamente debe personalizar el texto.

==================================================
9. EMAIL DELAY
==================================================

NO enviar inmediatamente.

Programar el email para:

+4 minutos

Crear una configuración:

email_delay_minutes = 4

Para el MVP, si todavía no existe proveedor de email configurado:

implementar DEMO MODE.

El sistema debe mostrar:

"Email programado"

y permitir visualizar el HTML.

La arquitectura debe quedar preparada para conectar posteriormente Resend o Amazon SES.

NO gastar créditos construyendo una integración compleja de múltiples proveedores.

==================================================
10. DASHBOARD
==================================================

Crear un dashboard sencillo:

/admin

Mostrar 4 KPIs:

- Leads
- Cotizaciones
- Emails
- Leads desde LinkedIn

Debajo:

tabla de cotizaciones recientes.

Columnas:

Cliente
Solicitud
Producto
Total
Fuente
Estado
Fecha

==================================================
11. JOURNEY DEL CLIENTE
==================================================

Al hacer clic en una cotización:

mostrar una página de detalle sencilla.

Debe mostrar:

CLIENTE

Solicitud original

ANÁLISIS IA

Producto recomendado

Cotización

Email

TIMELINE

Lead recibido
↓
IA analizó
↓
Producto seleccionado
↓
Cotización creada
↓
Email generado
↓
Email programado
↓
Email enviado

No crear un CRM completo.

==================================================
12. MARKETING
==================================================

Crear solamente una pantalla:

/admin/marketing

Debe permitir:

Seleccionar producto

[ Casa Premium XL ▼ ]

Botón:

"Generar publicación con IA"

La IA debe generar:

- texto
- CTA
- hashtags
- campaña
- URL de landing

Ejemplo:

"🐱 ¿Tienes dos gatos grandes?

La Casa Premium XL fue diseñada para ofrecerles un espacio cómodo para descansar.

✔️ Ideal para gatos grandes
✔️ Diseño para interiores
✔️ Disponible en diferentes colores

Solicita tu cotización personalizada 👇"

==================================================
13. GENERACIÓN DE IMAGEN
==================================================

En la pantalla de Marketing debe existir:

"Generar imagen con IA"

La imagen debe estar relacionada con el producto seleccionado.

Para ahorrar créditos de Lovable:

NO generar imágenes durante el proceso de construcción.

Implementar solamente la funcionalidad y el punto de integración.

Si no existe todavía un proveedor de imágenes configurado, utilizar temporalmente la imagen del producto y mostrar claramente:

"AI image generation not configured"

El sistema debe quedar preparado para conectar posteriormente un proveedor de generación de imágenes.

==================================================
14. PREVIEW LINKEDIN
==================================================

Mostrar una tarjeta simulando una publicación de LinkedIn:

Imagen

Texto

Hashtags

CTA

URL

Botones:

[Regenerar]

[Editar]

[Aprobar y publicar]

Antes de publicar, Carlos debe poder revisar el contenido.

==================================================
15. LINKEDIN CONNECTOR
==================================================

Utilizar el LinkedIn Connector que ya está disponible en Lovable.

NO crear otra implementación OAuth.

NO crear una integración LinkedIn personalizada.

Utilizar exclusivamente las capacidades disponibles del LinkedIn Connector.

Cuando Carlos presione:

"Aprobar y publicar"

utilizar el connector para publicar si la capacidad está disponible.

Guardar:

linkedin_post_id
status
published_at
product_id
campaign
content

Estados:

draft
approved
published
failed

Si el connector no permite publicar en el entorno actual:

mostrar un mensaje claro y mantener el contenido como approved/draft.

NO crear una API falsa.

==================================================
16. TRACKING
==================================================

Cada publicación de LinkedIn debe generar una URL:

/cotizar

con parámetros:

utm_source=linkedin
utm_medium=organic
utm_campaign=<campaign>
utm_content=<product>

Cuando el usuario llegue a la landing desde esa URL y envíe el formulario:

guardar esos valores en quote_requests.

Ejemplo:

source = linkedin
medium = organic
campaign = gatos_octubre
content = casa_premium_xl

==================================================
17. MARKETING ANALYTICS
==================================================

En /admin/marketing mostrar:

Publicaciones
Leads desde LinkedIn
Cotizaciones desde LinkedIn
Conversiones

Ejemplo:

LinkedIn

Publicaciones: 3
Leads: 12
Cotizaciones: 8
Ventas: 2

No crear gráficos complejos.

Usar cards y una tabla simple.

==================================================
18. FLUJO COMPLETO A IMPLEMENTAR
==================================================

FLUJO MARKETING:

Carlos entra a:

/admin/marketing

↓

Selecciona:

Casa Premium XL

↓

Presiona:

Generar publicación con IA

↓

IA genera:

texto
CTA
hashtags
campaña
URL

↓

Carlos presiona:

Generar imagen con IA

↓

Si no hay proveedor configurado:
usar imagen del producto como fallback.

↓

Carlos revisa Preview

↓

Carlos presiona:

Aprobar y publicar

↓

Utilizar LinkedIn Connector disponible

↓

Guardar publicación y tracking.

==================================================

FLUJO SALES:

Cliente entra a landing.

↓

Ve productos.

↓

Presiona:

Solicitar cotización.

↓

Completa formulario.

↓

Se registra lead.

↓

Se guarda source/campaign si viene de LinkedIn.

↓

IA interpreta solicitud.

↓

IA selecciona producto real del catálogo.

↓

Sistema genera cotización.

↓

Sistema genera email HTML.

↓

Email queda programado para +4 minutos.

↓

Enviar cuando exista proveedor configurado.

↓

Registrar resultado.

↓

Carlos entra a /admin.

↓

Ve el lead.

↓

Puede abrir la cotización.

↓

Puede ver todo el journey.

==================================================
19. DEMO DATA
==================================================

Crear automáticamente datos demo suficientes para probar:

5 productos

5 clientes

5 solicitudes de cotización

5 cotizaciones

3 publicaciones de marketing

Al menos 2 leads provenientes de LinkedIn.

==================================================
20. DISEÑO
==================================================

Landing:

premium
limpia
moderna
responsive
orientada a conversión

Dashboard:

simple
profesional
tipo CRM ligero

No crear demasiadas animaciones.

No crear componentes innecesarios.

==================================================
21. REGLAS PARA AHORRAR CRÉDITOS
==================================================

ESTO ES MUY IMPORTANTE.

Construir primero el MVP funcional.

No construir:

- multi-tenant
- múltiples roles
- CRM avanzado
- WhatsApp
- SMS
- múltiples proveedores de email
- múltiples proveedores de IA
- workflows visuales
- sistema avanzado de permisos
- sistema avanzado de inventario
- variantes complejas
- ecommerce completo
- pagos
- facturación
- analytics avanzado

No generar imágenes durante el build.

No crear documentación extensa.

No crear páginas innecesarias.

No implementar funcionalidades que no estén relacionadas directamente con estos dos flujos:

LINKEDIN → LANDING → LEAD → COTIZACIÓN → EMAIL

y

LANDING → LEAD → COTIZACIÓN → EMAIL

==================================================
22. CRITERIO DE ÉXITO
==================================================

El MVP debe poder demostrar exactamente:

MARKETING:

1. Carlos inicia sesión.
2. Va a Marketing.
3. Selecciona un producto.
4. Genera publicación con IA.
5. Genera/selecciona imagen.
6. Ve preview.
7. Aprueba.
8. Publica usando LinkedIn Connector si está disponible.
9. Genera URL trackeada.

SALES:

1. Usuario entra a landing.
2. Ve productos.
3. Solicita cotización.
4. Se registra lead.
5. IA interpreta solicitud.
6. IA encuentra producto del catálogo.
7. Sistema genera cotización.
8. Sistema genera email HTML.
9. Email queda programado para +4 minutos.
10. Se envía cuando exista proveedor configurado.
11. Se registra resultado.
12. Carlos entra al dashboard.
13. Carlos ve todo el journey.
14. Carlos puede ver que el lead provino de LinkedIn.

==================================================
23. PRIORIDAD ABSOLUTA
==================================================

NO quiero que Lovable intente construir todo un sistema empresarial.

Quiero un MVP pequeño pero REAL.

Prioridad:

1. Base de datos
2. Landing
3. Formulario
4. Cotización IA
5. Email HTML
6. Dashboard
7. Marketing
8. LinkedIn Connector
9. Tracking

Todo debe quedar funcional y conectado.

Usar Supabase para persistencia y Edge Functions solamente donde sea necesario.

Utilizar Secrets para API keys.

No exponer credenciales en frontend.

Administrador inicial:

TU_CORREO
