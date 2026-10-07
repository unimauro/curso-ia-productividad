> **Cómo usarlo sin gastar todos tus créditos:** este prompt es largo. Pégalo como SPEC en el conocimiento del proyecto de Lovable (Project settings → Knowledge) y construye por fases con el prompt 1 de la guía: fase 1 Kanban con datos sintéticos, fase 2 Supabase con roles y RLS, fase 3 alertas con Resend, fase 4 chat y Activity Canvas. Cambia TU_CORREO por tu correo.
>
> Aporte de un participante del curso · AI Productivity Engineering, eIA.

# Prompt para Lovable — Pulso Comercial

Quiero construir una aplicación web moderna llamada **“Pulso Comercial”**, orientada al seguimiento de oportunidades comerciales y actividades de ventas.

La aplicación debe permitir visualizar y gestionar el ciclo completo de una oportunidad comercial, conectar los datos con **Supabase**, enviar alertas mediante **Resend**, permitir movimiento de oportunidades mediante **drag & drop** y contar con un **chat integrado** para consultar información comercial.

La UI debe ser **profesional, moderna, intuitiva y visualmente agradable**, tomando como referencia visual la imagen que adjunto (si no adjunto una, propón un diseño SaaS moderno).

## 1. Objetivo principal

Crear un **Sales Pipeline / Commercial Pulse Dashboard** que permita a vendedores y gerentes:

* Ver todas las oportunidades comerciales.
* Conocer en qué etapa está cada oportunidad.
* Mover oportunidades entre etapas mediante drag & drop.
* Registrar actividades.
* Detectar oportunidades sin actividad.
* Calcular un pronóstico comercial.
* Recibir alertas por correo cuando existan cambios relevantes.
* Consultar información mediante un chat.
* Mantener histórico/auditoría de los cambios.
* Tener diferentes niveles de acceso entre vendedores y gerentes.

El sistema debe ser funcional y conectado a una base de datos real en **Supabase**.

---

# 2. Pipeline comercial

Crear un tablero Kanban principal con las siguientes columnas:

1. **Nuevo**
2. **Contactado**
3. **Cotizado**
4. **Negociación**
5. **Ganado**

Agregar también una opción de estado:

* **Perdido**
* **Archivado**

Las oportunidades deben poder moverse entre columnas mediante **drag & drop**.

Cuando una oportunidad sea movida:

* Actualizar inmediatamente Supabase.
* Registrar el cambio en una tabla de auditoría.
* Registrar usuario.
* Registrar fecha/hora.
* Registrar estado anterior.
* Registrar nuevo estado.
* Generar una actividad/evento.
* Mostrar feedback visual de éxito.
* Enviar una alerta por email mediante Resend cuando corresponda.

---

# 3. Diseño visual

Utilizar una estética similar a la imagen de referencia:

### Colores

* Azul oscuro para navegación y títulos.
* Azul intenso para etapas activas.
* Verde para oportunidades ganadas.
* Gris/blanco para backgrounds.
* Cards con bordes redondeados.
* Sombras suaves.
* Excelente uso de espacios.
* Tipografía moderna y profesional.

El diseño debe ser **responsive** para desktop, tablet y mobile.

Usar componentes modernos tipo:

* Cards
* Badges
* Dropdowns
* Tooltips
* Modals
* Side panels
* Toast notifications
* Progress indicators
* Charts
* Kanban cards

Evitar una apariencia genérica de CRUD.

Quiero que parezca un producto SaaS profesional.

---

# 4. Dashboard principal

Crear un dashboard superior con KPIs:

### Pipeline

* Total de oportunidades
* Valor total del pipeline
* Valor ponderado
* Oportunidades ganadas
* Oportunidades perdidas
* Tasa de conversión
* Ticket promedio

### Forecast

Calcular:

**Forecast = monto × probabilidad**

Ejemplo:

Una oportunidad de:

`$20,000`

con probabilidad:

`70%`

debe mostrar:

`$14,000 Forecast`

Mostrar un gráfico de forecast por etapa.

---

# 5. Kanban

Cada oportunidad debe mostrarse como una card.

Ejemplo:

**Acme Corporation**

`$25,000`

**Carlos Pérez**

Probability: `70%`

Expected close:

`Oct 30, 2026`

