# AI Productivity Engineering · Curso de IA y productividad

Sitio del curso (eIA): encuestas anónimas, material de las tareas y entrega de trabajos.

**Sitio:** https://unimauro.github.io/curso-ia-productividad/

| Página | Para qué |
|---|---|
| `index.html` | Portada con enlaces de la sesión y fecha límite |
| `encuesta.html` | Encuesta inicial anónima (un voto por navegador) |
| `cierre.html` | Encuesta de cierre anónima |
| `entregar.html` | Entrega de tareas: correo, nombre y texto, archivo (hasta 10 MB) o enlace |
| `docente.html` | Panel del docente con clave: resultados en tablas y entregas con descarga |
| `material/` | Archivos de las tareas |

## Cómo funciona

- Páginas estáticas en GitHub Pages. Preguntas en `preguntas.js`.
- API mínima en `api/server.py` (Python estándar y SQLite) en el VPS, detrás de `https://ai.tunky.net/encuesta-api/`.
- **Entregas:** se aceptan hasta la fecha límite de cada tarea, definida en la variable `PLAZOS` del servidor (UTC). Tarea 1: jueves 1 de octubre de 2026, 6:59 p. m. de Lima. Se guardan todas las versiones y el panel muestra la última de cada correo.
- **Límites:** el correo no se verifica, así que alguien podría entregar con un correo ajeno. Sin inicio de sesión, el voto único de las encuestas depende del navegador.
- **Privacidad:** los resultados, las entregas y los archivos solo se leen con la clave de administrador. La clave vive en el `.env` del servidor y en `.admin-key` local, que no se sube al repo.
