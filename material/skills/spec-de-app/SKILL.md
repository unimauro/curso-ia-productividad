---
name: spec-de-app
description: Escribe y mantiene el SPEC (especificación) de una app antes de construirla con Lovable, v0, Claude Code u otra herramienta, y revisa el impacto de cada cambio. Úsala cuando el usuario quiera crear una app, agregar una función, cambiar una regla o pida "hazme el spec".
---

# SPEC de una app

Un buen SPEC evita que la IA rehaga o rompa partes de la app en cada cambio. Siempre trabajas así: primero el SPEC, después el prompt.

## 1. Entrevista corta

Si falta información, pregunta solo lo esencial: objetivo, quién la usa, qué datos guarda, qué no debe hacer.

## 2. Estructura del SPEC

1. Objetivo en 2 líneas.
2. Usuarios y roles.
3. Historias de usuario numeradas: "Como X, quiero Y".
4. Pantallas.
5. Datos: tablas y campos.
6. Reglas de negocio con números (puntajes, plazos, cálculos).
7. Integraciones: base de datos, correo, IA, API, MCP.
8. Fuera de alcance de la versión 1.
9. Seguridad y datos personales (en Perú, Ley 29733; consentimiento).
10. Criterios de aceptación comprobables.
11. Fases de construcción: 3 o 4, cada una usable por sí sola.
12. Reglas para cambiar la app.

## 3. Del SPEC al prompt

- Entrega un prompt por fase, no uno gigante.
- Cada prompt empieza con: "Sigue el SPEC del proyecto. Construye solo la fase N".
- Recomienda pegar el SPEC en el conocimiento del proyecto de Lovable.

## 4. Cuando el usuario pida un cambio

1. Actualiza el SPEC y sube la versión (1.0 → 1.1).
2. Lista qué pantallas, tablas y reglas afecta.
3. Avisa si rompe un criterio de aceptación.
4. Solo entonces escribe el prompt del cambio.

## Reglas

- Nunca inventes datos reales: si faltan, usa datos de ejemplo marcados como ficticios.
- Prefiere reglas medibles a frases vagas.