Last activity:

`2 days ago`

Mostrar también:

* Avatar del vendedor.
* Cliente.
* Monto.
* Probabilidad.
* Fecha estimada de cierre.
* Última actividad.
* Número de actividades.
* Indicador de riesgo.

### Risk indicators

Si pasan más de **7 días sin actividad**, mostrar:

🔴 **Sin actividad**

Si pasan entre 4 y 7 días:

🟡 **Atención**

Si hubo actividad reciente:

🟢 **Activo**

---

# 6. Drag & Drop

Implementar drag & drop real.

Cuando el usuario arrastre una oportunidad de:

`Nuevo → Contactado`

debe aparecer una confirmación visual y actualizarse automáticamente.

Ejemplo:

```text
Opportunity moved

Acme Corporation

Nuevo
↓
Contactado

Updated successfully
```

La actualización debe persistir en Supabase.

No hacer solamente un cambio visual en frontend.

---

# 7. Vista detalle de oportunidad

Al hacer click en una oportunidad abrir un **side panel o modal grande**.

Mostrar:

### Información

* Cliente
* Empresa
* Contacto
* Email
* Teléfono
* Vendedor
* Monto
* Probabilidad
* Forecast
* Fecha de creación
* Fecha estimada de cierre
* Etapa actual

### Timeline

Crear un timeline de actividades:

```text
Today
09:30
Carlos movió la oportunidad a Negociación

Yesterday
15:20
Email enviado al cliente

Oct 4
11:10
Llamada con el cliente

Oct 2
09:00
Oportunidad creada
```

Cada evento debe guardarse en Supabase.

---

# 8. Actividades

Permitir registrar:

* Llamada
* Email
* Reunión
* WhatsApp
* Nota
* Cotización
* Cambio de etapa

Agregar botón:

**+ Nueva actividad**

Formulario:

```text
Tipo
Descripción
Fecha
Usuario
Resultado
```

---

# 9. Reglas comerciales

Implementar estas reglas:

### Regla 1 — Forecast

```text
forecast = amount × probability
```

### Regla 2 — Inactividad

Si una oportunidad permanece más de **7 días sin actividad**:

* Mostrar alerta roja.
* Marcar oportunidad como "Atención requerida".
* Registrar evento.
* Preparar alerta de email.

### Regla 3 — Cambio de etapa

Cada cambio de etapa debe quedar registrado.

### Regla 4 — Nunca eliminar

Las oportunidades no deben eliminarse físicamente.

Utilizar:

```text
archived = true
```

para archivarlas.

Mantener histórico.

---

# 10. Supabase

Conectar la aplicación a **Supabase**.

Crear el esquema necesario.

Como mínimo crear estas tablas:

### users

```text
id
name
email
role
avatar_url
created_at
```

Roles:

```text
seller
manager
admin
```

### customers

```text
id
name
company
email
phone
industry
created_at
```

### opportunities

```text
id
customer_id
owner_id
title
description
amount
probability
forecast
stage
expected_close_date
last_activity_at
archived
created_at
updated_at
```

### activities

```text
id
opportunity_id
user_id
type
description
activity_date
created_at
```

### opportunity_stage_history

```text
id
opportunity_id
user_id
previous_stage
new_stage
created_at
```

### notifications

```text
id
user_id
opportunity_id
type
message
status
created_at
```

### audit_log

```text
id
user_id
entity_type
entity_id
action
old_value
new_value
created_at
```

---

# 11. Seguridad

Implementar **Supabase Row Level Security (RLS)**.

Reglas:

### Seller

Un vendedor solamente puede visualizar y modificar sus propias oportunidades.

### Manager

Un gerente puede visualizar todas las oportunidades y actividades de su equipo.

### Admin

Puede visualizar y administrar todo.

No confiar solamente en restricciones del frontend.

Las restricciones deben implementarse también mediante Supabase RLS.

---

# 12. Resend

Integrar **Resend** para enviar emails.

El correo de destino para las alertas iniciales será:

**TU_CORREO**

IMPORTANTE:

No hardcodear API keys en el frontend.

Utilizar:

```text
RESEND_API_KEY
```

como variable de entorno / secret.

Crear una Edge Function de Supabase o backend seguro para enviar los emails.

---

# 13. Alertas por email

