---
name: preparar-sprint
description: Prepara un sprint del bootcamp AI Engineering de The Bridge por fases, para quien lo va a impartir. Las fases son análisis del material, slides y notas de la teórica, revisión y corrección del material, caso práctico y PDF de enlaces para profundizar. Úsala cuando pidan «preparar el sprint», «preparar la teórica», «revisar el sprint antes de liberarlo», «preparar el caso práctico» o «el PDF de enlaces» de un sprint.
---

# preparar-sprint

Basada en el prompt maestro v2 de Soraya. Sus reglas y sus fases están en `referencia/` sin cambios. Esta skill solo añade cómo arrancar y de dónde sale cada dato.

Cubre las funciones que siguen al sprint: preparar la teórica (7), preparar el caso práctico (8), el PDF de enlaces (10) y revisar el sprint y aplicar las correcciones (11). Las hace **quien vaya a impartir el sprint**, aunque esa semana sea TA. Los plazos están en `docs/semana-tipo.md` del repo `equipo-montes`: la revisión vence el martes a las 19:00 y la teórica, el miércoles.

## Antes de empezar

1. Lee `referencia/reglas.md` entero. Valen para todas las fases.
2. Reúne estos datos. Deduce lo que puedas y pregunta solo lo que falte:

| Dato | De dónde sale |
| --- | --- |
| Número de sprint | Lo dice la persona o el banner del calendario OCT26 |
| Material del sprint | La carpeta del sprint en `material_bootcamp_AI_Engineering`, en la rama de trabajo de quien prepara, o un zip con el sprint |
| Sesiones | Calendario OCT26: teórica el jueves y práctica el martes, de 19:00 a 21:00. Pregunta cuánto dura el Kahoot de cada una |
| Ordenador enlazado | Pregunta si hay un ordenador enlazado y en qué carpeta está el sprint |
| Tabla de modelos del sprint anterior | La del sprint anterior en el repo. Si no la hay, `plantillas/modelos_gemini_alumnos.md` es la del S04 |
| Hilos conductores ya usados | `referencia/reglas.md`, regla 6. Añade los nuevos al terminar |

3. Plantillas en `plantillas/`:
   - `plantilla_slides.html`: plantilla visual y motor de código de las slides.
   - `plantilla_enlaces_para_profundizar.pdf`: modelo del PDF de la Fase 5.
   - `modelos_gemini_alumnos.md`: tabla de versiones y modelos del S04.

## Fases

Están en `referencia/fases.md`. Van en orden y, al terminar cada una, se resume en 5 líneas como máximo y se espera el OK de la persona antes de seguir:

| Fase | Qué sale |
| --- | --- |
| 0 · Análisis | Preguntas, mapa de conceptos, agenda, opciones de hilo conductor y revisión de modelos |
| 1 · Slides | Slides de la teórica, como artifact |
| 2a · Notas del profesor | `.md` con guion slide a slide |
| 2b · Mazo de notas | Para la segunda pantalla, solo cuando la persona devuelva sus slides editadas |
| 3 · Revisión del material | Informes de hallazgos, cambios en los README y tabla de modelos |
| 3b · Aplicar cambios | Copias `_v2` y el informe de cambios aplicados |
| 4 · Caso práctico | Reparto de ejercicios y notebooks del profesor y del alumno |
| 5 · Referencias | `referencias_sprintXX.md` y `Enlaces_para_profundizar_SprintXX.pdf` |

Si la persona solo pide una parte (por ejemplo, «revisa el sprint»), haz solo las fases que tocan: para revisar, la 0 y la 3.

## Límites

- No hagas `git add`, `commit` ni `push` en los repos del bootcamp: eso lo hace la persona (regla 8).
- No toques ficheros `_SOLUTION` salvo que te lo pidan.
- Nunca leas ni muestres un `.env`.
- Lo que va al alumno sigue la skill `normas-aie`.
