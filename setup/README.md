# Puesta en marcha

Todo lo que hay que hacer después de clonar el repo para dejar el sistema funcionando. Se hace una vez por persona y lleva unos 20 minutos.

Si algo de esta carpeta no funciona como dice, se corrige aquí por PR: es la única fuente de los pasos.

## Antes de empezar

- Acceso al repo `aie-online-tb/equipo-montes` en GitHub.
- Claude Code instalado (`claude --version`), `git` y `python3`.

## Pasos

| Paso | Qué | Cómo | Quién |
| --- | --- | --- | --- |
| 1 | Clonar el repo | `git clone https://github.com/aie-online-tb/equipo-montes.git` junto a los demás repos del bootcamp | Cada uno |
| 2 | Instalar el plugin `aie-equipo` (skills y guardas) | `bash setup/instalar.sh` | Cada uno |
| 3 | Comprobar la instalación | `bash setup/comprobar.sh` | Cada uno |
| 4 | Activar los conectores | En claude.ai, Ajustes → Conectores: los de la tabla de [mapa-recursos.md](../docs/mapa-recursos.md#conectores) | Cada uno |
| 5 | Comprobar los conectores | Abre Claude Code en la carpeta del repo y pega [prompts/comprobar-conectores.md](prompts/comprobar-conectores.md) | Cada uno |
| 6 | Activar las rutinas | Sigue [prompts/activar-rutinas.md](prompts/activar-rutinas.md) | Cada uno su diaria; la maestra, solo Hugo |
| 7 | Primera prueba | En Claude Code: «¿quién libera el sprint esta semana y cuándo?» | Cada uno |
| 8 | Activar la revisión de Claude en GitHub | Sigue [revision-claude.md](revision-claude.md) | Solo Hugo, una vez |

Los pasos 2 y 3 se pueden repetir sin miedo: si algo ya está hecho, lo dejan como está.

## Qué rama usar

- `instalar.sh` instala el plugin desde tu copia local. Antes, haz `git checkout main && git pull`: así tienes lo que los dos damos por bueno.
- Las rutinas leen sus instrucciones de `main`. Un cambio en `rutinas/` no les llega hasta la siguiente release de `develop` a `main`.

## Actualizar

Cuando haya una versión nueva del plugin:

```bash
git pull
bash setup/instalar.sh
```

Reinicia Claude Code para que cargue la versión nueva.
