> Fase 1 del prompt de Pulso Comercial para Lovable: solo Kanban con Supabase, roles y datos demo. Aporte de un participante del curso · AI Productivity Engineering, eIA.

Quiero construir un MVP funcional llamado "Pulso Comercial".

IMPORTANTE:
Prioriza funcionalidad sobre cantidad de pantallas.
No construyas funcionalidades futuras todavía.
No agregues Canvas, Chat, Analytics avanzado ni configuraciones complejas en esta fase.

OBJETIVO:
Crear un dashboard comercial tipo Kanban conectado a Supabase para gestionar oportunidades.

STACK:
- React + TypeScript
- Tailwind
- shadcn/ui
- Supabase
- Drag & Drop

1. SUPABASE

Usa Supabase como única fuente de datos.

Crear estas tablas:

users:
- id
- name
- email
- role

customers:
- id
- name
- company
- email

opportunities:
- id
- customer_id
- owner_id
- title
- amount
- probability
- stage
- expected_close_date
- last_activity_at
- archived
- created_at
- updated_at

activities:
- id
- opportunity_id
- user_id
- type
- description
- created_at

stage_history:
- id
- opportunity_id
- user_id
- previous_stage
- new_stage
- created_at

2. ROLES

Crear dos roles:

manager
seller

Seller:
- solamente puede ver sus oportunidades.
- solamente puede modificar sus oportunidades.

Manager:
- puede ver todas las oportunidades.

Usar Supabase RLS.

3. DATOS DEMO

Generar datos sintéticos:

- 1 manager: Carlos Pérez
- 8 sellers
- 30 customers
- 60 opportunities
- aproximadamente 100 activities

Distribuir oportunidades entre:

Nuevo
Contactado
Cotizado
Negociación
Ganado
Perdido

4. DASHBOARD

Crear una única pantalla principal inicialmente.

Header:

"Pulso Comercial"

Mostrar KPIs:

- Pipeline
- Forecast
- Ganado
- En riesgo

Forecast:

amount × probability

5. KANBAN

Crear un Kanban horizontal con:

Nuevo
Contactado
Cotizado
Negociación
Ganado

Cada oportunidad debe mostrar:

- cliente
- monto
- vendedor
- probability
- expected close date
- indicador de actividad

Usar cards modernas.

6. DRAG & DROP

Implementar drag & drop real.

Cuando una oportunidad cambie de columna:

- actualizar stage en Supabase
- crear registro en stage_history
- actualizar updated_at
- actualizar la UI inmediatamente
- mostrar toast de confirmación

No hacer solamente un cambio visual.

7. INACTIVIDAD

Calcular días desde last_activity_at.

Más de 7 días:
mostrar indicador rojo "Sin actividad"

Entre 4 y 7 días:
mostrar indicador amarillo "Atención"

Menos de 4 días:
mostrar indicador verde "Activo"

8. DETALLE

Al hacer click en una oportunidad abrir un drawer lateral.

Mostrar:

- cliente
- monto
- probability
- forecast
- vendedor
- etapa
- fecha de cierre
- última actividad
- timeline de activities
- historial de cambios de etapa

9. UI

Usar un diseño SaaS profesional inspirado en la imagen que adjunto (si no adjunto una, propón un diseño SaaS moderno).

Colores principales:

Navy
Blue
Green

Cards redondeadas.
Sombras suaves.
Mucho espacio visual.
Responsive.

La pantalla debe verse como un producto comercial real, no como un CRUD genérico.

10. REGLA IMPORTANTE

NO implementar todavía:

- Resend
- emails
- Activity Canvas
- AI Chat
- Analytics avanzado
- Settings
- Notifications
- Integraciones externas

Primero quiero que el MVP anterior funcione completamente con Supabase.

Al terminar verifica que:

1. Supabase funciona.
2. Los datos aparecen.
3. El Kanban funciona.
4. Drag & Drop actualiza Supabase.
5. Stage history se registra.
6. Los permisos seller/manager funcionan.
7. El drawer de oportunidad funciona.

No dejes funcionalidades principales como placeholders.
