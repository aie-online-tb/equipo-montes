# Fases de preparación del sprint

Texto del prompt maestro v2 de Soraya. Único cambio, decidido por Hugo el 17/11/2026: la revisión del material (antes Fase 3) y la aplicación de cambios (antes Fase 3b) pasan a ser las fases **0b** y **0c** y van justo después del análisis, porque el sprint tiene que estar revisado antes de liberarse. El orden es 0, 0b, 0c, 1, 2a, 2b, 4 y 5. El original, sin tocar, está en `incubadora/soraya/preparar-sprint/`.

## Fase 0 · Análisis (antes de producir nada)
1. **Lee todo el zip.** Hazme las preguntas que necesites sobre alcance, hilo conductor, reparto y dudas del material.
2. **Contenidos que faltan:** avísame si los README prometen contenidos que no están en los notebooks de teoría.
3. **Mapa de conceptos y agenda de la teoría.** Prepara el mapa de conceptos y la agenda (minutos por bloque y número de slides). Además:
   - lista lo que reservas para el caso práctico;
   - propónme **3–4 opciones de hilo conductor**.
4. **Revisión de versiones y modelos** (siempre, en todos los sprints): comprueba en las páginas oficiales qué versiones de librerías, SDK, APIs y modelos usa el material. Compáralas con la tabla del sprint anterior:
   - **Si no hay cambios**, mantén la misma tabla y el mismo modelo de ejemplo en teoría y ejercicios.
   - **Si hay cambios** (un modelo retirado, una versión nueva del SDK que rompe algo, un cambio en la capa gratuita…), dime cuál, cita la fuente oficial y propón la tabla actualizada. Cita solo la página oficial, como la de precios para la capa gratuita, y pon el recomendado a modo de ejemplo.
   - Comprueba de verdad que el modelo de ejemplo responde. Si da error (404, 503…), dímelo con el texto del error.
5. **Red:** comprueba a qué webs y APIs del material llegas desde tu entorno. Lo que no puedas verificar, lo ejecutaré yo en mi ordenador.

## Fase 0b · Revisión del material de práctica y de la teoría
1. **Ejecuta** las soluciones de `Practica_live_review`, `03_Material_de_Practica` y los workouts, como dice la regla 3.
2. **`fase3_revision_material_practica.md`:** un informe con un **código por hallazgo** (por ejemplo, C1, G2, 11-A). Para cada uno: el archivo y la celda, qué pasa (con la salida real), cómo arreglarlo y si es obligatorio u opcional. El fichero conserva este nombre aunque la fase ahora sea la 0b.
3. **`cambios_README_teoria.md`:** las ambigüedades y errores que tengo que corregir de cara a los alumnos. Para cada uno: **qué modificar y en qué parte está** (archivo, apartado y texto actual → texto propuesto).
4. **`modelos_[[…]]_alumnos.md`** (regla de versiones): la tabla de versiones y modelos, **con el mismo formato en todos los sprints**, para pegarla en el README del sprint.
   - **Si no ha cambiado nada**, reutiliza la del sprint anterior y mantén el mismo modelo de ejemplo en teoría y ejercicios.
   - **Si ha cambiado algo**, actualízala, cita la fuente oficial y lista en `cambios_README_teoria.md` cada sitio del material donde haya que cambiar el modelo o la versión.

**Criterio de Hugo (17/11/2026, del S05):**
- El **modelo se comprueba una sola vez**, en el ejercicio de `Practica_live_review`, con el SDK que instalan los `requirements.txt`. No se ejecuta la teoría ni se lanza todo para probar el modelo.
- Los notebooks con API se ejecutan **de uno en uno**, nunca en paralelo: la capa gratuita da `429 RESOURCE_EXHAUSTED`.
- La 0b revisa también los **contenidos** (README, teoría, workouts y enunciado de la práctica), no solo el modelo. Lo que no se ha ejecutado o leído a fondo se dice en el informe.
- La solución de la práctica se ejecuta solo para revisar. **No se libera** con el sprint.
- Un modelo `*-preview` puede dar 404 con `google-genai` 3.x aunque responda por `curl`: el SDK usa la API `v1` y `curl` suele usar `v1beta`. Prueba siempre con el SDK.

## Fase 0c · Aplicar los cambios para subirlos al repo
Basándote en los informes de la Fase 0b que yo te valide:
- **Notebooks (`.ipynb`):** no se tocan los originales. Crea una copia `_v2`:
  - una celda inicial que resume los cambios;
  - en mis copias de trabajo, cada celda cambiada o nueva lleva su marca (regla 9).
  - Guarda las copias sin salidas.
  - Comprueba que pasan la validación de `nbformat` y que el código compila.
