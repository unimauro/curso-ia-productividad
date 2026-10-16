# PROMPT MAESTRO — CASAS PARA GATOS
## CRM + KANBAN + AGENTE IA + COTIZACIONES + GOOGLE CALENDAR + GOOGLE MEET

### 1. Objetivo

Evoluciona la aplicación existente de Casas para Gatos para convertirla en una plataforma comercial inteligente que centralice:

- CRM con Kanban.
- Chatbot web y agente de WhatsApp.
- Catálogo y base de conocimiento compartidos.
- Generación y envío de cotizaciones mediante Resend.
- Gestión de clientes y oportunidades comerciales.
- Seguimiento de leads y tareas.
- Medios de pago configurados.
- Registro de compras y postventa.
- Solicitud de reseñas.
- Agenda comercial integrada con Google Calendar y Google Meet.
- Dashboard administrativo y auditoría de acciones.

**Antes de modificar el código, inspecciona el proyecto existente**, incluyendo Supabase, tablas, componentes, Edge Functions, autenticación, Resend, chatbot e integraciones configuradas.

Reutiliza lo que ya funciona. No reconstruyas la aplicación desde cero, no dupliques servicios ni crees integraciones paralelas. Implementa los cambios de manera incremental y conserva las funcionalidades existentes.

### 2. Atención comercial unificada

El chatbot web y el agente de WhatsApp deben utilizar una misma lógica comercial y una fuente de datos compartida.

Ambos deben acceder a:

- Catálogo vigente y precios.
- Preguntas frecuentes y condiciones comerciales.
- Clientes y leads.
- Historial de conversaciones.
- Cotizaciones y partidas.
- Estado de ventas y pagos.
- Actividades y seguimientos.
- Agenda de reuniones.
- Configuración comercial autorizada.

Cuando un cliente utilice más de un canal, relaciona las conversaciones con el mismo registro solo cuando su identidad pueda verificarse con suficiente confianza.

El agente debe hablar en español peruano, con tono cálido, breve y natural. Debe responder con datos respaldados por el catálogo y preguntar cuando falte información.

No inventes precios, descuentos, productos, stock, pagos, disponibilidad de reuniones, reseñas ni resultados de operaciones.

### 3. Catálogo y reglas comerciales

Utiliza el catálogo, las preguntas frecuentes y la base de datos existentes como fuente de verdad.

Productos:

- Casa Premium XL.
- Casa Comfort.
- Refugio Cozy.
- Cama Deluxe.
- Torre para Gatos.

Consulta los precios y las características reales desde la fuente autorizada.

Las condiciones comerciales conocidas incluyen delivery para Lima Metropolitana y Callao, coordinación para provincias, pagos mediante Yape, Plin y transferencia bancaria, ausencia de descuentos registrados, ausencia de tienda física y garantía por defectos de fabricación.

Antes de utilizar estos datos en producción, valida que sigan coincidiendo con el catálogo y la configuración actual.

Los datos bancarios, enlaces de pago y condiciones especiales deben configurarse y verificarse por un administrador.

### 4. CRM con Kanban

Implementa un tablero Kanban que permita gestionar cada lead desde su primera consulta hasta la postventa.

Cada tarjeta debe mostrar:

- Nombre y datos de contacto disponibles.
- Canal de origen y campaña, si existen.
- Producto de interés.
- Presupuesto indicado por el cliente, si existe.
- Etapa comercial.
- Última interacción.
- Cotización asociada e importe, cuando existan.
- Próxima acción recomendada.
- Fecha de seguimiento.
- Responsable.
- Próxima reunión comercial, si existe.

Etapas del embudo:

1. Nuevo lead.
2. Contactado.
3. Calificado.
4. Cotización pendiente.
5. Cotización enviada.
6. Seguimiento.
7. Pendiente de pago.
8. Ganado.
9. Perdido.
10. Postventa.

Permite mover tarjetas mediante drag and drop y guardar cada cambio en Supabase, registrando la fecha, el usuario y la etapa anterior y nueva.

Incluye filtros por fecha, canal, producto, etapa y responsable.

No marques una venta como ganada solo porque el cliente manifieste interés. Exige confirmación válida de pago o el criterio comercial aprobado por el administrador.

