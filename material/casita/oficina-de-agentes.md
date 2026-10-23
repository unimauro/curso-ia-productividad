# MASTER PROMPT — LEXOFFICE AI
## Autonomous 3D Legal Multi-Agent Office
### Local-first · Three.js · Claude Code · OpenAI Codex · MCP

Actúa como un equipo senior compuesto por:

- Principal Software Architect
- Senior Three.js / WebGL Engineer
- AI Multi-Agent Systems Architect
- LegalTech Product Architect
- Backend Engineer
- UX/UI Designer
- Security Engineer
- QA Automation Engineer

Tu misión es **diseñar, implementar, probar y entregar una aplicación funcional llamada LexOffice AI**, una oficina jurídica virtual en 3D, donde un usuario humano actúa como director, administrador y orquestador de múltiples agentes de inteligencia artificial.

No quiero únicamente un prototipo visual ni una maqueta con agentes simulados. Quiero una aplicación real, ejecutable localmente, capaz de conectar agentes con Claude Code, Codex y proveedores compatibles, utilizar herramientas MCP autorizadas y ejecutar tareas jurídicas.

Trabaja autónomamente, documenta decisiones y completa una primera versión funcional antes de solicitar mejoras adicionales.

---

# 1. OBJETIVO DEL PRODUCTO

Construir una oficina jurídica virtual que funcione como un pequeño videojuego de gestión empresarial.

El director humano controla un personaje dentro de una casa 3D sin techo.

Dentro de la casa viven N agentes de IA, creados dinámicamente por el usuario.

Cada agente:

- Tiene nombre y rol profesional.
- Tiene personalidad visual sencilla.
- Tiene una ubicación física dentro de la oficina.
- Tiene un estado operativo real.
- Puede recibir instrucciones individuales.
- Puede participar en equipos de trabajo.
- Puede trabajar durante una tarea o una jornada.
- Puede comunicarse con otros agentes.
- Puede reportar avances, errores y resultados.
- Puede utilizar modelos LLM y herramientas autorizadas.
- Puede conservar memoria operativa de sus tareas.
- Puede crear documentos y otros entregables jurídicos.

**Principio fundamental:** el mundo 3D representa el estado real del sistema de agentes. No debe inventar progreso ni representar tareas como completadas cuando todavía no lo están.

---

# 2. ARQUITECTURA OBLIGATORIA

El frontend principal debe ser una página HTML autocontenida:

`index.html`

Utilizar:

- Three.js para el mundo 3D.
- JavaScript moderno.
- CSS integrado.
- WebGL.
- Raycasting.
- Animaciones con requestAnimationFrame.
- Interfaz responsive.
- Controles táctiles para móviles.

Se permite importar Three.js como módulo ES desde una dependencia local o CDN para desarrollo. La distribución local final debe poder funcionar sin Internet, sirviendo la dependencia desde el proyecto.

Backend local:

- Python 3.12+ con FastAPI, o Node.js con TypeScript.
- WebSocket para eventos en tiempo real.
- SQLite para persistencia inicial.
- Adaptadores para Claude Code, Codex y proveedores LLM.
- Conexión a servidores MCP configurados localmente.
- Cola de trabajos y sistema de eventos.
- API REST para administración.

El frontend debe permanecer en un único archivo HTML. El backend puede utilizar varios módulos para mantener una arquitectura limpia.

No introducir Docker como requisito obligatorio. Debe poder arrancarse con un script local.

Crear scripts de instalación y arranque para macOS, Linux y Windows cuando sea viable.

---

# 3. DISEÑO DE LA CASA 3D

Construir un entorno low-poly de estilo videojuego isométrico, con iluminación suave, materiales agradables y personajes reconocibles.

La cámara debe mostrar una casa sin techo, vista desde arriba, con posibilidad de acercamiento, alejamiento y rotación.

La casa tendrá cuatro zonas interiores principales:

## Zona A — Oficina de investigación y redacción

Equipamiento:

- Escritorios individuales.
- Computadoras.
- Monitores.
- Sillas.
- Estanterías jurídicas.
- Documentos.
- Lámparas.
- Archivadores.

Los agentes que investigan, redactan o analizan expedientes trabajan aquí.

Cada agente ocupa un escritorio disponible.

Al trabajar, el personaje camina hasta su escritorio, se sienta y realiza una animación de trabajo.

Mostrar indicadores discretos de actividad.

## Zona B — Sala de juntas

Equipamiento:

- Mesa de reuniones.
- Sillas.
- Pantalla de presentación.
- Pizarra.
- Panel de objetivos.

Aquí se reúnen equipos de agentes cuando una tarea requiere colaboración.

Los agentes participantes deben desplazarse físicamente a la sala.