Enviar email cuando ocurran eventos importantes.

### Cambio de etapa

Ejemplo:

```text
Subject:
Opportunity stage changed — Acme Corporation

Acme Corporation changed from:

Contactado → Cotizado

Amount:
$25,000

Probability:
70%

Changed by:
Carlos

Date:
Oct 6, 2026
```

### Oportunidad sin actividad

Ejemplo:

```text
Subject:
⚠️ Opportunity requires attention

Opportunity:
Acme Corporation

Amount:
$25,000

Stage:
Negociación

Last activity:
9 days ago

Action:
Follow up with customer
```

### Oportunidad ganada

Enviar:

```text
🎉 Opportunity Won

Customer:
Acme Corporation

Amount:
$25,000

Sales representative:
Carlos
```

---

# 14. Email settings

Crear una sección:

**Notification Settings**

Permitir configurar:

* Stage changes
* Inactivity alerts
* Won opportunities
* Daily summary
* Weekly commercial summary

Mostrar claramente si cada alerta está:

`ON / OFF`

---

# 15. Resumen semanal

Crear una función para generar un resumen comercial.

Ejemplo:

```text
Pulso Comercial — Weekly Summary

Pipeline:
$425,000

Forecast:
$287,500

New opportunities:
12

Won:
5

Lost:
2

At risk:
4

Top opportunity:
Acme Corporation — $80,000
```

Enviar mediante Resend.

---

# 16. Datos sintéticos

Crear automáticamente datos sintéticos realistas para poder probar la aplicación.

Crear aproximadamente:

* 8 vendedores
* 30 clientes
* 60 oportunidades
* 150 actividades
* Historial de cambios
* Diferentes probabilidades
* Diferentes fechas
* Algunas oportunidades con más de 7 días sin actividad
* Oportunidades ganadas y perdidas

Usar nombres y empresas ficticias.

Los datos deben estar distribuidos entre:

```text
Nuevo
Contactado
Cotizado
Negociación
Ganado
Perdido
```

Crear suficiente información para que el dashboard se vea real desde el primer momento.

---

# 17. Chat comercial

Agregar un botón flotante:

💬 **Commercial Assistant**

El usuario debe poder preguntar cosas como:

```text
¿Cuánto tenemos en pipeline?

¿Qué oportunidades están en riesgo?

¿Cuáles llevan más de 7 días sin actividad?

¿Cuál es el forecast de este mes?

¿Cuáles son las oportunidades más grandes?

¿Qué oportunidades están en negociación?

¿Cuánto hemos ganado este mes?
```

El chat debe consultar información real de Supabase.

Crear una arquitectura preparada para integrar posteriormente un LLM.

Separar:

```text
Chat UI
    ↓
AI / Chat Service
    ↓
Business Logic
    ↓
Supabase
```

No colocar lógica de negocio directamente dentro del componente visual del chat.

---

# 18. Arquitectura preparada para AI / MCP

Diseñar la aplicación para poder incorporar posteriormente herramientas MCP.

Crear conceptualmente herramientas como:

```text
get_pipeline()
get_opportunities()
get_opportunity()
get_at_risk_opportunities()
get_forecast()
get_sales_by_rep()
get_activity_history()
```

Esto permitirá posteriormente conectar el sistema con Claude, ChatGPT u otros agentes.

---

# 19. Activity Canvas

Además del Kanban, crear una vista denominada:

**Activity Canvas**

Esta vista permitirá visualizar el flujo de actividades y eventos.

Ejemplo:

```text
Lead
 ↓
Contactado
 ↓
Reunión
 ↓
Cotización
 ↓
Negociación
 ↓
Ganado
```

Mostrar visualmente:

* Eventos
* Actividades
* Cambios de etapa
* Alertas
* Usuarios
* Fechas

Debe ser posible seleccionar un evento y ver sus detalles.

---

# 20. Filtros

Agregar filtros:

```text
Vendedor
Etapa
Cliente
Industria
Monto
Probabilidad
Fecha de cierre
Estado
Actividad
```

También agregar:

**Search opportunities**

---

# 21. Dashboard del gerente

Crear una vista especial:

### Manager Dashboard

Mostrar:

```text
Total Pipeline
Forecast
Won
Lost
Conversion Rate
At Risk
```