### 5. IA para recomendar y ejecutar la próxima acción

La IA debe analizar el contexto y recomendar la siguiente acción comercial.

Ejemplos:

- Lead nuevo: responder y conocer su necesidad.
- Producto identificado: preparar cotización.
- Cotización pendiente: completar información.
- Cotización enviada: programar seguimiento.
- Cliente interesado en comprar: mostrar los medios de pago autorizados.
- Compra confirmada: iniciar postventa.
- Cliente con una oportunidad comercial grande: ofrecer una reunión.
- Cliente con una reunión confirmada: mostrar fecha y enlace.
- Cliente que solicita ayuda humana: derivar a un asesor.

Cada recomendación debe incluir acción, motivo, fecha cuando corresponda y un botón para ejecutarla.

La IA puede ejecutar acciones autorizadas desde la conversación. El administrador debe poder revisar y ejecutar acciones desde el CRM.

Registra las acciones realizadas, sus resultados y los errores. Evita mensajes repetitivos y operaciones duplicadas.

### 6. Chatbot web y agente de WhatsApp

El agente debe poder:

- Responder preguntas sobre productos.
- Recomendar productos existentes.
- Calificar leads.
- Registrar o actualizar clientes.
- Consultar el historial de conversaciones.
- Generar cotizaciones.
- Solicitar confirmación para enviar cotizaciones.
- Enviar cotizaciones por Resend.
- Compartir medios de pago configurados.
- Programar seguimientos.
- Ofrecer reuniones comerciales.
- Consultar y gestionar citas.
- Registrar compras y activar postventa.
- Derivar conversaciones a una persona.

Crea o reutiliza herramientas de backend equivalentes a:

- `get_product_info`
- `create_or_update_lead`
- `get_customer_history`
- `create_quote`
- `send_quote_email`
- `get_payment_methods`
- `update_lead_stage`
- `schedule_follow_up`
- `record_payment_confirmation`
- `request_product_review`
- `check_calendar_availability`
- `create_calendar_meeting`
- `reschedule_calendar_meeting`
- `cancel_calendar_meeting`
- `handoff_to_human`

Adapta los nombres a la arquitectura existente. No dupliques servicios que ya realizan estas funciones.

### 7. Cotizaciones desde la conversación mediante Resend

**Prioridad: el cliente debe poder solicitar, revisar, confirmar y recibir su cotización sin salir del chatbot web o WhatsApp.**

Ya existe una integración de Resend. Inspecciona y reutiliza su implementación, Edge Functions, plantillas y variables de entorno. No crees una segunda integración.

Flujo obligatorio:

1. El cliente solicita una cotización.
2. El agente identifica productos y cantidades.
3. Si falta el correo electrónico, lo solicita en la conversación.
4. El backend consulta los precios vigentes y calcula los importes.
5. El agente presenta un resumen de productos, cantidades, precios, delivery e importe total cuando pueda determinarse.
6. El agente solicita confirmación para enviar al correo indicado.
7. Tras la confirmación, ejecuta el servicio existente de Resend.
8. El backend registra el resultado.
9. El agente informa el resultado en el mismo canal de conversación.
10. El CRM y el Kanban reflejan el estado real de la cotización.

Ejemplo:

Cliente: “Me interesa la Casa Premium XL. ¿Me puedes cotizar?”

Agente: “¡Claro! Te ayudo con tu cotización. ¿A qué correo te la envío?”

Cliente: “tu-correo@ejemplo.com”.

Agente: “Perfecto. Preparé tu cotización. ¿Confirmas que la envíe a tu-correo@ejemplo.com?”

Cliente: “Sí, envíala”.

El backend envía la cotización mediante Resend.

Si el proveedor acepta el envío, el agente confirma:

“¡Listo! Tu cotización fue enviada a tu correo. Revisa también tu carpeta de spam por si acaso. ¿Quieres que te ayude con el siguiente paso?”

Si falla, informa del problema y permite reintentar o contactar con un asesor.

Reglas técnicas:

