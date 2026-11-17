---
name: liberar-sprint
description: Libera un sprint del bootcamp AI Engineering de The Bridge en el intake OCT26. El martes prepara la release (soluciones del sprint que cierra, sprint nuevo sin soluciones y workouts) y el miércoles comprueba la liberación y deja el campus listo. Úsala cuando el TA diga «liberar el sprint», «preparar la release», «cambio de sprint», «abre el siguiente sprint» o «deja el campus listo».
---

# liberar-sprint

Funciones 14 (liberar el sprint) y 15 (campus) del TA. Basada en la skill personal de Hugo `cambio-sprint`, escrita para MAY26, y adaptada a OCT26.

## Cuándo

| Día | Qué | Quién |
| --- | --- | --- |
| Martes, desde las 19:00 | Pasos 0 a 3: dejar la release preparada y abrir la PR mientras el LI da la práctica | TA |
| Miércoles, hacia las 13:00 | Paso 4 y 5: mergear la release, mostrar la sección del campus y comprobar enlaces | TA |

N es el sprint que cierra y N+1 el que se libera. Si entre los dos hay un Project Break, para y pregunta qué se libera.

### Copias por partes

En OCT26 el contenido no entra en una sola release semanal. Cada pieza es una copia aparte:

| Pieza | Cuándo suele entrar |
| --- | --- |
| Sprint N+1 sin soluciones | Martes o miércoles, antes de liberar |
| Soluciones del sprint anterior | Después de su práctica del martes |
| Slides del jueves y otros añadidos (talleres) | Cuando estén listos |

Pregunta qué pieza toca y haz solo los pasos de esa pieza: el 1 para soluciones, el 2 y el 3 para el sprint nuevo, y una copia directa para slides y añadidos.

Cada copia son dos PRs seguidas: `feature/copy_from_material` → `develop` y `develop` → `main`. El título de la PR a `main` empieza por «release:» y dice qué entra, por ejemplo «release: Sprint 05» o «release: soluciones Sprint 04». Las mergea el TA.

## Repos y ramas

| Repo | Rama de trabajo | Destino |
| --- | --- | --- |
| `material_bootcamp_AI_Engineering` | Solo lectura | Fuente |
| `bootcamp_AI_Engineering_10_26` | `feature/copy_from_material` | PR a `develop`, luego PR de `develop` a `main` |
| `workouts_AIE_permanente` | `main` | Los workouts del campus |

Pregunta en qué carpeta tiene la persona los repos y comprueba que están al día antes de copiar nada.

## Pasos

Si se pide `--dry-run`, haz los pasos de comprobación y enseña el plan completo sin copiar ni cambiar nada.

### Paso 0 · Comprobar el sprint N+1 en material

- Localiza el módulo y la carpeta del sprint N+1. Desde el S05 la estructura es `<Modulo>/Sprint_XX/{01_Teoria/NN_Bloque/, 02_Workout/NN_Bloque/, Practica_live_review/, README.md, assets/}`.
- Si falta `01_Teoria/`, `02_Workout/` o el `README.md`, para y avisa.
- Las carpetas que terminan en « 2» son duplicados de Finder: no se copian nunca y se listan en Incidencias.

### Paso 1 · Soluciones del sprint N

En `bootcamp_AI_Engineering_10_26`, rama `feature/copy_from_material`: copia desde material todos los `*_SOLUTION*` del sprint N, también los de `Practica_live_review/`, que no estén ya. Déjalos en stage.

### Paso 2 · Sprint N+1 sin soluciones

En la misma rama, copia el sprint N+1 con la misma ruta de módulo que en material, sin `*_SOLUTION*`, sin `README_profes.md` y sin duplicados « 2». Déjalo en stage.

### Paso 3 · Workouts

En `workouts_AIE_permanente`, comprueba si está `Sprint_XX/02_Workout/` del sprint N+1. Si falta, cópialo desde material, con `assets/` si los notebooks lo usan. Aquí sí pueden ir los `_SOLUTION`. Déjalo en stage.

Al terminar los pasos 1 a 3, enseña qué hay en stage en cada repo y **espera el OK** antes de hacer commit, push o abrir PR. Con el OK, el orden es:
1. PR de `feature/copy_from_material` a `develop`.
2. PR «release: …» de `develop` a `main`. Si es el sprint nuevo, se deja abierta hasta la hora de liberar del miércoles.

### Paso 4 · Miércoles: liberar

- La PR a `main` la mergea el TA, nunca Claude. Comprueba después que el sprint N+1 está en `main` y que no hay `_SOLUTION` de N+1 ni `README_profes.md`.
- Campus: en la sección del sprint N+1, comprueba que cada «Fundamentos técnicos y ejemplos» apunta a `blob/main/<Modulo>/Sprint_XX/01_Teoria/NN_Bloque/README.md`, o a la carpeta si el bloque no tiene README, igual que el sprint anterior. El curso de OCT26 está en `docs/mapa-recursos.md` del repo `equipo-montes`.
- La sección se muestra solo cuando la persona lo confirme.

### Paso 5 · Informe

1. Sprints N y N+1 detectados.
2. Soluciones añadidas.
3. Sprint N+1 copiado.
4. Workouts: completos o qué se copió.
5. Campus: recursos revisados y URL finales.
6. Qué ha quedado en stage o en PR en cada repo.
7. Incidencias y duplicados « 2».
8. Ambigüedades, con la pregunta para la persona.

Después, el mensaje de apertura del sprint lo escribe el TA con las plantillas de mensajes (spec 005).

## Reglas

- Nunca una PR a `main` que no venga de `develop`.
- Nunca `*_SOLUTION*` del sprint nuevo ni `README_profes.md` en el repo de alumnos.
- No se cambia nada en el campus sin confirmación.
- Ante cualquier caso que estas reglas no cubran, para y pregunta.

## Pendiente

- El id del curso de OCT26 en el campus y la parte de workouts en adminonline (LTI). Hasta tenerlos, el Paso 4 solo revisa enlaces.
