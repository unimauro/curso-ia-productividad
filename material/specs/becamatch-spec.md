# SPEC · BecaMatch: el "Tinder" de las becas

Versión 1.0 · Proyecto de práctica del curso AI Productivity Engineering (eIA)

## 1. Objetivo

Ayudar a estudiantes y profesionales a encontrar becas que encajan con su perfil, deslizando tarjetas: derecha "me interesa", izquierda "no es para mí". La app guarda las becas elegidas y avisa antes de que venzan.

## 2. Usuarios

- **Postulante:** crea su perfil, desliza becas, guarda las que le interesan y recibe recordatorios.
- **Administrador:** carga y verifica las becas.

## 3. Historias de usuario

1. Como postulante, completo mi perfil en menos de 2 minutos: nivel (pregrado, maestría, doctorado, curso), área de estudio, países de interés, idiomas y nivel, promedio y año de egreso.
2. Como postulante, veo una tarjeta por beca con nombre, entidad, país, cobertura, fecha límite y un puntaje de compatibilidad.
3. Como postulante, deslizo a la derecha para guardar y a la izquierda para descartar. En computadora uso botones.
4. Como postulante, veo "Mis becas" ordenadas por fecha límite, con cuántos días faltan.
5. Como postulante, recibo un correo 7 días antes de cada fecha límite de mis becas guardadas.
6. Como postulante, le pido al asistente de IA que me explique los requisitos de una beca y me arme una lista de documentos.
7. Como administrador, cargo becas con su enlace oficial y las marco como verificadas.

## 4. Pantallas

Inicio · Registro y perfil · Mazo de tarjetas · Detalle de beca · Mis becas · Asistente · Administración

## 5. Datos

| Tabla | Campos |
|---|---|
| perfiles | usuario, nivel, area, paises, idiomas, promedio, egreso, consentimiento, creado |
| becas | id, nombre, entidad, pais, nivel, areas, idioma_requerido, promedio_minimo, cobertura, fecha_limite, enlace_oficial, verificada, fuente |
| decisiones | usuario, beca, decision (me_interesa o descartada), fecha |
| recordatorios | usuario, beca, fecha_envio, enviado |

## 6. Reglas

- **Compatibilidad de 0 a 100:** nivel coincide 30, área coincide 25, idioma cumplido 15, promedio cumplido 20, país de interés 10. El mazo muestra primero las de 50 o más.
- Una beca descartada no vuelve a aparecer, salvo que el usuario la recupere desde "Descartadas".
- Solo se muestran becas con fecha límite futura y marcadas como verificadas.
- El asistente responde solo con los datos de la beca y su enlace oficial. Si no sabe algo, lo dice y envía al enlace oficial.

## 7. Integraciones

- Base de datos y usuarios: Lovable Cloud (Supabase).
- Correos: Resend.
- IA: la IA de Lovable para el asistente.
- MCP: el administrador consulta la base en Claude con el MCP de Supabase en solo lectura.

## 8. Fuera de alcance en la versión 1

Postular desde la app · pagos · chat entre usuarios · recomendaciones con aprendizaje automático.

## 9. Seguridad y datos personales

- Casilla de consentimiento obligatoria (Ley 29733).
- Cada usuario ve solo su perfil y sus decisiones.
- Solo mayores de 18 años, o con autorización de sus padres.
- Nunca inventar becas, montos ni fechas: cada beca necesita enlace oficial.

## 10. Criterios de aceptación

- Un usuario nuevo crea su perfil y ve al menos 5 tarjetas ordenadas por compatibilidad.
- Deslizar guarda la decisión y la tarjeta no reaparece.
- "Mis becas" muestra los días que faltan y llega un correo de prueba.
- El asistente no inventa un requisito que no está en la beca.

## 11. Fases

1. Mazo de tarjetas con los datos de ejemplo.
2. Perfil y puntaje de compatibilidad.
3. Mis becas y recordatorios por correo.
4. Asistente de IA y panel de administración.

## 12. Reglas para cambiar la app

Antes de pedir un cambio, actualiza este SPEC y pide a la IA: "Revisa el SPEC y dime qué partes de la app afecta este cambio antes de hacerlo".

Datos de ejemplo (ficticios): https://unimauro.github.io/curso-ia-productividad/material/becas-ejemplo.json