- Calcular precios e importes en el backend.
- No exponer la API key de Resend en el frontend.
- Validar los datos antes de enviar.
- Solicitar confirmación del cliente.
- Evitar envíos duplicados mediante idempotencia o un control equivalente.
- Registrar destinatario, cotización, canal, fecha y resultado.
- Cambiar el estado a “Cotización enviada” únicamente cuando Resend acepte el mensaje.
- No afirmar que llegó a la bandeja de entrada sin evidencia de entrega.
- Mantener la cotización como borrador si el cliente no confirma.
- Reutilizar el mismo servicio desde web y WhatsApp.

### 8. Medios de pago

Cuando el cliente esté listo para comprar, el agente debe poder compartir los medios de pago configurados.

Los medios contemplados son Yape, Plin y transferencia bancaria.

Los números, titulares, cuentas, enlaces e instrucciones deben obtenerse de una configuración validada por el administrador.

Si falta información, el agente debe ofrecer la intervención de un asesor. Nunca inventes cuentas ni confirmes pagos sin evidencia.

### 9. Seguimiento comercial y tareas

Implementa tareas y recordatorios configurables para:

- Leads sin respuesta.
- Cotizaciones pendientes de envío.
- Cotizaciones enviadas que requieren seguimiento.
- Operaciones pendientes de pago.
- Reuniones próximas.
- Reuniones que requieren reprogramación.
- Actividades de postventa.

Permite definir plazos, responsables y canales autorizados.

No envíes mensajes automáticos sin una regla configurada. Evita duplicados y cancela o actualiza los recordatorios cuando cambie el estado de una oportunidad.

### 10. Gestor de citas con Google Calendar y Google Meet

Implementa una sección llamada **Agenda comercial**, integrada con el CRM, el Kanban y los agentes de conversación.

Su objetivo es facilitar llamadas de asesoría para clientes que necesiten una propuesta comercial, una compra de volumen o ayuda personalizada.

#### 10.1 Detección de oportunidades

La IA puede ofrecer una reunión cuando detecte:

- Interés en comprar varias casas.
- Solicitudes de cotización de volumen.
- Consultas de negocios o establecimientos comerciales.
- Necesidad de asesoría personalizada.
- Solicitud explícita de hablar con un asesor.

Las cantidades mínimas para compras de volumen deben ser configurables. No inventes condiciones mayoristas ni prometas descuentos no aprobados.

Ejemplo:

“¡Claro! Si estás pensando en comprar varias casas para gatos, podemos coordinar una llamada para conocer tus necesidades y preparar una propuesta. ¿Te gustaría agendar una reunión con nuestro asesor?”

#### 10.2 Conexión con Google Calendar

Utiliza OAuth y las APIs oficiales de Google Calendar.

Antes de implementar, verifica si existe alguna integración previa. Reutilízala cuando sea posible.

La configuración debe permitir:

- Autorizar la cuenta de Google.
- Seleccionar el calendario comercial.
- Consultar disponibilidad real.
- Configurar días y horarios de atención.
- Definir duración y anticipación mínima.
- Configurar la zona horaria `America/Lima`.
- Definir días no laborables.
- Consultar reuniones próximas.
- Cancelar y reprogramar citas.

Las credenciales y tokens deben gestionarse de forma segura en el backend. No los expongas al frontend.

Si Google no está conectado, muestra los pasos pendientes y mantén funcionando el resto de la plataforma.

#### 10.3 Agendamiento conversacional

El flujo debe ser:

1. El agente ofrece una reunión cuando resulte útil.
2. Solicita nombre, correo y motivo si faltan.
3. Pregunta por la fecha u horario preferido.
4. Consulta disponibilidad real.
5. Presenta opciones disponibles.
6. El cliente selecciona un horario.
7. El agente muestra fecha, hora, duración y motivo.
8. Solicita confirmación.
9. Tras confirmar, vuelve a validar la disponibilidad.
10. Crea el evento en Google Calendar.
11. Solicita la creación de una videoconferencia mediante el mecanismo oficial de Google Calendar.
12. Guarda el evento y el enlace real de Meet en Supabase.
13. Vincula la reunión con el lead, cliente y oportunidad.
14. Confirma el resultado en la conversación original.

Nunca inventes horarios ni enlaces de Meet. No confirmes una cita antes de que Google acepte la operación.