- **Textos (`.md`, `.py`, `.html`, README):** se editan directamente, sin marcas ni iconos y con el formato original (regla 10).
- **Incluye** la carpeta `Practica_live_review` y los README. Los `_SOLUTION` solo si te lo pido (regla 8).
- **`cambios_aplicados_Sprint_XX.md`:** el informe de lo que has cambiado. Para cada cambio: el archivo, el código del informe y en qué consiste. Lista también lo que no has cambiado a propósito y por qué.
- **Ejecución en mi ordenador:** prepárame un script para ejecutar ahí los `_v2` que necesiten red o claves, y revisa el resultado cuando te lo pase.
- **Cuando lo aplique en el repo**, la versión que va al repo no lleva marcas.
- **Los mismos cambios van también al repo `material`** (PR a la rama de trabajo de quien imparte, en OCT26 `hugo`), para que el sprint siguiente no arrastre el fallo. Los `_SOLUTION` de material sí se corrigen ahí, si Hugo lo pide.

## Fase 1 · Slides de la sesión de teoría
- **Formato:** página web publicada como artifact, con el mismo estilo que la plantilla.
  - Colores corporativos: rojo `#F42C37` y negro `#1D1D1B`, con fondo blanco.
  - Tipografías: Archivo (títulos), IBM Plex Sans (texto) y JetBrains Mono (código).
  - Logo de The Bridge: la plantilla ya lo trae.
  - **Los símbolos de código se ven tal cual se escriben.** `==`, `!=`, `<=`, `>=`, `->`, `**`, `//`, etc. no se pueden «juntar» en un único glifo. Desactiva las ligaduras de JetBrains Mono en todo el código: bloques, editor, resaltado, salida y código en línea (`font-variant-ligatures: none; font-feature-settings: "liga" 0, "calt" 0;`). Compruébalo mirando una slide con esos operadores.
- **Funcionalidad que debe conservar:**
  - Navegación con flechas, índice con la tecla `I` y pantalla completa.
  - Python ejecutable en el navegador (Brython 3.13.2), con `input()` que lee de una caja «Entrada».
  - Errores mostrados con su tipo, mensaje y línea.
  - Botón «Solución» en los ejercicios y playground de Markdown solo si el tema lo pide. Si no se usa, quita también su JavaScript sin romper el resto.
  - Ajuste conocido del motor: si el código pasa por `compile()`, Brython pierde las docstrings. Ejecuta el texto con `exec` y acepta el nombre de archivo `"<string>"` al buscar la línea del error.
- **Objetivo:** **presentar los conceptos nuevos** del sprint. El alumno aún no ha visto nada y le surgen muchas dudas; la práctica llega en el caso práctico.
- **Extensión:** **15 slides como máximo**. No te saltes ningún concepto de la teoría: agrupa temas relacionados en la misma slide.
- **Estructura:**
  - Portada · semana + agenda con minutos por bloque (en una sola slide) · slides de contenido · resumen final con Kahoot.
  - **La mayoría de las slides de contenido son de conceptos, con poco texto**: qué es, para qué sirve y cómo se escribe. Usa viñetas cortas, una tabla o un esquema, sin párrafos largos.
  - **Código ejecutable solo en un par de slides por bloque**, en las que muestran el concepto clave en acción. En esas slides, explicación a la izquierda y código a la derecha.
  - **Ejemplos nuevos, del hilo conductor, no los del repo.** Los conceptos son los mismos que en la teoría.
  - El modelo o la versión de los ejemplos es el de la tabla de la Fase 0.
- **Dinámica en cada bloque:**
  - Una pregunta al grupo como mucho por slide: «Antes de mirar», «Votad», «Pregunta trampa».
  - Un quiz rápido de «¿qué devuelve?».
  - Cómo leer los errores: tipo + mensaje + línea, y los errores típicos del bloque.
  - Un ejercicio con botón «Solución».
- **No adelantes el caso práctico:**
  - no uses funciones que los alumnos tengan que descubrir solos;
  - no resuelvas un ejercicio de `Practica_live_review`.
- **Código seguro:** nada de `while True` fuera de un generador, y no imprimas sets de textos si la respuesta depende del orden.
- **Comprobación:** mide que nada se sale de cada slide, con las fuentes reales cargadas.
- [[Opcional: un adelanto breve de ___ en el bloque ___]]

## Fase 2a · Notas del profesor para la teoría (`.md`)
- **Mapa de conceptos → número de slide.**
- **Ideas fuerza** de la sesión.
- **Lista para antes de clase.** Incluye probar el día antes las claves y el modelo de ejemplo, y la red del aula.
- **Cronograma** con puntos de control (en qué slide deberías estar en cada minuto) y qué recortar si vas tarde.
- **Guion slide a slide**, con lo siguiente en cada slide:
  - qué decir y qué demo hacer;
  - «Antes de mirar» con la respuesta comprobada;
  - la salida exacta del código;
  - un «¿Qué devuelve X?» (tipo y valor);
  - preguntas probables con su respuesta;
  - «En el trabajo» (para qué se usa de verdad);
  - errores típicos con su **texto exacto**;
  - un escenario del día a día con el hilo conductor.
