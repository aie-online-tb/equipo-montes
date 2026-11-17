# 001 · Estructura del repo y del plugin

Estado: borrador del 17/11/2026, pendiente de aprobar.

## Qué

Dejar cerrada la forma del repo: qué carpeta guarda qué, cómo se instala y actualiza el plugin común y cómo se comprueba que todo sigue siendo válido después de cada cambio.

## Por qué

Todo lo demás (skills, rutinas, plantillas) se va a apoyar en esta estructura. Si cambia a mitad de camino, hay que mover cosas y reinstalar. Además, los dos vamos a tocar el repo con Claude: necesitamos que un error en el plugin se vea en la PR y no al instalarlo.

## Alcance

Dentro:
- Una línea en el README de cada carpeta que diga qué entra en ella y qué no.
- El plugin `aie-equipo` como único plugin común al empezar. Uno nuevo solo se crea si un grupo de skills no tiene sentido para los dos.
- Versionado del plugin: se sube la versión en `plugin.json` en cada PR de `develop` a `main` que cambie el plugin.
- Una comprobación automática en cada PR que valide el marketplace y el plugin.
- Instrucciones para instalar y actualizar en la guía de inicio, probadas por los dos.

Fuera:
- El contenido de las skills (spec 003).
- Los conectores (spec 002).

## Criterios de aceptación

- Hugo y Soraya han instalado el plugin desde el marketplace del repo y ven la skill `normas-aie` en Claude Code.
- Una PR que rompa `marketplace.json` o `plugin.json` muestra un check en rojo.
- Ninguna carpeta del repo queda sin explicar.
- Se ha comprobado si el plugin se puede usar desde la app de chat con el plan Pro, y la guía dice el resultado.

## Preguntas abiertas

- ¿La comprobación automática se hace con GitHub Actions? Depende de que la organización tenga Actions activado para repos privados.