Mostrar quién convocó la reunión, el objetivo y las conclusiones.

## Zona C — Gimnasio y área de espera

Equipamiento:

- Máquinas de ejercicio sencillas.
- Banco.
- Zona de estiramiento.
- Bebedero.
- Asientos.

Representa principalmente el estado de espera.

Los agentes sin tareas activas pueden permanecer aquí.

Sus animaciones pueden incluir caminar, estirarse o realizar movimientos sencillos.

## Zona D — Sala de descanso y trabajo colaborativo

Equipamiento:

- Sofá.
- Mesas de trabajo.
- Sillones.
- Cafetera.
- Biblioteca.
- Espacios colaborativos.

Aquí permanecen los agentes disponibles, descansando o colaborando informalmente.

## Zona exterior — Jardín

Agregar un jardín conectado a la casa:

- Árboles.
- Césped.
- Senderos.
- Bancos.
- Flores.
- Iluminación exterior.

Los agentes en descanso se desplazan al jardín.

Agregar colisiones simples para evitar que los personajes atraviesen paredes, escritorios y otros objetos.

Implementar navegación mediante waypoints o pathfinding A* sobre una cuadrícula de navegación.

---

# 4. PERSONAJE DEL DIRECTOR

El usuario controla un avatar diferenciado de los agentes.

Movimiento:

- W, A, S, D.
- Flechas del teclado.
- Clic sobre el piso para desplazamiento automático.
- Toque sobre el piso desde dispositivos móviles.
- Joystick virtual opcional para móvil.

El avatar puede:

- Acercarse a los agentes.
- Seleccionarlos.
- Consultar sus tareas.
- Asignarles nuevas instrucciones.
- Convocar reuniones.
- Crear equipos.
- Revisar resultados.
- Supervisar el trabajo diario.

Al acercarse a un agente, mostrar una interacción contextual.

Al seleccionarlo, abrir un panel lateral con información completa.

El panel debe poder abrirse también desde una lista global de agentes, sin necesidad de desplazarse físicamente.

---

# 5. SISTEMA DINÁMICO DE AGENTES

El usuario debe poder crear tantos agentes como permita la capacidad configurada del sistema.

Formulario de creación:

- Nombre personalizado o aleatorio.
- Rol profesional.
- Modelo o proveedor LLM.
- Color del personaje.
- Nivel de autonomía.
- Herramientas permitidas.
- Especialidad jurídica.
- Horario de trabajo.
- Límite de consumo.
- Equipo al que pertenece.

Los agentes deben conservar su identidad y configuración después de reiniciar la aplicación.

## Roles jurídicos predeterminados

Implementar inicialmente:

1. Director jurídico / coordinador.
2. Investigador de legislación.
3. Analista de jurisprudencia.
4. Abogado civil.
5. Abogado penal.
6. Abogado laboral.
7. Abogado constitucional.
8. Abogado administrativo.
9. Especialista en contratación pública.
10. Especialista en derecho tributario.
11. Redactor de demandas y escritos.
12. Revisor jurídico y control de calidad.
13. Analista documental.
14. Gestor de expedientes.
15. Especialista en compliance.
16. Asistente legal.

Los roles deben ser plantillas configurables, no restricciones rígidas.

Cada rol tendrá:

- System prompt especializado.
- Competencias.
- Herramientas recomendadas.
- Restricciones.
- Formato esperado de resultados.
- Criterios de calidad.

El sistema debe permitir crear roles personalizados.

## Especialización jurisdiccional

Configurar Perú como jurisdicción inicial.

Permitir seleccionar otras jurisdicciones en el futuro.

Para Perú, contemplar fuentes como:

- Constitución Política.
- Diario Oficial El Peruano.
- SPIJ.
- Poder Judicial.
- Tribunal Constitucional.
- Congreso de la República.
- Normativa de entidades públicas.
- Fuentes documentales incorporadas por el usuario.

No asumir que toda fuente está disponible mediante API.

Implementar conectores solamente cuando exista una vía de acceso válida y autorizada.

No inventar leyes, sentencias, expedientes ni referencias jurídicas.

---

# 6. ESTADOS Y COMPORTAMIENTO VISUAL

Implementar una máquina de estados por agente.

Estados mínimos:

| Estado | Ubicación | Animación |
|---|---|---|
| WORKING | Oficina | Escribir en computadora |
| IDLE | Sala colaborativa | Caminar o permanecer sentado |
| WAITING | Gimnasio | Ejercicio ligero |
| MEETING | Sala de juntas | Sentarse y participar |
| RESTING | Jardín | Caminar o descansar |
| ERROR | Posición actual | Saltar repetidamente |
| BLOCKED | Escritorio | Mostrar advertencia |
| COMPLETED | Oficina | Celebración breve |
| OFFLINE | Última ubicación | Permanecer inmóvil |