Agregar gráficos:

* Pipeline por etapa
* Forecast por vendedor
* Ventas ganadas por mes
* Oportunidades creadas
* Actividad por vendedor
* Aging de oportunidades

---

# 22. Vista del vendedor

El vendedor solamente debe ver:

```text
My Pipeline
My Opportunities
My Activities
My Forecast
My Tasks
```

Agregar una sección:

### "What needs my attention?"

Ejemplo:

```text
🔴 3 opportunities without activity
🟡 2 deals closing this week
🟢 4 active opportunities
```

---

# 23. UX

Agregar microinteracciones:

* Drag & drop suave.
* Animaciones ligeras.
* Toast después de guardar.
* Loading skeletons.
* Empty states.
* Confirmación antes de acciones importantes.
* Estados de error claros.
* Optimistic UI para movimientos del Kanban.
* Responsive design.

El usuario debe sentir que está utilizando una aplicación SaaS profesional.

---

# 24. Navegación

Crear sidebar:

```text
🏠 Dashboard

📊 Pipeline

🧩 Activity Canvas

👥 Customers

💼 Opportunities

📅 Activities

📈 Analytics

🤖 Commercial Assistant

🔔 Notifications

⚙️ Settings
```

---

# 25. Página inicial

El dashboard debe abrir mostrando inmediatamente:

```text
Good morning, Carlos 👋

Here's your commercial pulse today.

$425K
Pipeline

$287K
Forecast

12
Opportunities

4
At Risk
```

Debajo:

**My Pipeline**

con el Kanban.

---

# 26. Requisitos técnicos

Utilizar:

* React
* TypeScript
* Tailwind CSS
* shadcn/ui
* Supabase
* Supabase Auth
* Supabase RLS
* Supabase Edge Functions
* Resend
* Drag & Drop library compatible with React
* Recharts para gráficos

Mantener una arquitectura limpia y modular.

Separar:

```text
components
pages
services
hooks
types
lib
supabase
```

No colocar toda la lógica dentro de un único componente.

---

# 27. Environment variables

Preparar:

```env
VITE_SUPABASE_URL=
VITE_SUPABASE_ANON_KEY=

RESEND_API_KEY=

ALERT_EMAIL=TU_CORREO
```

Nunca exponer `RESEND_API_KEY` en el navegador.

---

# 28. Demo inicial

Al finalizar, la aplicación debe funcionar inmediatamente con datos sintéticos.

Crear un usuario demo:

```text
Manager
```

y varios vendedores.

El usuario debe poder:

1. Abrir el dashboard.
2. Ver el pipeline.
3. Arrastrar una oportunidad.
4. Ver cómo cambia de etapa.
5. Ver el cambio persistido en Supabase.
6. Ver el evento en el timeline.
7. Generar una alerta.
8. Ver el email enviado mediante Resend.
9. Consultar información desde el chat.
10. Ver gráficos actualizados automáticamente.

---

# 29. Importante

No construir solamente un prototipo visual.

Quiero una **aplicación funcional end-to-end**, aunque inicialmente sea un MVP.

Priorizar:

**UI → Supabase → Business Logic → Notifications → Chat**

La información mostrada en pantalla debe provenir de Supabase y no estar hardcodeada.

El diseño debe tomar como inspiración la imagen proporcionada, pero mejorarla significativamente en términos de UX, navegación, interacción y visualización de datos.

El resultado debe sentirse como un producto SaaS comercial listo para evolucionar a producción.

---

### Flujo principal esperado

```text
                    PULSO COMERCIAL
                          │
                          ▼
                    ┌───────────┐
                    │ Dashboard │
                    └─────┬─────┘
                          │
             ┌────────────┼────────────┐
             ▼            ▼            ▼
         Pipeline     Analytics       Chat
             │                         │
             ▼                         ▼
        Drag & Drop              AI Assistant
             │                         │
             ▼                         │
          Supabase ◄───────────────────┘
             │
       ┌─────┴──────┐
       ▼            ▼
    History       Alerts
                      │
                      ▼
                   Resend
                      │
                      ▼
             TU_CORREO
```

**Construye primero la estructura funcional completa, conecta Supabase, genera los datos sintéticos y después refina la UI. No dejes botones o funcionalidades principales como simples placeholders.**
