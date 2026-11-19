---
name: liberar-sprint
description: Libera un sprint del bootcamp AI Engineering de The Bridge en el intake OCT26. Antes de copiar nada comprueba que el sprint nuevo está revisado con preparar-sprint; el miércoles por la noche prepara la release (soluciones del sprint que cierra y sprint nuevo sin soluciones) y el jueves a primera hora comprueba la liberación y deja el campus listo. Úsala cuando el TA diga «liberar el sprint», «preparar la release», «cambio de sprint», «abre el siguiente sprint» o «deja el campus listo».
---

# liberar-sprint

Funciones 14 (liberar el sprint) y 15 (campus) del TA. Basada en la skill personal de Hugo `cambio-sprint`, escrita para MAY26, y adaptada a OCT26.

## Cuándo

| Día | Qué | Quién |
| --- | --- | --- |
| Miércoles, al terminar la clase de las 19:00 | Puerta de revisión y pasos 0 a 2: dejar la release preparada y abrir la PR | TA |
| Jueves, a primera hora | Paso 3 y 4: mergear la release, mostrar la sección del campus y comprobar enlaces | TA |

N es el sprint que cierra y N+1 el que se libera. Si entre los dos hay un Project Break, para y pregunta qué se libera.

### Copias por partes

En OCT26 el contenido no entra en una sola release semanal. Cada pieza es una copia aparte:

| Pieza | Cuándo suele entrar |
| --- | --- |
| Sprint N+1 sin soluciones | Miércoles, antes de liberar |
| Soluciones del sprint anterior | Después de su práctica del martes |
| Slides del jueves y otros añadidos (talleres) | Cuando estén listos |

Pregunta qué pieza toca y haz solo los pasos de esa pieza: el 1 para soluciones, el 2 para el sprint nuevo, y una copia directa para slides y añadidos. La puerta de revisión solo se pasa al copiar el sprint nuevo.

Cada copia son dos PRs seguidas: `feature/copy_from_material` → `develop` y `develop` → `main`. El título de la PR a `main` empieza por «release:» solo si abre un sprint, por ejemplo «release: Sprint 05»; si añade soluciones, slides o talleres, empieza por «feat:», por ejemplo «feat: soluciones Sprint 04». Cada pieza va en su propia PR. Las mergea el TA, y la que va a `main` en `equipo-montes` necesita la aprobación de la otra persona.

Ojo con la PR de `develop` a `main`: lleva **todo lo que `develop` tenga pendiente**, no solo la pieza de esa semana (en el S05 arrastró «TC Movies»). Dilo en la descripción. Y el orden importa: la PR a `main` se deja en **borrador** hasta que la copia se haya mergeado en `develop`; solo entonces pasa a «Ready for review», y se comprueba que lleva los ficheros esperados.

## Repos y ramas

| Repo | Rama de trabajo | Destino |
| --- | --- | --- |
| `material_bootcamp_AI_Engineering` | Solo lectura | Fuente |
| `bootcamp_AI_Engineering_10_26` | `feature/copy_from_material` | PR a `develop`, luego PR de `develop` a `main` |

Pregunta en qué carpeta tiene la persona los repos y comprueba que están al día antes de copiar nada.

## Pasos

Si se pide `--dry-run`, haz los pasos de comprobación y enseña el plan completo sin copiar ni cambiar nada.

### Puerta de revisión · el sprint N+1 está revisado

Solo al copiar el sprint nuevo, y antes del Paso 0. Lo que se copia al repo de alumnos es lo que van a leer ellos, así que primero tiene que estar revisado. Quien imparte el sprint lo hace con la skill `preparar-sprint`, en sus fases 0, 0b y 0c; aquí solo se comprueba que está hecho. Pide a la persona los informes, o búscalos en su carpeta `Sprint_XX/preparacion_TA`:

| Fase de `preparar-sprint` | Qué prueba que está hecha |
| --- | --- |
| 0 · Análisis y versiones | Tabla de versiones y modelos del sprint. Si algo cambió respecto al sprint anterior, con la fuente oficial. Preguntas del análisis resueltas |
| 0b · Revisión del material | `fase3_revision_material_practica.md` y `cambios_README_teoria.md`, sin hallazgos obligatorios abiertos |
| 0c · Aplicar cambios | `cambios_aplicados_Sprint_XX.md` y los cambios ya aplicados en material (README y teoría con la tabla de modelos, sin marcas de revisión) |

