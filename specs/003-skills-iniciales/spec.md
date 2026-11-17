# 003 · Skills iniciales

Estado: aprobada por Hugo el 17/11/2026.

## Qué

Las tres primeras skills comunes del plugin `aie-equipo`, una por cada función que más tiempo cuesta cada semana:

| Skill | Para quién | Función |
| --- | --- | --- |
| `preparar-sprint` | Quien vaya a impartir el sprint | Revisar el sprint, preparar la teórica y el caso práctico y hacer el PDF de enlaces (funciones 7, 8, 10 y 11) |
| `liberar-sprint` | TA | Abrir la PR de release el martes, liberar el miércoles y dejar el campus listo (funciones 14 y 15) |
| `acta-sesion` | TA | Generar el acta de una sesión a partir de su transcripción (función 20) |

## Por qué

Cada uno ya tiene su versión: Soraya, el prompt maestro para preparar sprints y su skill de actas; Hugo, skills personales para el cambio de sprint, el Kahoot y las grabaciones. Si las funciones rotan, las herramientas tienen que ser las mismas para los dos. Si no, cada relevo cambia también la forma de trabajar.

## Alcance

Dentro:
- `preparar-sprint`: parte del prompt maestro v2 de Soraya (`incubadora/soraya/preparar-sprint/`), con sus fases y sus reglas. Sus plantillas pasan a `plantillas/`.
- `liberar-sprint`: parte de la skill personal de Hugo para el cambio de sprint, adaptada a OCT26 (PR el martes, liberación el miércoles hacia las 13:00).
- `acta-sesion`: parte de la skill de actas de Soraya, que ya usa la automatización de grabaciones.
- Cada skill dice al empezar qué necesita (repo, sprint, ordenador conectado) y para si falta algo.

Fuera:
- La automatización de grabaciones, que sigue en el equipo de Hugo.
- Kahoot y subir vídeos: se quedan como skills personales de Hugo hasta que el otro las necesite.

## Criterios de aceptación

- Soraya ha revisado `preparar-sprint` y `acta-sesion` antes de que pasen al plugin, porque salen de su trabajo.
- Hugo ha preparado el S06 con `preparar-sprint` y Soraya el S08.
- El TA de una semana real ha liberado un sprint con `liberar-sprint` sin pasos a mano que no estén en la skill.
- Ninguna skill hace commit, push ni cambios en Trello, Slack o el campus sin confirmación.

## Preguntas abiertas

- ¿Las skills personales de Hugo se copian en el repo tal cual o se reescriben? Hay que leerlas primero.
