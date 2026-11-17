---
name: normas-aie
description: Normas de redacción y de publicación del bootcamp de AI Engineering de The Bridge. Úsala siempre que escribas o revises algo que vaya a ver un alumno (material, mensajes, comentarios de corrección, guiones, Kahoot) o que vaya a entrar en un repo del bootcamp.
---

# Normas del bootcamp de AI Engineering

## Redacción de cara al alumno

- Español sencillo. Masculino genérico, nunca lenguaje neutro. Excepción aceptada: las actas de sesión usan «alumnado».
- Los sprints no tienen «Unidades». No escribas «Unidad XX»: nombra por sprint y bloque temático.
- El material reutilizable (guiones de vídeo, Kahoot, ejercicios) no menciona el sprint ni el orden del curso en el texto que ve o escucha el alumno. Esa referencia solo va en el título o en el nombre del fichero.
- En AI Engineering no hay prácticas obligatorias. No hables de prácticas obligatorias ni de entregas salvo en Team Challenges y Project Breaks.
- Nombres de fichero sin espacios ni tildes.

## Lo que entra en un repo

- No toques ficheros `_SOLUTION` salvo que te lo pidan.
- En un repo de alumnos nunca hay `README_profes` ni `_SOLUTION` del sprint activo. Las soluciones se suben al liberar el sprint siguiente.
- Nunca leas, imprimas ni pegues el contenido de un `.env` ni de ninguna clave.

## Git en los repos del bootcamp

- Nunca una PR a `main` que no venga de `develop`.
- En los repos de alumnos el contenido entra por `feature/copy_from_material` (OCT26) o `feature_copy_from_material` (MAY26) y la PR a `main` se titula «release: …» si abre un sprint o «feat: …» si añade soluciones, slides o talleres.
- Las actas van por la rama `develop-actas` hacia `develop`.
- Si una rama con un uso ya registrado va a sustituirse por otra, avisa y pide confirmación a una persona.
