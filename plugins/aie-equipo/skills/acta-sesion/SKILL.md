---
name: acta-sesion
description: Convierte la transcripción .vtt de una sesión del bootcamp AI Engineering de The Bridge (Live Review, sesión de dudas, taller) en el acta de la sesión, en Markdown y en PDF maquetado con la identidad de The Bridge. Úsala cuando pidan «el acta de la clase», «apuntes de la clase», «resumen de la LR», «estructurar la transcripción» o trabajen con un .vtt de una sesión.
---


# acta-sesion

Skill de Soraya (`apuntes-clase-vtt`), pasada al plugin común. Los cambios respecto a su versión están al final, en «Cambios para el equipo».

Convierte un `.vtt` en apuntes de clase **cortos y densos**: el PDF debe caber en **~4 páginas interiores** (sin contar portada) y leerse de un vistazo.

## Rutas

- **Datos de trabajo**: relativos al directorio actual (normalmente `.../Transcripciones/`).
- **Recursos de la skill** (`SKILL_DIR` = la carpeta donde está este `SKILL.md`, que Claude Code indica al cargar la skill):

| Archivo | Uso |
|---|---|
| `plantillas/apuntes_plantilla.md` | Esqueleto breve con marcadores `{{...}}` |
| `plantillas/ejemplo_LR1_sprint13.md` | Ejemplo real de la longitud y densidad objetivo |
| `referencia/guia_estilo.md` | Reglas duras de estilo. **Léela siempre antes de redactar** |
| `scripts/limpiar_vtt.py` | Parsea el VTT → texto limpio con `[HH:MM] Hablante: …` |
| `scripts/generar_pdf.py` | Convierte el `.md` a `.pdf` con la identidad de The Bridge |
| `assets/logo_thebridge*.svg`, `assets/fonts/` | Logo e Inter Tight + JetBrains Mono |

## Salidas (en el directorio actual)

| Archivo | Qué es |
|---|---|
| `<basename>_resumen_sprintNN.md` | Apuntes finales en Markdown |
| `<basename>_resumen_sprintNN.pdf` | Mismos apuntes maquetados |

`NN` siempre con dos dígitos. `<basename>` = stem del `.vtt` original.

El `.vtt` original **no se toca**.

---

## Paso 0 — Localizar el VTT y los metadatos

1. Si el usuario dio nombre de archivo, úsalo. Si no, lista los `.vtt` del `cwd`: 1 solo → úsalo; varios → pregunta; ninguno → error.
2. Deduce lo que puedas; pregunta solo si no se puede:

| Metadato | Cómo deducirlo |
|---|---|
| **Número de sprint** | Carpeta padre `Sprint_13` / `sprint_01` / `S13` |
| **Número de LR** | Nombre del archivo (`LR1.vtt`) |
| **Profesor** | Speaker más frecuente del VTT |
| **Título** | Primeras intervenciones del profesor + bloques principales |
| **Módulo / contexto** | Preguntar al usuario |

3. Limpia el VTT:

```bash
python "$SKILL_DIR/scripts/limpiar_vtt.py" "<archivo.vtt>" \
  --out "_transcripcion_limpia.txt" --stats
```

4. Lee ese `_transcripcion_limpia.txt` entero. **Es la única fuente de verdad.** Bórralo al final (Paso 4). El `.vtt` original queda intacto.

---

## Paso 1 — Lectura y planificación

1. Lee `SKILL_DIR/referencia/guia_estilo.md` entero.
2. Lee `SKILL_DIR/plantillas/ejemplo_LR1_sprint13.md` para fijar **longitud y densidad**.
3. Lee `SKILL_DIR/plantillas/apuntes_plantilla.md` para los marcadores.

Con el `.txt` delante, decide:

- **3 ideas clave** (una línea cada una).
- **3–5 secciones** de desarrollo. Agrupa; una idea por sección.
- Rango de timestamps por sección (`HH:MM–HH:MM`).
- **Glosario y dudas son opcionales**: solo si aportan algo que no esté en el cuerpo.

---

## Paso 2 — Redactar el `.md`

Escribe en el `cwd` el archivo `<basename>_resumen_sprintNN.md`. **Objetivo: PDF de 4 páginas interiores.**

### Métricas duras

| Métrica | Objetivo |
|---|---|
| Líneas totales del `.md` | **70–130** |
| Ideas clave | **3** bullets de **1 línea** |
| Secciones de desarrollo | **3–5** |
| Cuerpo por sección | 2–5 líneas de prosa + lista corta opcional |
| Tablas en todo el documento | **≤ 3** |
| Bloques de código | **≤ 2**, cada uno **≤ 12 líneas** |
| Glosario (si lo hay) | **≤ 6 términos** |
| Dudas resueltas (si las hay) | **≤ 3 dudas**, respuesta de **1–2 líneas** |

### Reglas de contenido

- Español, segunda persona o impersonal. Frases cortas.
- Timestamps en formato `⏱ HH:MM–HH:MM` (dos dígitos, guion largo `–`).
- Código, archivos, métodos en `` `inline` ``. Bloques `python`/`bash` solo si citas ≥3 líneas distintas.
- **Nada que no esté en el VTT**: no inventes APIs, bibliotecas, nombres de alumnos.
- **Nada de ruido**: saludos, "¿se me oye?", esperas, charlas privadas.
- **No dupliques entre cuerpo y glosario**: si ya lo explicaste, no lo repitas.