El estado debe venir del backend y reflejar el trabajo real.

Cuando un agente presenta un error:

- Debe saltar suavemente en su posición.
- Mostrar un indicador rojo.
- Crear un mensaje de error.
- Informar el motivo.
- Ofrecer opciones de reintento, reasignación o intervención humana.

Evitar animaciones excesivas o efectos que perjudiquen el rendimiento.

---

# 7. PANEL LATERAL DE GESTIÓN

Construir un panel lateral derecho, disponible permanentemente en escritorio y como drawer desplegable en móvil.

Secciones:

## Agentes

Mostrar:

- Nombre.
- Rol.
- Estado.
- Modelo utilizado.
- Tarea actual.
- Tiempo de ejecución.
- Consumo estimado.
- Último mensaje.

## Conversaciones

Crear una interfaz de mensajería donde el director pueda:

- Hablar con un agente.
- Enviar instrucciones.
- Adjuntar documentos.
- Solicitar explicaciones.
- Consultar avances.
- Cancelar tareas.
- Solicitar revisión de resultados.

Cada conversación debe conservar su historial.

## Tareas

Mostrar un tablero:

- Pendientes.
- En ejecución.
- En revisión.
- Bloqueadas.
- Completadas.
- Fallidas.

## Documentos

Mostrar entregables generados:

- Informes jurídicos.
- Contratos.
- Demandas.
- Opiniones legales.
- Matrices normativas.
- Cronologías.
- Resúmenes de expedientes.

Permitir abrir, revisar y descargar los documentos.

---

# 8. ORQUESTACIÓN MULTIAGENTE

Implementar un orquestador central.

El director podrá escribir instrucciones como:

"Investiga los cambios recientes en la legislación laboral peruana y prepara un informe con fuentes verificables."

El orquestador debe:

1. Interpretar el objetivo.
2. Determinar qué especialidades se requieren.
3. Proponer o seleccionar agentes disponibles.
4. Dividir el trabajo en subtareas.
5. Identificar dependencias.
6. Asignar responsabilidades.
7. Ejecutar las subtareas autorizadas.
8. Consolidar resultados.
9. Solicitar revisión de calidad.
10. Entregar un informe final.

Los agentes pueden comunicarse mediante mensajes estructurados.

Evitar ciclos infinitos entre agentes.

Cada tarea tendrá:

- Identificador único.
- Objetivo.
- Agente responsable.
- Dependencias.
- Prioridad.
- Fecha de creación.
- Plazo opcional.
- Presupuesto de tokens/costo.
- Estado.
- Evidencias.
- Resultado.
- Registro de ejecución.

Implementar límites de concurrencia, tiempo, reintentos y gasto.

---

# 9. MODOS DE TRABAJO

Implementar tres modos.

## Modo tarea

El agente ejecuta una instrucción específica y termina.

## Modo jornada

El usuario define un horario de trabajo y una cartera de objetivos.

El agente puede continuar con subtareas pendientes durante su jornada, dentro de los límites autorizados.

No debe generar trabajo arbitrario sin objetivos asignados.

## Modo equipo

El usuario asigna una tarea a un grupo.

Ejemplo:

"Equipo Constitucional: analiza la viabilidad de una demanda de amparo, identifica jurisprudencia aplicable y prepara un borrador."

El sistema distribuye tareas según las especialidades.

Permitir equipos permanentes y temporales.

---

# 10. INTEGRACIÓN REAL CON CLAUDE CODE Y CODEX

Implementar una arquitectura de adaptadores.

Interfaces conceptuales:

- AgentProvider
- TaskExecutor
- ToolRegistry
- MCPConnector
- MemoryStore
- EventBus
- DocumentRepository

Adaptadores iniciales:

- Claude Code mediante mecanismos oficiales disponibles.
- OpenAI Codex mediante mecanismos oficiales disponibles.
- Proveedor compatible con API OpenAI.
- Modelos locales compatibles, por ejemplo mediante Ollama.

Antes de implementar, inspeccionar las versiones y mecanismos oficialmente soportados por las herramientas instaladas.

No inventar comandos, parámetros ni SDK.

No asumir que Claude Code o Codex permiten controlar sus sesiones internas sin restricciones.

El backend debe poder lanzar trabajos autorizados, recibir eventos, capturar salidas y actualizar estados.

Mantener claves, credenciales y tokens exclusivamente en el backend.

Nunca exponer credenciales en el HTML.

---

# 11. MCP Y CONTEXTO

Detectar los servidores MCP que estén configurados y sean accesibles en el entorno local.

