# Equipo Montes

Repo de organización y herramientas de Soraya Malpica y Hugo Menéndez, equipo docente del bootcamp de AI Engineering de The Bridge. Alcance: intake OCT26 en adelante. Es la memoria compartida del equipo: lo que deba durar y valer para los dos se escribe aquí.

## Qué no contiene
- Material del bootcamp: vive en `aie-online-tb/material_bootcamp_AI_Engineering` y en los repos de alumnos.
- Ninguna clave, token ni `.env`. No leas ni muestres ficheros `.env`.

## Cómo nos organizamos
- Dos roles que rotan por módulo: **LI** imparte las Live Reviews de la semana; **TA** acompaña todas las clases y lleva la operación de la semana.
- Hay funciones que siguen a la semana (LI o TA de esa semana) y funciones que siguen al sprint (quien lo imparte).
- Antes de responder sobre quién hace qué o cuándo, consulta `docs/roles-y-funciones.md`, `docs/semana-tipo.md`, `docs/li-por-modulo.md`, `docs/mapa-recursos.md` y `docs/guia-inicio.md`.
- En OCT26 el sprint se libera el JUEVES (PR el miércoles por la noche). Es la regla vigente (ver `docs/decisiones.md`) y la semana tipo va de jueves a miércoles.
- Notion ya no se usa. Trello es la fuente de verdad de las tareas.

## Git y PR (detalle en `docs/reglas-git.md`)
- Ramas cortas con prefijo personal (`hugo/003-…`, `soraya/004-…`) desde `develop`; se borran al mergear.
- Nunca una PR a `main` que no venga de `develop`. Claude no mergea a `main`.
- Una PR de `develop` a `main` necesita Approve explícito de la otra persona.
- Una PR por tarea. Prefijos `release:`, `feat:`, `fix:` y `chore:` (si dudas, `feat:`).
- Si una rama con uso ya registrado va a sustituirse, avisa y pide confirmación.

## Reglas de trabajo
- Trello: lectura libre. Cambios solo si una persona lo pide; para mover, archivar o borrar, pide OK antes. No cambies Slack ni el calendario sin que una persona lo apruebe.
- Simetría Soraya/Hugo: si cambias entorno, cuentas, permisos o conectores, o fijas un criterio que solo vive en el chat, comprueba con `git grep` si queda registrado aquí. Si no, dilo en ese mensaje y propón dónde (`setup/` o `docs/decisiones.md`), sin valores secretos.
- Cada pieza nueva nace de una spec en `specs/`. Lee `specs/README.md` antes de proponer una.
- Los repos de alumnos y de material no llevan `CLAUDE.md` (no se pueden subir a GitHub): sus reglas de ramas y contenido viven aquí, en `docs/reglas-git.md`.
- `workouts_AIE_permanente` no se actualiza. Si un doc o skill dice lo contrario, corrígelo por PR.

## Redacción
- Español; términos técnicos en inglés cuando sea lo natural. Masculino genérico.
- De cara al alumno, sigue la skill `normas-aie` del plugin `aie-equipo`.