Las fases 1, 2a, 2b, 4 y 5 (slides, notas, mazo de notas, caso práctico y PDF de enlaces) no bloquean la liberación: son para las sesiones y entran después, como piezas aparte.

- Si falta alguna prueba, **para**, dilo y ofrece lanzar `preparar-sprint` con las fases que faltan (para revisar, la 0, la 0b y la 0c).
- Solo se sigue sin ellas si la persona lo pide de forma explícita. Anótalo en Incidencias del informe, con quién lo decidió.

### Paso 0 · Comprobar el sprint N+1 en material

- Localiza el módulo y la carpeta del sprint N+1. Desde el S05 la estructura es `<Modulo>/Sprint_XX/{01_Teoria/NN_Bloque/, 02_Workout/NN_Bloque/, Practica_live_review/, README.md, assets/}`.
- Si falta `01_Teoria/`, `02_Workout/` o el `README.md`, para y avisa.
- Las carpetas que terminan en « 2» son duplicados de Finder: no se copian nunca y se listan en Incidencias.
- Busca en lo que se va a copiar marcas de revisión (✏️, ⚠️, ℹ️, 🤖) y copias `_v2`. Si hay alguna, no se copia: se lista en Incidencias.

### Paso 1 · Soluciones del sprint N

En `bootcamp_AI_Engineering_10_26`, rama `feature/copy_from_material`: copia desde material todas las soluciones del sprint N (ficheros `*_SOLUTION*` y carpetas `SOLUTION/`), también los de `Practica_live_review/`, que no estén ya. Déjalos en stage.

### Paso 2 · Sprint N+1 sin soluciones

En la misma rama, copia el sprint N+1 con la misma ruta de módulo que en material, sin `*_SOLUTION*`, sin `README_profes.md` y sin duplicados « 2». Déjalo en stage.

Al terminar los pasos 1 y 2, enseña qué hay en stage y **espera el OK** antes de hacer commit, push o abrir PR. Con el OK, el orden es:
1. PR de `feature/copy_from_material` a `develop`.
2. PR de `develop` a `main`, «release: …» si es el sprint nuevo o «feat: …» si son soluciones o slides. Si es el sprint nuevo, se deja abierta hasta la hora de liberar del jueves.

### Paso 3 · Jueves: liberar

- La PR a `main` la mergea el TA, nunca Claude. Comprueba después que el sprint N+1 está en `main` y que no hay `_SOLUTION` de N+1 ni `README_profes.md`.
- Campus: en la sección del sprint N+1, comprueba que cada «Fundamentos técnicos y ejemplos» apunta a `blob/main/<Modulo>/Sprint_XX/01_Teoria/NN_Bloque/README.md`, o a la carpeta si el bloque no tiene README, igual que el sprint anterior. El curso de OCT26 está en `docs/mapa-recursos.md` del repo `equipo-montes`.
- La sección se muestra solo cuando la persona lo confirme.

### Paso 4 · Informe

1. Sprints N y N+1 detectados.
2. Puerta de revisión: qué pruebas había, cuáles faltaban y si se siguió sin ellas.
3. Soluciones añadidas.
4. Sprint N+1 copiado.
5. Campus: recursos revisados y URL finales.
6. Qué ha quedado en stage o en PR en cada repo.
7. Incidencias, marcas de revisión y duplicados « 2».
8. Ambigüedades, con la pregunta para la persona.

Después, el mensaje de apertura del sprint lo escribe el TA con las plantillas de mensajes (spec 005).

## Reglas

- Nunca una PR a `main` que no venga de `develop`.
- Nunca soluciones del sprint nuevo (`*_SOLUTION*` ni carpetas `SOLUTION/`) ni `README_profes.md` en el repo de alumnos.
- Nunca marcas ni iconos de revisión en lo que va al repo de alumnos.
- No se cambia nada en el campus sin confirmación.
- Ante cualquier caso que estas reglas no cubran, para y pregunta.

## Pendiente

- El id del curso de OCT26 en el campus y la parte de workouts en adminonline (LTI). Hasta tenerlos, el Paso 3 solo revisa enlaces.