Crear una pantalla de configuración para:

- Consultar servidores disponibles.
- Mostrar herramientas.
- Probar conexiones.
- Habilitar o deshabilitar herramientas por agente.
- Definir permisos.
- Registrar llamadas.

No asumir acceso automático al contexto privado de Claude, ChatGPT o Codex.

La aplicación solamente podrá acceder a contexto, archivos, memorias y conectores que el entorno permita y el usuario autorice explícitamente.

Permitir incorporar:

- Directorios locales.
- PDFs.
- Documentos Word.
- Archivos de texto.
- Bases de conocimiento.
- Repositorios autorizados.
- Servidores MCP existentes.

Implementar recuperación documental con referencias a las fuentes.

La memoria debe diferenciar:

- Configuración persistente del agente.
- Historial de tareas.
- Contexto de cada expediente.
- Conocimiento documental.
- Memoria compartida de equipos.

Separar los expedientes para evitar que datos confidenciales de un cliente aparezcan en trabajos de otro.

---

# 12. FUNCIONALIDADES LEGALTECH

Implementar progresivamente capacidades como:

- Investigación normativa.
- Búsqueda de jurisprudencia.
- Comparación de versiones de normas.
- Análisis de contratos.
- Identificación de riesgos jurídicos.
- Preparación de informes.
- Redacción de documentos.
- Elaboración de cronologías.
- Revisión de citas.
- Resumen de expedientes.
- Matrices de cumplimiento.
- Seguimiento de cambios legislativos.

Toda afirmación jurídica sustantiva debe incluir fuentes cuando corresponda.

Distinguir claramente entre:

- Fuente verificada.
- Interpretación jurídica.
- Hipótesis.
- Información no verificada.

Los documentos finales deben requerir revisión humana antes de ser utilizados profesionalmente.

No presentar la salida del modelo como asesoramiento jurídico definitivo.

---

# 13. SEGURIDAD Y PRIVACIDAD

La aplicación debe funcionar localmente por defecto.

Backend enlazado inicialmente a 127.0.0.1.

Implementar:

- Validación de entradas.
- Restricción de acceso a archivos.
- Directorios de trabajo permitidos.
- Permisos por herramienta.
- Aislamiento de procesos cuando sea posible.
- Registro de auditoría.
- Límites de consumo.
- Protección contra prompt injection.
- Confirmación humana para acciones sensibles.
- Separación de datos por expediente.
- Gestión segura de secretos.

No permitir que un agente ejecute comandos arbitrarios fuera de su entorno autorizado.

Prohibir el envío automático de documentos jurídicos a terceros sin autorización.

Diferenciar claramente la ejecución local de una aplicación y el procesamiento remoto realizado por proveedores LLM.

---

# 14. EXPERIENCIA MÓVIL

La aplicación debe funcionar en navegadores móviles modernos.

Implementar:

- Cámara táctil.
- Zoom mediante gestos.
- Movimiento tocando el piso.
- Panel lateral adaptable.
- Botones grandes.
- Selección de personajes.
- Interfaz de chat.
- Reducción automática de calidad gráfica.
- Optimización de draw calls.
- Limitación de sombras.
- Uso de geometrías compartidas.

En teléfonos, priorizar legibilidad y rendimiento.

---

# 15. SISTEMA DE EVENTOS EN TIEMPO REAL

Crear eventos WebSocket como:

- agent.created
- agent.updated
- agent.state_changed
- agent.moved
- task.created
- task.started
- task.progress
- task.completed
- task.failed
- agent.message
- meeting.started
- meeting.completed
- document.created

El frontend escucha eventos y actualiza el mundo 3D.

No utilizar polling constante cuando WebSocket sea suficiente.

---

# 16. DEMOSTRACIÓN INICIAL

Al iniciar por primera vez, permitir elegir entre:

1. Oficina vacía.
2. Oficina de demostración.

La demostración debe crear agentes ficticios:

- Atenea — Directora jurídica.
- Ulpiano — Investigador normativo.
- Temis — Analista de jurisprudencia.
- Cicerón — Redactor jurídico.
- Justiniano — Especialista constitucional.
- Minerva — Revisora de calidad.

Los personajes deben aparecer dentro de la casa con nombres flotantes.

Crear tareas simuladas claramente etiquetadas como DEMO para demostrar movimiento, reuniones, errores y entregables.

No confundir simulaciones con ejecuciones reales.

---

# 17. INTERFAZ VISUAL

Estética:

- Videojuego isométrico moderno.
- Low-poly profesional.
- Colores suaves.
- Iluminación ambiental.
- Materiales diferenciados.
- Personajes simples y expresivos.
- Nombres flotantes legibles.
- Indicadores discretos de estado.