### Callouts (muy importante — fuente de errores pasados)

Los emojis `⚠️ 💡 📌 ✅ ❌` al inicio de línea se renderizan en el PDF como etiqueta roja seguida de tu frase:

| Escribes | Se ve en PDF |
|---|---|
| `⚠️ olvidar la vuelta al supervisor…` | **Atención:** olvidar la vuelta… |
| `💡 el modelo propone, Python decide` | **Idea:** el modelo propone… |
| `📌 el estado arranca con cadenas vacías` | **Nota:** el estado arranca… |

**❌ NUNCA escribas la palabra de callout después del emoji**: `💡 **Idea:** …` se verá *"Idea: Idea: …"*. (El script tiene una red de seguridad, pero no cuentes con ella: hazlo bien al escribir.)

Las secciones fijas (`🎯 Ideas claves`, `📑 Índice`, `📌 Glosario`, `❓ Dudas`, `📅 Pendiente`) sí llevan emoji — ese se elimina en el PDF automáticamente.

---

## Paso 3 — Generar el PDF

```bash
python "$SKILL_DIR/scripts/generar_pdf.py" \
  "<basename>_resumen_sprintNN.md" --toc
```

Si falta la librería, instala con `pip install markdown-pdf` y vuelve a ejecutar.

### Diseño corporativo (automático, no lo toques)

- Paleta: rojo `#E30613`, negro, crema `#FAF7F8`.
- Tipografía: Inter Tight (ExtraBold en titulares), JetBrains Mono para código.
- Portada negra con logo blanco, etiqueta roja `LIVE REVIEW N – SPRINT NN`, título grande y ficha con profesor + contexto.
- Páginas interiores: cabecera con logo + nombre de la sesión; pie con `thebridge.tech · Bootcamp AI Engineering` + número de página.
- H2 numerados con filete rojo; tablas con cabecera negra y filas alternas; código sobre fondo oscuro con barra roja; citas sobre crema.

La portada se construye del propio `.md`. Respeta el esqueleto:

- `# Live Review N – Sprint NN: Título` → etiqueta + título grande.
- `> Clase impartida por <Profesor>. <Contexto>` → ficha de metadatos.
- `> Formato: …` → fila de la ficha.

Opciones:

- `--toc` → marcadores navegables (recomendado).
- `--sin-portada` → sin portada; el H1 queda al inicio.
- `--out <ruta.pdf>` → otra ruta.

Si aparece `AVISO: el PDF parece haber perdido texto…`, abre el PDF y revisa la tabla o bloque de código que cae en el salto de página. Si falla por otro motivo, avisa al usuario y entrega al menos el `.md`.

---

## Paso 4 — Comprobar y entregar

Lista de verificación obligatoria:

- [ ] El `.md` tiene **70–130 líneas**.
- [ ] Hay **3–5 secciones** de desarrollo, cada una con su `⏱ HH:MM–HH:MM`.
- [ ] El PDF ocupa **4 páginas interiores** (± 1).
- [ ] **Cero duplicados**: grep del `.md` con `(💡|⚠️|📌|✅|❌)\s*\*\*(Idea|Atenci|Nota|Sí|No)` → sin matches.
- [ ] No hay `AVISO:` del script PDF (o se ha revisado).
- [ ] No hay placeholders `{{...}}` sin rellenar.
- [ ] No hay nombres propios de alumnos ni ruido del VTT.
- [ ] Timestamps `HH:MM–HH:MM` con dos dígitos y guion largo.
- [ ] La portada muestra bien sprint, título y profesor.
- [ ] Se ha borrado `_transcripcion_limpia.txt`. El `.vtt` sigue intacto.

Al terminar, di en dos o tres líneas:

- qué se ha generado y dónde,
- qué metadatos has deducido (sprint, profesor, título) para que los revise,
- cualquier `AVISO` o `ERROR` del script.

---

## Paso 5 — Subir el acta al repo de alumnos (opcional)

Solo si la persona lo pide. Antes de tocar nada, enséñale el plan y espera su OK.

- Repo: el de alumnos del intake (OCT26: `bootcamp_AI_Engineering_10_26`).
- Rama: `develop-actas`. PR a `develop`, nunca a `main`.
- Ruta: `00_Actas_Sesiones/Sprint_XX/`.
- Nombre: `AIE_SXX_SESION_DD_MM.md` y `.pdf` (por ejemplo, `AIE_S05_LR1_19_11.pdf`), que es el que usa la automatización de grabaciones.
- El campus enlaza el PDF del repo en forma `blob/main/…`. Da 404 hasta la release de `develop` a `main`, y está aceptado.

## Cambios para el equipo

Respecto a la skill original de Soraya:

- Nombre `acta-sesion` y rutas relativas a la carpeta de la skill, para que funcione instalada desde el plugin.
- Paso 5 nuevo, opcional, con el nombre y la rama que usa la automatización de grabaciones.
- Plantillas, guía de estilo, scripts, logo y fuentes, sin cambios.

Las actas dicen «alumnado»: es una excepción aceptada a la norma de masculino genérico.
