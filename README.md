# Equipo Montes

Punto común de trabajo de Soraya y Hugo para el bootcamp de AI Engineering de The Bridge (intake OCT26 en adelante).

Este repo es la **memoria compartida** del equipo: aquí está escrito cómo nos organizamos, qué reglas seguimos y qué herramientas de Claude usamos los dos. Si algo debe durar y valer para ambos, se escribe aquí y no en un chat.

## Empieza por aquí

1. Lee la [guía de inicio](docs/guia-inicio.md): 10 minutos y sabes cómo funciona todo.
2. Clona el repo y ábrelo con Claude Code.
3. Instala las skills comunes (una sola vez):

```bash
claude plugin marketplace add aie-online-tb/equipo-montes
claude plugin install aie-equipo@equipo-montes
```

## Qué hay en cada carpeta

| Carpeta | Qué contiene |
| --- | --- |
| `docs/` | Roles, semana tipo, quién es LI en cada módulo, reglas de git, mapa de recursos y decisiones |
| `specs/` | Una carpeta por pieza del sistema, con su spec, su plan y sus tareas (SDD) |
| `plugins/aie-equipo/` | Las skills comunes, instalables como plugin de Claude Code |
| `plantillas/` | Mensajes de Slack, slides y PDF que reutilizamos |
| `rutinas/` | El texto de cada tarea programada, para activarla en la cuenta de quien toque |
| `incubadora/` | Lo personal que cada uno propone subir al equipo |
| `.claude/rules/` | Reglas que Claude carga solo cuando toca ciertos ficheros |

## Cómo se contribuye

- Rama corta desde `develop`, con tu prefijo: `hugo/003-mapa-recursos`, `soraya/004-skill-actas`.
- PR a `develop`: puedes mergearla tú.
- PR de `develop` a `main`: pide revisión en GitHub a la otra persona.

El detalle está en [docs/reglas-git.md](docs/reglas-git.md).
