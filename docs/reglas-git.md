# Reglas de git y PR

Decididas por Hugo el 16/11/2026. Valen para este repo y, salvo donde se indica, para todos los repos del bootcamp.

## Ramas de este repo

- `main`: lo que los dos tenemos instalado y damos por bueno.
- `develop`: integración.
- Ramas cortas con prefijo personal, que nacen de `develop` y se borran al mergear: `hugo/003-mapa-recursos`, `soraya/004-skill-actas`. Cuando el trabajo responde a una spec, el nombre lleva su número.

Nota: en git no pueden existir a la vez una rama `hugo` y ramas `hugo/algo`. Por eso no hay rama personal fija; el prefijo hace ese papel. A partir del prefijo, cada uno se organiza como quiera.

## Reglas

1. Nunca una PR a `main` que no venga de `develop`.
2. Toda PR que no sea de `develop` a `main` puede mergearla su autor.
3. Las PR de `develop` a `main` piden revisión en GitHub a la otra persona, sea LI o TA esa semana.
4. Una PR a `main` puede mergearse sin revisión si falta menos de una hora para que haga falta. Se deja un comentario en la PR con el motivo.
5. Claude puede hacer commit, push y abrir PR en ramas de trabajo. Nunca mergea a `main`.
6. Si una rama con un uso ya registrado va a sustituirse por otra con otro nombre, antes se avisa y se pide confirmación a una persona.
7. Commits y PR pequeños.

## Versión del plugin

- Cada PR de `develop` a `main` que cambie un plugin sube su `version` en `plugin.json`: el último número para arreglos, el del medio para skills nuevas y el primero para cambios que obliguen a reinstalar.
- Cada PR pasa un check automático que valida el marketplace y los plugins. Si sale en rojo, no se mergea.

Las normas de estilo y formato no forman parte de estas reglas. Su estandarización queda como tema futuro (spec 006).

## Guardas

Comprobaciones automáticas que hacen cumplir estas reglas.

| Guarda | Dónde | Qué hace |
| --- | --- | --- |
| PR a `main` solo desde `develop` | GitHub Action en `equipo-montes` | Pone la PR en rojo si viene de otra rama |
| Sin `.env` ni claves | GitHub Action en `equipo-montes` | Pone la PR en rojo si entra un `.env` o algo con forma de clave. Nunca muestra el valor |
| Plugin válido | GitHub Action en `equipo-montes` | Valida el marketplace y los plugins |
| `.env` | Hook del plugin `aie-equipo`, en el Claude de cada uno | Impide leer o editar un `.env` |
| Push a `main` o `develop`, push forzado y PR a `main` desde otra rama | Hook del plugin `aie-equipo` | Pide confirmación antes de hacerlo |
| Protección de rama de `main` | Ajustes de GitHub, los pone una persona | Exige PR y check en verde |

Las guardas de los repos del bootcamp se añaden con su propia PR en cada repo.

## Ramas con uso registrado en otros repos

| Repo | Rama | Uso |
| --- | --- | --- |
| `material_bootcamp_AI_Engineering` | `hugo` | Rama de trabajo de Hugo; base de sus PR |
| `material_bootcamp_AI_Engineering` | `*_soraya` | Ramas de trabajo de Soraya |
| Repos de alumnos | `feature_copy_from_material` | Entrada del contenido que viene de material |
| Repos de alumnos | `develop-actas` | Actas de sesión, con PR a `develop` |
| Todos | `develop` → `main` | Release, con PR titulada «release: …» |

En un repo de alumnos nunca hay `README_profes` ni `_SOLUTION` del sprint activo.