Si el horario deja de estar disponible, vuelve a consultar el calendario y presenta alternativas.

#### 10.4 Invitaciones y confirmaciones

Utiliza Google Calendar para invitar a los asistentes cuando los permisos y la configuración lo permitan.

Reutiliza Resend para mensajes comerciales complementarios, si se necesitan, evitando enviar dos invitaciones equivalentes.

La confirmación debe incluir:

- Nombre de la reunión.
- Fecha y hora.
- Zona horaria.
- Duración.
- Motivo.
- Enlace real de Meet.
- Instrucciones de cancelación o reprogramación.

Registra el resultado real del envío. Si falla, informa del error y permite reintentar.

#### 10.5 CRM y Kanban

La tarjeta del lead debe poder mostrar:

- Fecha de la próxima reunión.
- Estado de la cita.
- Motivo.
- Responsable comercial.
- Acceso a los detalles de la reunión.
- Próxima acción recomendada.

Los estados de la reunión serán:

- Pendiente de confirmación.
- Confirmada.
- Completada.
- Cancelada.
- Reprogramación solicitada.

Agendar una reunión no significa que la venta esté ganada.

Después de la llamada, el asesor podrá registrar el resultado, las necesidades del cliente, la cotización pendiente y el siguiente paso.

#### 10.6 Administración de la agenda

Crea una vista que permita consultar:

- Reuniones del día.
- Próximas reuniones.
- Reuniones por asesor.
- Citas pendientes de confirmación.
- Reuniones canceladas.
- Solicitudes de reprogramación.

Permite filtrar por fecha, cliente, canal y estado. Desde una cita se debe poder abrir el historial del cliente y sus cotizaciones.

#### 10.7 Reprogramación y cancelación

Permite solicitar cambios desde el chatbot web o WhatsApp.

Verifica que la solicitud esté autorizada. Consulta disponibilidad real, presenta opciones y solicita confirmación antes de modificar el evento.

Actualiza Google Calendar y Supabase, notifica a los participantes y conserva el historial de la cita original.

#### 10.8 Recordatorios

Permite configurar recordatorios, por ejemplo, 24 horas y 1 hora antes de la reunión.

Solo deben enviarse para citas confirmadas, con canales autorizados. Registra los envíos para evitar duplicados y actualiza los recordatorios si la cita cambia o se cancela.

#### 10.9 Herramientas del agente

Reutiliza o implementa funciones seguras equivalentes a:

- `check_calendar_availability`
- `get_available_meeting_slots`
- `create_calendar_meeting`
- `get_meeting_details`
- `reschedule_calendar_meeting`
- `cancel_calendar_meeting`
- `record_meeting_outcome`
- `send_meeting_confirmation`

Todas deben ejecutarse en el backend, validar permisos y registrar resultados.

#### 10.10 Modo demo

Permite simular citas sin crear eventos reales ni enviar invitaciones. Identifica claramente las operaciones como DEMO.

No presentes una reunión simulada como una cita confirmada.

### 11. Compras y postventa

Registra las compras confirmadas y relaciónalas con el cliente, la cotización y los productos.

La confirmación debe proceder de una fuente autorizada o de una acción administrativa verificable.

Después de una compra, habilita el flujo de postventa.

#### Solicitud de reseñas

Permite configurar el plazo y el canal de solicitud.

Ejemplo:

“¡Hola! Esperamos que tu michi esté disfrutando su nuevo espacio. ¿Nos compartirías tu opinión sobre el producto? Tu experiencia nos ayuda a mejorar.”

Registra compra, fecha, canal, estado del envío, respuesta y enlace a la reseña si existe.

No inventes reseñas ni atribuyas opiniones ficticias a clientes reales. No publiques reseñas sin autorización.

### 12. Dashboard administrativo

Incluye:

- Resumen comercial.
- Kanban de leads.
- Clientes.
- Conversaciones web y WhatsApp.
- Cotizaciones.
- Ventas y pagos.
- Seguimientos pendientes.
- Agenda comercial.
- Postventa y reseñas.
- Historial de actividades.
- Configuración de integraciones.

Las métricas deben calcularse a partir de datos reales. Identifica claramente los datos de demostración.

### 13. Base de datos y seguridad