- **Tabla de correspondencia** entre cada ejemplo de las slides y el equivalente del repo.
- **Banco de preguntas extra** con respuestas, que sirva de base para el Kahoot.
- **Avisos:**
  - diferencias entre Brython y Colab/CPython;
  - qué no se pudo verificar desde tu entorno;
  - incoherencias del material: salidas guardadas incorrectas, enlaces antiguos, modelos retirados, contenidos prometidos que faltan…

## Fase 2b · Mazo de notas para la segunda pantalla
**Solo cuando te devuelva mis slides y mis notas editadas.**
- Convierte el «Guion slide a slide» de **mis** notas en una presentación (artifact de tipo Slides) para tenerla en una segunda pantalla mientras doy la clase. Usa el mismo estilo que los mazos de sprints anteriores.
- **Etiquetas:** cada diapositiva lleva la etiqueta S1…Sn con la **numeración real de mis slides editadas**, no la de tu versión. Parte las más densas en «1/2», «2/2».
- **Código de colores:** naranja para las preguntas al grupo (con su respuesta), azul («EN DIRECTO») para lo que hay que ejecutar, con su salida exacta, y una píldora «SALTABLE» para lo que se puede recortar.
- **Pie de página:** el bloque, los minutos y los puntos de control, ya con la numeración nueva.
- **Erratas:** corrígelas. Los cambios de contenido (algo incorrecto) avísamelos uno a uno.
- **Lista de desajustes:** dime qué quité de las slides pero sigue en las notas, y qué partes de las notas o de la agenda usan todavía la numeración antigua. **No toques mis slides.**

## Fase 4 · Caso práctico ([[N]] sesión(es))
1. **Reparto de los ejercicios de `Practica_live_review`** entre las sesiones:
   - minutos por ejercicio, en el orden de la teoría y contando el Kahoot del inicio;
   - los ejercicios **«si da tiempo»**, y qué recortar si vas tarde;
   - roles de equipo que rotan;
   - qué mirar mientras circulas (error frecuente → pregunta sin dar la respuesta);
   - un **plan B** si falla la red del aula.
   - Si propones un reparto, márcalo como Propuesta.
2. **Notebook para mí (`.ipynb`) con las soluciones**, por sesión y **ya ejecutado desde cero**. Si hay `input()`, simúlalo y dilo. Para cada ejercicio:
   - el enunciado del repo;
   - la **solución oficial copiada tal cual** del `_SOLUTION`;
   - 🔑 notas clave (qué remarcar y qué se usa que no esté en la teoría);
   - ⚠️ fallos o cosas raras de la solución oficial, comprobados ejecutándola;
   - ❓ 2 o 3 posibles preguntas de los alumnos, con su respuesta.
   - Si una solución falta o tiene errores, añade una versión correcta marcada como Propuesta.
   - Al final, una chuleta de preguntas rápidas.
3. **Notebook para los alumnos (`.ipynb`) con solo los ejercicios**, sin teoría y sin soluciones. Cada ejercicio con:
   - contexto breve, enunciado y código de partida del repo;
   - pistas desplegables;
   - una celda vacía;
   - una **celda de comprobación** que diga ✅ o qué revisar, sin dar la respuesta.
   - Si la comprobación necesita nombres concretos de variables o funciones, indícalos en «Para la comprobación».
4. **Verificación de las comprobaciones** con soluciones correctas (todas ✅) y con soluciones erróneas (ningún ✅). Lo que necesite red, en un script para mi ordenador que guarde el resultado en un `.txt` y el notebook del TA ejecutado.

## Fase 5 · Referencias para profundizar
1. **`referencias_sprintXX.md`:** las referencias oficiales por tema, solo páginas oficiales o la documentación de la librería. **Comprueba que cada enlace funciona** y que trata lo que dices.
3. **PDF de referencias con el formato del PDF modelo**, que se llame `Enlaces_para_profundizar_SprintXX.pdf`. Replica el modelo:
   - el logo de The Bridge, el título «LINKS Y REFERENCIAS PARA SEGUIR PROFUNDIZANDO», la línea gris y la marca de agua;
   - los apartados numerados en negrita cursiva;
   - las URL completas, en azul y subrayadas, **todas clicables**.
   - Las URL largas se parten solo por las barras «/».
   - Dime qué difiere del modelo (por ejemplo, la tipografía si no está disponible).
