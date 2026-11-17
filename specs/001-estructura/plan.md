# 001 · Plan

1. Un `README.md` en cada carpeta de primer nivel que diga qué entra y qué no.
2. Un workflow de GitHub Actions que, en cada PR y en cada push a `main` y `develop`, ejecute `claude plugin validate` sobre el marketplace y sobre cada plugin. La versión de Claude Code va fijada para que el check no cambie solo; se sube a mano de vez en cuando.
3. Plantilla de PR con la spec y dos comprobaciones: versión del plugin y ausencia de secretos.
4. Regla de versionado del plugin en `docs/reglas-git.md`.
5. Comandos de actualización en la guía de inicio.
6. Comprobar con los dos la instalación y si el plugin se puede usar desde la app de chat con el plan Pro.