Inspecciona primero el esquema de Supabase.

Reutiliza, cuando corresponda, las tablas existentes:

- `customers`
- `quote_requests`
- `products`
- `quotes`
- `quote_items`
- `email_messages`
- `activity_logs`

Añade únicamente las entidades o campos que falten para gestionar etapas comerciales, conversaciones, tareas, compras, reuniones, pagos y reseñas.

Aplica autenticación, políticas RLS, validación en backend y registros de auditoría.

No expongas claves secretas ni permitas que la IA modifique arbitrariamente precios, confirme pagos o falsifique resultados.

Aplica idempotencia para envíos, creación de reuniones y otras operaciones sensibles.

### 14. Datos de prueba

Crea o conserva un cliente ficticio de demostración:

- Nombre: Mauro Demo.
- Correo: `tu-correo@ejemplo.com`.
- Canal: chatbot web.
- Producto de interés: Casa Premium XL.
- Estado inicial: Nuevo lead.

Identifica todos los datos como DEMO. No envíes correos, WhatsApp ni invitaciones reales sin autorización.

Permite simular el flujo:

Nuevo lead → calificación → cotización → envío simulado → pago simulado → agenda simulada → postventa → solicitud de reseña simulada.

No conviertas una compra, pago, cita o reseña simulados en datos reales.

### 15. Integraciones externas

**Resend:** reutiliza la integración existente para enviar cotizaciones y mensajes complementarios.

**WhatsApp:** inspecciona el proveedor configurado. Si existe, reutilízalo. Si no, prepara el adaptador y documenta los requisitos pendientes. No simules una conexión real.

**Google Calendar y Meet:** conecta mediante OAuth y APIs oficiales. Si faltan permisos o credenciales, muestra qué configuración necesita el administrador.

El chatbot web y las demás funciones deben seguir operativos aunque una integración externa esté pendiente.

### 16. Criterios de aceptación

La implementación debe permitir comprobar que:

1. Los leads se registran con su canal de origen.
2. El Kanban muestra etapas y próximas acciones.
3. La IA recomienda productos del catálogo vigente.
4. Los importes de cotización se calculan en el backend.
5. El cliente puede revisar y confirmar una cotización desde la conversación.
6. Resend envía la cotización y su resultado queda registrado.
7. El agente informa el resultado en el canal original.
8. Los medios de pago proceden de la configuración autorizada.
9. Las conversaciones web y WhatsApp comparten la misma lógica.
10. Una compra confirmada activa el flujo de postventa.
11. Las reseñas no se inventan ni publican sin autorización.
12. La IA puede identificar oportunidades apropiadas para una llamada.
13. Google Calendar devuelve disponibilidad real.
14. El cliente puede confirmar una cita desde la conversación.
15. Se crea un evento real y se obtiene el enlace real de Meet.
16. La cita aparece en la agenda y en el Kanban.
17. Se pueden cancelar y reprogramar citas.
18. Las invitaciones y recordatorios no se duplican.
19. Los errores de las integraciones quedan registrados.
20. Los datos de demo nunca se confunden con operaciones reales.
21. Las funcionalidades anteriores siguen operativas.

### 17. Plan de implementación

Primero inspecciona el proyecto y presenta un diagnóstico breve que indique:

- Funcionalidades existentes.
- Componentes y servicios que se reutilizarán.
- Cambios requeridos en Supabase.
- Estado de Resend.
- Estado del proveedor de WhatsApp.
- Estado de Google Calendar y Google Meet.
- Credenciales, permisos o configuraciones pendientes.

Después implementa incrementalmente, priorizando:

1. CRM y Kanban.
2. Cotizaciones conversacionales mediante Resend.
3. Agenda comercial con Google Calendar y Meet.
4. Seguimientos y postventa.
5. Integración real de WhatsApp, si está pendiente.

Ejecuta las pruebas y entrega un resumen de lo implementado, las pruebas superadas y los bloqueos que requieran configuración externa.

**Prioridad absoluta:** permitir que el agente acompañe al cliente desde su consulta inicial hasta la cotización, el seguimiento y, cuando corresponda, una reunión comercial, registrando cada acción en el CRM sin duplicar servicios ni simular resultados reales.
