# SPEC · Pulso Comercial: seguimiento de ventas

Versión 1.0 · Proyecto de práctica del curso AI Productivity Engineering (eIA)

## 1. Objetivo

Que cada vendedor sepa qué hacer hoy y que el gerente vea el avance contra la meta, sin hojas de cálculo sueltas.

## 2. Usuarios

- **Vendedor:** registra oportunidades y actividades, y ve sus tareas del día.
- **Gerente:** ve el embudo de todo el equipo, las metas y el pronóstico.

## 3. Historias de usuario

1. Como vendedor, registro una oportunidad en menos de 1 minuto: cliente, monto estimado, etapa, probabilidad, próxima acción y fecha.
2. Como vendedor, veo un tablero por etapas (Nuevo, Contactado, Cotizado, Negociación, Ganado, Perdido) y muevo tarjetas arrastrando.
3. Como vendedor, veo "Mi día": las próximas acciones de hoy y las oportunidades sin contacto hace más de 7 días.
4. Como vendedor, le pregunto al asistente "¿qué debo hacer hoy?" y me responde con mis oportunidades.
5. Como gerente, veo ventas ganadas contra la meta del mes por vendedor y el pronóstico.
6. Como gerente, recibo un correo cada lunes con el resumen de la semana.
7. Los leads de la app de la sesión 3 entran como oportunidades en etapa "Nuevo".

## 4. Pantallas

Inicio de sesión · Mi día · Tablero de oportunidades · Detalle de oportunidad · Clientes · Panel del gerente · Asistente

## 5. Datos

| Tabla | Campos |
|---|---|
| vendedores | usuario, nombre, region, meta_mensual, rol (vendedor o gerente) |
| clientes | id, negocio, tipo, distrito, telefono, correo, consentimiento |
| oportunidades | id, cliente, vendedor, monto, etapa, probabilidad, proxima_accion, fecha_proxima_accion, origen, creada, cerrada |
| actividades | oportunidad, tipo (llamada, WhatsApp, visita, correo), nota, fecha |

## 6. Reglas

- **Pronóstico** = suma de monto × probabilidad de las oportunidades abiertas.
- **Alerta** si una oportunidad abierta no tiene actividad en 7 días.
- Al pasar a Ganado o Perdido, se registra la fecha de cierre y el motivo.
- Un vendedor ve solo sus oportunidades; el gerente ve todas.

## 7. Integraciones

- Base de datos y usuarios: Lovable Cloud (Supabase), la misma de la app de la sesión 3.
- Ventas históricas: tu API de la sesión 2, /api/resumen.
- Correos: Resend.
- MCP: el gerente consulta en Claude con el MCP de Supabase en solo lectura: "¿quién tiene más oportunidades sin contacto?".

## 8. Fuera de alcance en la versión 1

Facturación · inventario · comisiones · app móvil nativa.

## 9. Seguridad

- Permisos por fila: cada vendedor solo ve lo suyo.
- Los datos de clientes requieren consentimiento.
- Nunca borrar oportunidades: se archivan.

## 10. Criterios de aceptación

- Un vendedor crea una oportunidad y la mueve de etapa en el tablero.
- "Mi día" muestra las alertas de más de 7 días sin contacto.
- El gerente ve el avance contra la meta y el pronóstico, y coinciden con la suma manual.
- Un lead nuevo de la app de la sesión 3 aparece como oportunidad.

## 11. Fases

1. Tablero de oportunidades con datos de ejemplo.
2. Usuarios, roles y permisos.
3. Mi día, alertas y asistente.
4. Panel del gerente, correo semanal y conexión con la API.

## 12. Reglas para cambiar la app

Antes de pedir un cambio, actualiza este SPEC y pide a la IA: "Revisa el SPEC y dime qué partes de la app afecta este cambio antes de hacerlo".
