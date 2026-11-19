# Apertura de sprint

Cuándo: jueves a primera hora (decidido el 18/11/2026), con el sprint ya liberado en el repo y visible en el campus. Quién: TA, con la automatización de Soraya cuando esté compartida.

## Plantilla

```
¡ @canal !

Ya tenéis disponible el Sprint {N}{, el último del Módulo X / con el que empezamos el Módulo X - Nombre}. {Una o dos frases que unan con lo anterior y planteen la pregunta que responde el sprint.} Esto es lo que vais a trabajar:

* **{Bloque 1}:** {qué se hace y la idea clave en una frase}.
* **{Bloque 2}:** {…}.
* **{Bloque 3}:** {…}.

{Opcional: cómo trabajar el sprint o qué es lo único que se practica en directo.}

Ya está disponible en el [campus]({ENLACE_CAMPUS}) y en el [repositorio de GitHub]({ENLACE_REPO}).

Como siempre, estamos disponibles para cualquier duda que os surja. ¡A por ello!
```

## Reglas

- Un punto por bloque de `01_Teoria/`, con el nombre del bloque tal como sale en el repo.
- Cada punto dice qué se hace y deja una idea para recordar. Si hay una confusión típica, se avisa con «Ojo con…».
- Los workouts no son entregables: no se habla de entregas.
- El enlace al repo apunta a la carpeta del sprint en `main`.

## Ejemplo real (MAY26, Sprint 16)

```
¡ @canal !

Ya tenéis disponible el Sprint 16, el último del Módulo 6 - MLOps para IA Generativa. Hasta ahora habéis construido una API segura con un agente detrás; este sprint responde a la pregunta que falta: ¿cómo la publico para que cualquiera pueda usarla desde una URL? Esto es lo que vais a trabajar:

* **Docker y containerización:** empaquetaréis la API en una imagen y la arrancaréis en un contenedor. La idea clave: si funciona en el contenedor, funciona en cualquier máquina. En el workout practicáis con una API segura (CRUD) en Docker.
* **Deployment de RAG y agentes en cloud:** llevaréis el agente cultural a Render con una base de datos PostgreSQL, y veréis por qué el RAG viaja dentro del mismo contenedor. Ojo con las claves: van en el panel del servicio, nunca en el repositorio.
* **Arquitectura, costes y CI/CD:** qué límites tiene un servicio en la nube (cold start, memoria, cuotas), cuánto cuesta y cómo sería un pipeline mínimo con GitHub Actions. Es teoría: no hay workout de esto.

Se publican los tres bloques de golpe: leed la teoría, seguid los workouts (repo + vídeo de la demo) y practicad por vuestra cuenta. Los workouts no son entregables. El único ejercicio del sprint es la Live Review: desplegar una API de calidad del aire con Docker, PostgreSQL y Render.

Ya está disponible en el campus y en el repositorio de GitHub.

Como siempre, estamos disponibles para cualquier duda que os surja. ¡A por ello!
```
