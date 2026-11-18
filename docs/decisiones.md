# Registro de decisiones

Una línea por decisión, la más reciente arriba. Si una decisión cambia, no se borra: se añade la nueva y se marca la anterior como sustituida.

| Fecha | Decisión | Quién |
| --- | --- | --- |
| 18/11/2026 | El mensaje de apertura de sprint se envía los jueves a primera hora, con una automatización de Soraya, en vez del miércoles al liberar. Pendiente: Soraya comparte la automatización en este repo y avisa a Hugo (tarjeta de Trello). Hasta entonces, `rutinas/maestra.md` y `rutinas/diaria.md` siguen con el borrador del miércoles y habrá que ajustarlos | Hugo |
| 18/11/2026 | Se retiran de la cuenta de Hugo las rutinas de prueba (Diaria y Maestra de ensayo y Seguimientos pospuestos, que usaba Notion). Siguen activas Maestra, Diaria y PRs. Soraya no tiene que replicar nada, solo montar las suyas con `setup/prompt-inicial.md` | Hugo |
| 17/11/2026 | Tutorías: las atiende quien imparte el módulo correspondiente | Hugo y Soraya |
| 17/11/2026 | Este repo lo mantienen los dos | Hugo y Soraya |
| 17/11/2026 | Calendario del S08: apertura el 14/12, práctica el 15/12 y sesión de dudas de S06, S07 y S08 el 17/12, para que el S07 no se quede solo con teórica por el puente. Las fechas exactas se confirman en el calendario | Hugo y Soraya |
| 17/11/2026 | Revisar el Deck de N+1 el viernes anterior, en vez del martes, y avisar a María de cualquier cambio | Hugo y Soraya |
| 17/11/2026 | Una PR por tarea (apertura, soluciones, slides, taller, Team Challenge), no una sola release semanal | Hugo y Soraya |
| 17/11/2026 | Prefijos de commits y PR: `release:` solo para abrir un sprint, `feat:` para añadir soluciones, slides o talleres, `fix:` para correcciones. `chore:` queda por estandarizar | Hugo y Soraya |
| 17/11/2026 | Una PR de `develop` a `main` no se mergea sin la aprobación explícita de la otra persona, salvo que falte menos de una hora | Hugo y Soraya |
| 17/11/2026 | Se deja de usar Notion. Trello, el calendario de Google, la hoja de seguimiento y este repo son las fuentes. Slack se mantiene conectado al espacio del claustro | Hugo y Soraya |
| 16/11/2026 | Ramas: `main`, `develop` y ramas cortas con prefijo personal (`hugo/…`, `soraya/…`), sin rama personal fija | Hugo |
| 16/11/2026 | Se deroga la regla de formato y marcas en los ficheros. La estandarización de estilo queda como tema futuro | Hugo |
| 16/11/2026 | Se crea este repo, nuevo y privado, separado del de material, como punto común de trabajo con Claude | Hugo |
| 16/11/2026 | El repo se construye con SDD y con las estructuras de Claude Code: `CLAUDE.md`, `.claude/rules/` y skills como plugin | Hugo |
| 16/11/2026 | Reglas de PR: solo `develop` → `main` pide revisión; el resto puede mergearlo su autor. Deroga la revisión cruzada de PR a `develop` | Hugo |
| 16/11/2026 | Claude puede hacer commit, push y PR en ramas de trabajo y nunca mergea a `main` | Hugo |
| 16/11/2026 | La PR de release la abre el TA el martes a partir de las 19:00 y se libera el miércoles hacia las 13:00 | Hugo |
| 16/11/2026 | Semana tipo de miércoles a martes; weekly los lunes a las 16:00; mensaje de cierre los viernes | Hugo |
| 16/11/2026 | Las 29 funciones se asignan a rol (LI o TA), y unas siguen a la semana y otras al sprint | Hugo |
| 16/11/2026 | Tres capas: Personal, Equipo Montes y Claustro | Hugo |
| 16/11/2026 | Alcance: OCT26 en adelante. MAY26 queda fuera | Hugo |
| 16/11/2026 | Los dos seguimos con Claude Pro personal; no hay proyecto de Claude compartido | Hugo |
| 16/11/2026 | No se genera más contenido troncal. Alejandro Reyes sale del proyecto | Hugo |
| 16/11/2026 | Kahoots: se reciclan; solo se crea uno nuevo si el LI lo necesita | Hugo |
| 16/11/2026 | La automatización de grabaciones se queda en el equipo de Hugo; el TA comprueba la subida | Hugo |
| 16/11/2026 | La hoja de ruta de estandarización del repo material queda obsoleta y se absorbe aquí a menor escala | Hugo |
| 16/11/2026 | Se abandona la tarea programada Diaria; si hace falta se diseñará otra | Hugo |
| 16/11/2026 | En OCT26 el sprint se libera el miércoles, para que el alumno lo vea antes de la teórica del jueves | Hugo |

## Abiertas

- LI de M06 MLOps.
- Proteger `main`: Hugo mira qué permite el plan gratuito de GitHub en repos privados; si no, Soraya busca el script que ya usó con alumnos.
- Reflejar el cambio del S08 en el calendario OCT26 y en `li-por-modulo.md`: hoy el calendario sigue con la teórica del S08 el 10/12.
- Tutorías: formato y horarios.
- Estandarizar `chore:` y el resto de prefijos (Claude propone).
- Estandarización de estilo y formato (spec 006).
