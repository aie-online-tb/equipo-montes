# Revisión de Claude en GitHub

Dos workflows usan Claude en este repo:

| Workflow | Cuándo corre | Qué hace |
| --- | --- | --- |
| [revision-claude.yml](../.github/workflows/revision-claude.yml) | Al abrir o actualizar una PR a `main` (no en borrador) | Revisa el diff contra las reglas del repo y deja comentarios en línea y un resumen con veredicto |
| [claude.yml](../.github/workflows/claude.yml) | Cuando alguien escribe `@claude` en una PR o un issue | Responde a la pregunta o revisa lo que se le pida |

Los dos solo leen y comentan. Nunca aprueban, hacen push ni mergean: la revisión y el merge de `develop` a `main` siguen siendo de la otra persona ([reglas-git.md](../docs/reglas-git.md)).

Mientras falte el secreto, los dos terminan en verde sin hacer nada.

## Activarla (una vez, la hace Hugo)

1. **Instalar la app de Claude en GitHub.** En [github.com/apps/claude](https://github.com/apps/claude), instálala en la organización `aie-online-tb` y elige solo el repo `equipo-montes`. Hace falta ser owner de la organización; si no lo eres, pídeselo a quien lo sea.
2. **Generar el token.** En una terminal con Claude Code: `claude setup-token`. Abre el navegador, inicias sesión con tu cuenta de Claude y te da un token. Cópialo y no lo pegues en ningún otro sitio.
3. **Guardarlo como secreto del repo.** En GitHub: `equipo-montes` → Settings → Secrets and variables → Actions → New repository secret. Nombre: `CLAUDE_CODE_OAUTH_TOKEN`. Valor: el token.
4. **Probar.** Abre o actualiza la PR de `develop` a `main`. En la pestaña Checks debe aparecer «Revisión de Claude» y, al terminar, un comentario suyo en la PR.

Atajo: el comando `/install-github-app` de Claude Code hace los pasos 1 a 3 guiados. Al final abre una PR con sus propios workflows: ciérrala sin mergear, porque los de este repo ya están.

## Coste y límites

- Cada revisión gasta cuota del plan de Claude de quien generó el token, como una sesión de Claude Code. Si esa persona se queda sin cuota, la revisión falla en ese momento.
- En un repo privado, los minutos de GitHub Actions cuentan contra el cupo mensual de la organización.
- El token caduca. Anota la fecha en que lo generas y repite los pasos 2 y 3 cuando haga falta.
- Ninguna clave ni token entra en el repo: solo en los secretos de GitHub.

## Cambiar lo que revisa

Las instrucciones de la revisión están en el `prompt` de [revision-claude.yml](../.github/workflows/revision-claude.yml). Se cambian por PR, como cualquier otra cosa del repo.
