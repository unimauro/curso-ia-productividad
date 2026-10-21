# SKY WARRIORS: EVOLUTION — Videojuego web 2D, 2.5D y 3D

Actúa como un equipo senior de desarrollo de videojuegos formado por un Game Director, Game Designer, Graphics Engineer, Gameplay Programmer, Sound Designer, UI/UX Designer y QA Engineer.

Tu objetivo es diseñar, implementar y entregar un videojuego de combate aéreo completamente funcional para navegadores modernos, con una arquitectura escalable y gráficos atractivos.

**No construyas solamente una demostración visual. Debes desarrollar un videojuego realmente jugable.**

## 1. Concepto general

Nombre: Sky Warriors: Evolution.

Género: Arcade Shooter / Aerial Combat.

Inspiración: 1942, Raiden, Sky Force y Ace Combat, sin copiar recursos protegidos.

Modos de juego:
- 2D: combate aéreo clásico con desplazamiento vertical.
- 2.5D: perspectiva isométrica, profundidad y efectos visuales.
- 3D: aviones tridimensionales, cámara dinámica y escenarios inmersivos.

El jugador podrá seleccionar el modo desde el menú principal. Diseña la arquitectura para compartir las reglas de combate entre los tres modos.

## 2. Stack tecnológico

Utiliza:
- TypeScript y Vite.
- Phaser para el motor de juego 2D.
- Three.js para el renderizado 3D.
- React para menús, configuración y paneles.
- Zustand para estado global.
- Web Audio API o Howler.js para efectos de sonido.
- IndexedDB o localStorage para guardar progresos.
- Vitest y Playwright para pruebas.
- GitHub Actions para integración y despliegue.
- GitHub Pages para publicar el videojuego.

Prioriza rendimiento, modularidad y compatibilidad con Chrome, Edge, Firefox y Safari.

## 3. Controles de teclado

| Tecla | Acción |
|---|---|
| W / ↑ | Avanzar |
| S / ↓ | Retroceder |
| A / ← | Mover a la izquierda |
| D / → | Mover a la derecha |
| Espacio | Disparo principal |
| J | Misiles |
| K | Arma especial |
| Shift | Turbo |
| Q / E | Rotación en modo 3D |
| C | Cambiar cámara |
| P / Esc | Pausa |
| M | Activar o silenciar sonido |

Permite personalizar los controles y guardar la configuración.

## 4. Mecánicas de juego

- Vidas, barra de energía y escudo temporal tras recibir daño.
- Puntaje, multiplicador por combos y récord guardado localmente.
- Enemigos con patrones distintos: cazas rápidos, bombarderos resistentes, torretas y enjambres.
- Un jefe al final de cada nivel, con fases y puntos débiles.
- Mejoras que caen de los enemigos: disparo doble, misiles, escudo, vida extra y bomba especial.
- Dificultad progresiva por nivel y tres niveles de dificultad: fácil, normal y difícil.
- Al menos 3 niveles con escenarios distintos: costa, desierto y ciudad nocturna.

## 5. Gráficos, sonido e interfaz

- Gráficos generados por código o recursos propios con licencia libre; nada copiado de juegos existentes.
- Explosiones, partículas, destellos y vibración de cámara al recibir daño.
- Música y efectos de sonido con volumen ajustable.
- Menú principal, selección de modo, pausa, opciones, pantalla de fin de partida y tabla de récords.
- Indicadores en pantalla: vidas, energía, puntaje, arma activa y nivel.
- Funciona en celular con controles táctiles: joystick virtual y botones de disparo.

## 6. Calidad y pruebas

- Pruebas unitarias con Vitest para colisiones, puntaje y daño.
- Una prueba de Playwright que abra el juego, inicie una partida y compruebe que el puntaje sube.
- 60 cuadros por segundo en una computadora común; usa pools de objetos para balas y enemigos.
- Sin errores en la consola del navegador.

## 7. Entrega por fases

**Fase 1 (obligatoria en esta tarea):** menú principal y modo 2D completamente jugable, con al menos 1 nivel, enemigos, jefe, mejoras, puntaje, sonido, pausa y fin de partida. Publicado en GitHub Pages con un flujo de GitHub Actions.

**Fase 2:** modo 2.5D isométrico usando las mismas reglas de combate.

**Fase 3:** modo 3D con Three.js, cámara dinámica y rotación con Q y E.

## 8. Reglas para el agente

- Trabaja en una rama y abre un pull request; no subas cambios directo a la rama principal.
- El README debe explicar cómo jugar, cómo correrlo en local (`npm install` y `npm run dev`) y la estructura del proyecto.
- Corre las pruebas y el build antes de abrir el pull request.
- Resume en español lo que hiciste, lo que falta y cómo probarlo.
