#!/usr/bin/env python3
"""Convierte los apuntes .md en un PDF con la identidad corporativa de The Bridge.

- Dependencia única: `pip install markdown-pdf` (trae PyMuPDF).
- No necesita pandoc, LaTeX ni fuentes instaladas en el sistema:
  la tipografía (Inter Tight + JetBrains Mono) y el logo van dentro de la
  skill, en `assets/`.
- Mantiene el .md tal cual y escribe el .pdf junto a él (o en --out).

Diseño (thebridge.tech):
  · Rojo corporativo #E30613 · Negro #000000 · Crema #FAF7F8 · Blanco
  · Tipografía Inter Tight (titulares en ExtraBold), código en JetBrains Mono
  · Portada en negro con el logo, etiqueta roja y el título de la clase
  · Cabecera con logo y pie con web + número de página en cada página interior

Uso:
    python generar_pdf.py <archivo.md> [--out <archivo.pdf>] [--toc] [--sin-portada]
"""
import argparse
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

SKILL_DIR = Path(__file__).resolve().parent.parent
ASSETS = SKILL_DIR / "assets"
FONTS = ASSETS / "fonts"
LOGO = ASSETS / "logo_thebridge.svg"
LOGO_BLANCO = ASSETS / "logo_thebridge_blanco.svg"

# ── Paleta corporativa ─────────────────────────────────────────────────
ROJO = "#E30613"
ROJO_LOGO = "#F5333F"
NEGRO = "#000000"
TINTA = "#1A1A1A"
GRIS = "#6B6B6B"
LINEA = "#E6E1E3"
CREMA = "#FAF7F8"

PIE_WEB = "thebridge.tech"
PIE_PROGRAMA = "Bootcamp AI Engineering"

# Nota: MuPDF pinta mal `background-color` en elementos en línea (code, span):
# solo se usan fondos en bloques (pre, th, blockquote).

# Márgenes del cuerpo (pt) en A4 (595 × 842)
M_IZQ, M_SUP, M_DER, M_INF = 56, 92, 56, 76


def _rgb(hex_color):
    h = hex_color.lstrip("#")
    return tuple(int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))


FONT_FACES = """
@font-face { font-family: "Inter Tight"; src: url(InterTight-Regular.ttf); }
@font-face { font-family: "Inter Tight"; font-style: italic; src: url(InterTight-Italic.ttf); }
@font-face { font-family: "Inter Tight"; font-weight: bold; src: url(InterTight-Bold.ttf); }
@font-face { font-family: "Inter Tight"; font-weight: bold; font-style: italic; src: url(InterTight-BoldItalic.ttf); }
@font-face { font-family: "Inter Tight SB"; src: url(InterTight-SemiBold.ttf); }
@font-face { font-family: "Inter Tight SB"; font-weight: bold; src: url(InterTight-SemiBold.ttf); }
@font-face { font-family: "Inter Tight XB"; src: url(InterTight-ExtraBold.ttf); }
@font-face { font-family: "Inter Tight XB"; font-weight: bold; src: url(InterTight-ExtraBold.ttf); }
@font-face { font-family: "Inter Tight MD"; src: url(InterTight-Medium.ttf); }
@font-face { font-family: "JetBrains Mono"; src: url(JetBrainsMono-Regular.ttf); }
@font-face { font-family: "JetBrains Mono"; font-weight: bold; src: url(JetBrainsMono-Bold.ttf); }
"""

# IMPORTANTE: el motor de maquetación de MuPDF (fitz.Story) pinta "fantasmas"
# (barras negras/grises sobre el texto) cuando el CSS lleva `background-color`
# o `border`. Por eso el CSS solo define tipografía y espaciado, y todos los
# fondos, filetes y bandas se dibujan después con PyMuPDF (ver `decorar_bloques`).
# Además, `padding` en <pre>/<blockquote> hace que MuPDF PIERDA texto al partir
# página: el "relleno" de esas cajas se simula con márgenes y se pinta a mano.
CSS = FONT_FACES + f"""
body {{ font-family: "Inter Tight", sans-serif; font-size: 10pt; line-height: 1.5;
        color: {TINTA}; margin: 0; }}
p {{ margin: 0 0 7pt 0; }}
strong, b {{ font-weight: bold; color: {NEGRO}; }}
em, i {{ font-style: italic; }}
a {{ color: {ROJO}; text-decoration: none; }}

h1 {{ font-family: "Inter Tight XB"; font-size: 22pt; line-height: 1.15; color: {NEGRO};
      margin: 0 0 12pt 0; }}
h2 {{ font-family: "Inter Tight XB"; font-size: 15pt; line-height: 1.2; color: {NEGRO};
      margin: 22pt 0 12pt 0; }}
h2 .num {{ color: {ROJO}; }}
h2 .ts {{ font-family: "JetBrains Mono"; font-size: 8.5pt; color: {GRIS}; }}
h3 {{ font-family: "Inter Tight SB"; font-size: 11.5pt; color: {ROJO};
      margin: 13pt 0 5pt 0; }}
h4 {{ font-family: "Inter Tight SB"; font-size: 10.5pt; color: {NEGRO}; margin: 10pt 0 4pt 0; }}

ul, ol {{ margin: 0 0 8pt 0; padding-left: 16pt; }}
li {{ margin: 0 0 3pt 0; }}

code {{ font-family: "JetBrains Mono", monospace; font-size: 8.6pt; color: #B3050F; }}
pre {{ font-family: "JetBrains Mono", monospace; font-size: 8.4pt; line-height: 1.45;
       color: #F2F2F2; padding: 0; margin: 16pt 13pt 22pt 16pt;
       white-space: pre-wrap; }}
pre code {{ color: #F2F2F2; font-size: 8.4pt; }}

table {{ width: 100%; margin: 6pt 0 12pt 0; font-size: 9.2pt; }}
th {{ font-family: "Inter Tight SB"; color: #FFFFFF; text-align: left; padding: 5pt 8pt; }}
td {{ padding: 4.5pt 8pt; vertical-align: baseline; }}  /* 'top' desalinea negritas/cursivas en MuPDF */
td strong {{ color: {NEGRO}; }}
th strong, th b, th em, th code {{ color: #FFFFFF; }}

blockquote {{ margin: 14pt 13pt 20pt 16pt; padding: 0; color: #3A3A3A;
              font-style: italic; }}
blockquote p {{ margin: 0; }}

.callout {{ font-family: "Inter Tight SB"; color: {ROJO}; }}
"""

# ── Preprocesado del Markdown ──────────────────────────────────────────
# Los emojis no existen en Inter Tight: se sustituyen por marcas tipográficas
# coherentes con la marca (o se eliminan en los títulos fijos).
EMOJI_TITULOS = ["🎯", "📑", "📌", "❓", "📅", "💡", "⚠️", "⚠", "✅", "❌", "★", "⭐"]
EMOJI_INLINE = {
    "⚠️": '<span class="callout">Atención:</span>',
    "⚠": '<span class="callout">Atención:</span>',
    "💡": '<span class="callout">Idea:</span>',
    "📌": '<span class="callout">Nota:</span>',
    "✅": '<span class="callout">Sí</span>',
    "❌": '<span class="callout">No</span>',
    "✓": '<span class="callout">✓</span>',
    "★": '<span class="callout">★</span>',
    "⭐": '<span class="callout">★</span>',
    "🎯": "",
    "📑": "",
    "📅": "",
    "❓": "",
}
RE_TS = re.compile(r"⏱\s*(\d{2}:\d{2}\s*[–-]\s*\d{2}:\d{2})")
RE_H2_NUM = re.compile(r"^(##\s+)(\d+)\.\s+(.*)$")

# Red de seguridad: si tras un emoji-callout viene inmediatamente la misma palabra
# en negrita (p. ej. `💡 **Idea:** …`), se eliminaría la negrita para no pintar
# "Idea: Idea:". Acepta variantes con/sin dos puntos y con tildes.
RE_CALLOUT_DUP = re.compile(
    r"(⚠️|⚠|💡|📌|✅|❌)\s*\*\*(Atenci[oó]n|Idea|Nota|S[ií]|No)\s*:?\*\*\s*:?\s*",
    re.IGNORECASE,
)


def _limpiar_titulo(texto):
    for e in EMOJI_TITULOS:
        texto = texto.replace(e, "")
    return re.sub(r"\s{2,}", " ", texto).strip()


def extraer_portada(md_text):
    """Separa el H1 y la cita inicial (metadatos) del resto del documento."""
    lines = md_text.splitlines()
    i = 0
    while i < len(lines) and not lines[i].strip():
        i += 1
    if i >= len(lines) or not lines[i].startswith("# "):
        return None, md_text

    h1 = lines[i][2:].strip()
    i += 1
    meta = []
    while i < len(lines) and (not lines[i].strip() or lines[i].lstrip().startswith(">")):
        if lines[i].strip():
            meta.append(lines[i].lstrip()[1:].strip())
        i += 1
    if i < len(lines) and lines[i].strip() == "---":
        i += 1

    eyebrow, titulo = "Apuntes de clase", h1
    m = re.match(r"^(.*?Sprint\s*\d+)\s*[:–—-]\s*(.+)$", h1, re.I)
    if m:
        eyebrow, titulo = m.group(1).strip(), m.group(2).strip()

    profesor, contexto, extra = None, None, []
    for linea in meta:
        linea = re.sub(r"[*_`]", "", linea)
        mp = re.match(r"^Clase impartida por\s+(.+?)\.\s*(.*)$", linea, re.I)
        if mp:
            profesor = mp.group(1).strip()
            contexto = mp.group(2).strip() or None
        elif linea:
            extra.append(linea)

    portada = {"h1": h1, "eyebrow": eyebrow, "titulo": titulo,
               "profesor": profesor, "contexto": contexto, "extra": extra}
    return portada, "\n".join(lines[i:])


def preprocesar(md_text):
    out, en_codigo = [], False
    for linea in md_text.splitlines():
        if linea.lstrip().startswith("```"):
            en_codigo = not en_codigo
            out.append(linea)
            continue
        if en_codigo:
            out.append(linea)
            continue
        if re.fullmatch(r"\s*(-{3,}|\*{3,}|_{3,})\s*", linea):
            # Separadores: el H2 ya lleva su filete rojo; MuPDF pinta los <hr> de forma irregular
            out.append("")
            continue
        if linea.startswith("#"):
            linea = _limpiar_titulo(linea)
            linea = RE_TS.sub(r'<span class="ts">  \1</span>', linea)
            linea = RE_H2_NUM.sub(r'\1<span class="num">\2.</span> \3', linea)
        else:
            # Colapsa `💡 **Idea:**` → `💡` para evitar "Idea: Idea:" en el PDF.
            linea = RE_CALLOUT_DUP.sub(r"\1 ", linea)
            for e, rep in EMOJI_INLINE.items():
                linea = linea.replace(e, rep)
            linea = RE_TS.sub(r"`\1`", linea)
        out.append(linea)
    return "\n".join(out)


# ── Decoración con PyMuPDF ─────────────────────────────────────────────
def _logo_pdf(fitz, ruta):
    svg = fitz.open(str(ruta))
    return fitz.open("pdf", svg.convert_to_pdf())


def _fuentes(fitz):
    return {
        "reg": fitz.Font(fontfile=str(FONTS / "InterTight-Regular.ttf")),
        "md": fitz.Font(fontfile=str(FONTS / "InterTight-Medium.ttf")),
        "sb": fitz.Font(fontfile=str(FONTS / "InterTight-SemiBold.ttf")),
        "xb": fitz.Font(fontfile=str(FONTS / "InterTight-ExtraBold.ttf")),
        "mono": fitz.Font(fontfile=str(FONTS / "JetBrainsMono-Regular.ttf")),
    }


def _texto(page, fuente, x, y, txt, size, color, align="left"):
    """Escribe una línea con la fuente corporativa. y = línea base."""
    w = fuente.text_length(txt, fontsize=size)
    if align == "right":
        x -= w
    elif align == "center":
        x -= w / 2
    tw = fitz_mod.TextWriter(page.rect, color=_rgb(color))
    tw.append((x, y), txt, font=fuente, fontsize=size)
    tw.write_text(page)
    return w


def _envolver(fuente, txt, size, ancho):
    palabras, lineas, actual = txt.split(), [], ""
    for p in palabras:
        prueba = (actual + " " + p).strip()
        if fuente.text_length(prueba, fontsize=size) <= ancho or not actual:
            actual = prueba
        else:
            lineas.append(actual)
            actual = p
    if actual:
        lineas.append(actual)
    return lineas


def dibujar_portada(doc, portada, F):
    fitz = fitz_mod
    page = doc.new_page(pno=0, width=595, height=842)
    W, H = page.rect.width, page.rect.height
    corte = 560  # zona negra superior

    # Fondo: negro arriba, crema abajo
    page.draw_rect(fitz.Rect(0, 0, W, corte), color=None, fill=_rgb(NEGRO))
    page.draw_rect(fitz.Rect(0, corte, W, H), color=None, fill=_rgb(CREMA))

    # Motivo gráfico: el "puente" del logo, grande y recortado a la derecha
    sx, sy, lado = 395, 300, 260
    page.draw_rect(fitz.Rect(sx, sy, sx + lado, sy + lado), color=None,
                   fill=_rgb(ROJO_LOGO), radius=0.16)
    k = lado / 31.414
    arco = fitz.Rect(sx + 5.234 * k, sy + 15.731 * k, sx + 26.179 * k, sy + lado)
    hueco = fitz.Rect(sx + 10.471 * k, sy + 20.966 * k, sx + 20.943 * k, sy + lado)
    page.draw_rect(arco, color=None, fill=_rgb(NEGRO))
    page.draw_rect(hueco, color=None, fill=_rgb(ROJO_LOGO))
    # el cuadrado "sangra" sobre el corte: tapamos lo que cae en la zona crema
    page.draw_rect(fitz.Rect(0, corte, W, H), color=None, fill=_rgb(CREMA))

    # Logo blanco
    logo = _logo_pdf(fitz, LOGO_BLANCO)
    page.show_pdf_page(fitz.Rect(56, 52, 56 + 137 * 1.15, 52 + 32 * 1.15), logo, 0)

    # Etiqueta (pill) roja
    eb = portada["eyebrow"].upper()
    size_eb = 8.5
    w_eb = F["sb"].text_length(eb, fontsize=size_eb)
    pill = fitz.Rect(56, 170, 56 + w_eb + 22, 170 + 21)
    page.draw_rect(pill, color=None, fill=_rgb(ROJO), radius=0.5)
    _texto(page, F["sb"], 56 + 11, 170 + 14.2, eb, size_eb, "#FFFFFF")

    # Título grande
    size_t = 30
    lineas = _envolver(F["xb"], portada["titulo"], size_t, 330)
    if len(lineas) > 5:
        size_t = 24
        lineas = _envolver(F["xb"], portada["titulo"], size_t, 330)
    y = 238
    for ln in lineas:
        _texto(page, F["xb"], 56, y, ln, size_t, "#FFFFFF")
        y += size_t * 1.12
    # subrayado rojo corto
    page.draw_rect(fitz.Rect(56, y - size_t * 0.55 + 14, 96, y - size_t * 0.55 + 17.5),
                   color=None, fill=_rgb(ROJO))

    # Ficha de metadatos en la zona crema
    filas = []
    if portada["profesor"]:
        filas.append(("Profesor/a", portada["profesor"]))
    if portada["contexto"]:
        filas.append(("Contexto", portada["contexto"]))
    for e in portada["extra"]:
        if ":" in e:
            k_, v_ = e.split(":", 1)
            filas.append((k_.strip(), v_.strip()))
        else:
            filas.append(("", e))
    y = corte + 46
    for etiqueta, valor in filas[:4]:
        _texto(page, F["sb"], 56, y, etiqueta.upper(), 7.5, ROJO)
        yy = y + 15
        valor = valor[:1].upper() + valor[1:]
        for ln in _envolver(F["md"], valor, 11.5, 480)[:3]:
            _texto(page, F["md"], 56, yy, ln, 11.5, NEGRO)
            yy += 15
        y = yy + 12

    # Banda inferior
    page.draw_rect(fitz.Rect(0, H - 46, W, H), color=None, fill=_rgb(NEGRO))
    page.draw_rect(fitz.Rect(0, H - 46, 8, H), color=None, fill=_rgb(ROJO))
    _texto(page, F["sb"], 56, H - 19.5, PIE_PROGRAMA.upper(), 8, "#FFFFFF")
    _texto(page, F["md"], W - 56, H - 19.5, PIE_WEB, 9, "#FFFFFF", align="right")


def decorar_paginas(doc, titulo_corto, F, primera):
    fitz = fitz_mod
    logo = _logo_pdf(fitz, LOGO)
    total = doc.page_count - primera
    for idx in range(primera, doc.page_count):
        page = doc[idx]
        W, H = page.rect.width, page.rect.height
        n = idx - primera + 1

        # Cabecera
        page.show_pdf_page(fitz.Rect(M_IZQ, 30, M_IZQ + 137 * 0.62, 30 + 32 * 0.62), logo, 0)
        cab = titulo_corto.upper()
        while F["sb"].text_length(cab, fontsize=7) > 300 and len(cab) > 10:
            cab = cab[:-2]
        if cab != titulo_corto.upper():
            cab = cab.rstrip() + "…"
        _texto(page, F["sb"], W - M_DER, 46, cab, 7, GRIS, align="right")
        page.draw_line((M_IZQ, 62), (W - M_DER, 62), color=_rgb(LINEA), width=0.6)
        page.draw_rect(fitz.Rect(M_IZQ, 61, M_IZQ + 34, 63.2), color=None, fill=_rgb(ROJO))

        # Pie
        page.draw_line((M_IZQ, H - 50), (W - M_DER, H - 50), color=_rgb(LINEA), width=0.6)
        page.draw_rect(fitz.Rect(M_IZQ, H - 38, M_IZQ + 6, H - 32), color=None,
                       fill=_rgb(ROJO), radius=0.2)
        _texto(page, F["md"], M_IZQ + 11, H - 32.3, f"{PIE_WEB}  ·  {PIE_PROGRAMA}", 7.5, GRIS)
        tot = f" / {total:02d}"
        w_tot = F["md"].text_length(tot, fontsize=7.5)
        _texto(page, F["md"], W - M_DER, H - 32.3, tot, 7.5, GRIS, align="right")
        _texto(page, F["xb"], W - M_DER - w_tot, H - 32.3, f"{n:02d}", 9, ROJO, align="right")


fitz_mod = None

RE_ETIQUETA = re.compile(r"<(h2|pre|blockquote|table|tr)(\s|>)")


def _marcar_bloques(html, saltos=()):
    """Pone un id a cada bloque que hay que decorar: d<N>-<tipo>.
    Las filas de cabecera de tabla se marcan como `trh`. `saltos` es una lista
    de pares (id_tabla, pt) para empujar esas tablas a la página siguiente."""
    n = [0]
    en_thead = [False]

    def rep(m):
        tag = m.group(1)
        n[0] += 1
        tipo = "trh" if tag == "tr" and en_thead[0] else tag
        ident = f"d{n[0]}-{tipo}"
        return f'<{tag} id="{ident}"{m.group(2)}'

    out = []
    for trozo in re.split(r"(<thead>|</thead>)", html):
        if trozo == "<thead>":
            en_thead[0] = True
        elif trozo == "</thead>":
            en_thead[0] = False
        else:
            trozo = RE_ETIQUETA.sub(rep, trozo)
        out.append(trozo)
    html = "".join(out)
    # (page-break-before con tablas cuelga MuPDF: se empuja con margen superior)
    for ident, empuje in dict(saltos).items():
        html = html.replace(f'<table id="{ident}">',
                            f'<table id="{ident}" style="margin-top: {empuje:.1f}pt">')
    return html


def maquetar(cuerpo_md, archivo, saltos=()):
    """Maqueta el Markdown con fitz.Story (lo mismo que hace markdown-pdf) y
    devuelve el documento, la posición de cada bloque decorable y los H2."""
    import io
    from markdown_it import MarkdownIt
    fitz = fitz_mod

    html = MarkdownIt("commonmark").enable("table").render(cuerpo_md)
    html = _marcar_bloques(html, saltos)
    story = fitz.Story(html=html, archive=archivo, user_css=CSS)

    pagina = fitz.paper_rect("a4")
    zona = pagina + (M_IZQ, M_SUP, -M_DER, -M_INF)
    buf = io.BytesIO()
    writer = fitz.DocumentWriter(buf)
    estado = {"pag": 0}
    bloques, marcadores, enlaces = {}, [], []

    def registrar(e):
        e.page_num = estado["pag"] + 1
        enlaces.append(e)
        if e.id and e.id.startswith("d"):
            clave = (estado["pag"], e.id)
            r = fitz.Rect(e.rect)
            bloques[clave] = bloques[clave] | r if clave in bloques else r
        if (e.open_close & 1) and e.heading == 2:
            marcadores.append((e.text, estado["pag"]))

    mas = 1
    while mas and estado["pag"] < 400:  # tope de seguridad
        dev = writer.begin_page(pagina)
        mas, _ = story.place(zona)
        story.element_positions(registrar)
        story.draw(dev)
        writer.end_page()
        estado["pag"] += 1
    writer.close()
    buf.seek(0)
    doc = fitz.Story.add_pdf_links(buf, enlaces)
    _verificar_texto(html, doc)
    return doc, bloques, marcadores, zona


def tablas_huerfanas(bloques, zona):
    """Tablas cuya fila de cabecera queda sola al pie de una página."""
    num = lambda ident: int(ident[1:].split("-", 1)[0])
    por_pag = {}
    for (pag, ident), r in bloques.items():
        fuera = r.y0 >= zona.y1 - 1 or r.y1 > zona.y1 + 2
        if fuera and not ident.endswith("-table"):
            continue  # MuPDF también informa de filas que ya no caben en esta página
        por_pag.setdefault(pag, []).append(ident)
    huerfanas = {}
    for pag, ids in por_pag.items():
        tablas = sorted((i for i in ids if i.endswith("-table")), key=num)
        for trh in (i for i in ids if i.endswith("-trh")):
            n = num(trh)
            hay_filas = any(i.endswith("-tr") and num(i) > n for i in ids)
            if not hay_filas:
                previas = [t for t in tablas if num(t) < n]
                if previas:
                    y0 = bloques[(pag, previas[-1])].y0
                    huerfanas[previas[-1]] = zona.y1 - y0 + 12
    return huerfanas


def _verificar_texto(html, doc):
    """Avisa si el PDF tiene bastante menos texto que el Markdown (bug de MuPDF)."""
    import html as html_mod
    plano = html_mod.unescape(re.sub(r"<[^>]+>", "", html))
    esperado = len(re.sub(r"\s+", "", plano))
    obtenido = len(re.sub(r"\s+", "", "".join(p.get_text() for p in doc)))
    if esperado and obtenido < esperado * 0.97:
        print(f"AVISO: el PDF parece haber perdido texto ({obtenido}/{esperado} caracteres). "
              "Revisa el PDF y, si falta contenido, simplifica la tabla o bloque que "
              "cae justo en el salto de página.", file=sys.stderr)


def _fin_continuacion(page, zona, x0, tipo):
    """Cuando un <pre>/<blockquote> salta de página, MuPDF no informa de su
    trozo en la página nueva. Lo deducimos del texto: líneas en mono (código)
    o en cursiva (cita) desde arriba del todo. Devuelve el y final o None."""
    fin = None
    lineas = []
    for b in page.get_text("dict")["blocks"]:
        for l in b.get("lines", []):
            if l["bbox"][1] >= zona.y0 - 2 and l["bbox"][3] <= zona.y1 + 2 and l["spans"]:
                lineas.append(l)
    lineas.sort(key=lambda l: l["bbox"][1])
    for l in lineas:
        spans = [sp for sp in l["spans"] if sp["text"].strip()]
        if not spans:
            continue
        if l["bbox"][0] < x0 - 1.5:
            break
        if tipo == "pre":
            ok = all("Mono" in sp["font"] for sp in spans)
        else:
            ok = all("Italic" in sp["font"] or "Mono" in sp["font"] or sp["flags"] & 2
                     for sp in spans)
        if not ok:
            break
        fin = l["bbox"][3]
    return fin


def decorar_bloques(doc, bloques, zona):
    """Dibuja por debajo del texto los fondos y filetes que el CSS no puede pintar."""
    fitz = fitz_mod
    bloques = dict(bloques)
    for (pag, ident), r in list(bloques.items()):
        tipo = ident.split("-", 1)[1]
        if tipo not in ("pre", "blockquote") or r.y1 < zona.y1 - 14:
            continue
        sig = pag + 1
        while sig < doc.page_count:
            fin = _fin_continuacion(doc[sig], zona, r.x0, tipo)
            if fin is None:
                break
            bloques[(sig, ident)] = fitz.Rect(r.x0, zona.y0 + 2, r.x1, fin)
            if fin < zona.y1 - 14:
                break
            sig += 1
    filas_tabla = {}
    for (pag, ident), r in sorted(bloques.items(), key=lambda kv: (kv[0][0], kv[1].y0)):
        if r.y0 >= zona.y1 - 1 or r.y1 > zona.y1 + 2:
            continue  # filas que MuPDF ya ha mandado a la página siguiente
        page = doc[pag]
        tipo = ident.split("-", 1)[1]
        if tipo == "h2":
            y = r.y1 + 5
            page.draw_rect(fitz.Rect(zona.x0, y, zona.x1, y + 1.5), color=None,
                           fill=_rgb(ROJO), overlay=False)
        elif tipo == "pre":
            # MuPDF da la caja de contenido; el fondo se extiende sobre el margen del CSS
            caja = fitz.Rect(r.x0 - 16, r.y0 - 10, r.x1 + 13, r.y1 + 10)
            page.draw_rect(caja, color=None, fill=_rgb("#141414"), overlay=False)
            page.draw_rect(fitz.Rect(caja.x0, caja.y0, caja.x0 + 3.5, caja.y1), color=None,
                           fill=_rgb(ROJO))
        elif tipo == "blockquote":
            caja = fitz.Rect(r.x0 - 16, r.y0 - 8, r.x1 + 13, r.y1 + 8)
            page.draw_rect(caja, color=None, fill=_rgb(CREMA), overlay=False)
            page.draw_rect(fitz.Rect(caja.x0, caja.y0, caja.x0 + 3.5, caja.y1), color=None,
                           fill=_rgb(ROJO))
        elif tipo == "trh":
            page.draw_rect(r, color=None, fill=_rgb(NEGRO), overlay=False)
            filas_tabla[pag] = 0
        elif tipo == "tr":
            i = filas_tabla.get(pag, 0) + 1
            filas_tabla[pag] = i
            if i % 2 == 0:
                page.draw_rect(r, color=None, fill=_rgb(CREMA), overlay=False)
            page.draw_line((r.x0, r.y1), (r.x1, r.y1), color=_rgb(LINEA), width=0.6)
        elif tipo == "table":
            filas_tabla[pag] = 0
            page.draw_line((r.x0, r.y1 - 0.3), (r.x1, r.y1 - 0.3), color=_rgb(NEGRO), width=0.9)


def main():
    global fitz_mod
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("md", help="Ruta al .md")
    p.add_argument("--out", help="Ruta de salida .pdf")
    p.add_argument("--toc", action="store_true",
                   help="Añade marcadores navegables al PDF (basados en encabezados H2)")
    p.add_argument("--sin-portada", action="store_true",
                   help="No genera portada; el H1 se mantiene al inicio del cuerpo")
    args = p.parse_args()

    md_path = Path(args.md)
    if not md_path.exists():
        print(f"ERROR: no existe {md_path}", file=sys.stderr)
        sys.exit(1)
    if md_path.suffix.lower() != ".md":
        print(f"ERROR: se esperaba un .md ({md_path})", file=sys.stderr)
        sys.exit(1)

    try:
        import markdown_pdf  # noqa: F401  (trae markdown-it-py y PyMuPDF)
        import pymupdf as fitz
    except ImportError:
        print("ERROR: falta la librería `markdown-pdf`.\n"
              "       Instálala con:  pip install markdown-pdf", file=sys.stderr)
        sys.exit(3)
    fitz_mod = fitz

    faltan = [f for f in (LOGO, LOGO_BLANCO, FONTS / "InterTight-Regular.ttf") if not f.exists()]
    if faltan:
        print("ERROR: faltan recursos de marca en la skill:\n  " +
              "\n  ".join(str(f) for f in faltan), file=sys.stderr)
        sys.exit(2)

    md_text = md_path.read_text(encoding="utf-8")
    out_path = Path(args.out) if args.out else md_path.with_suffix(".pdf")

    portada, cuerpo = (None, md_text) if args.sin_portada else extraer_portada(md_text)
    cuerpo = preprocesar(cuerpo)

    archivo = fitz.Archive()
    archivo.add(str(FONTS))
    archivo.add(str(md_path.resolve().parent))  # imágenes relativas del .md

    try:
        saltos = {}
        for _ in range(4):  # si una tabla deja su cabecera sola, se pasa a la página siguiente
            doc, bloques, marcadores, zona = maquetar(cuerpo, archivo, tuple(saltos.items()))
            nuevas = {k: v for k, v in tablas_huerfanas(bloques, zona).items() if k not in saltos}
            if not nuevas:
                break
            saltos.update(nuevas)
        decorar_bloques(doc, bloques, zona)
        doc.set_metadata({
            "title": portada["h1"] if portada else md_path.stem,
            "author": "The Bridge", "subject": PIE_PROGRAMA,
            "creator": "apuntes-clase-vtt", "producer": "markdown-pdf / PyMuPDF",
        })
        F = _fuentes(fitz)
        primera = 0
        if portada:
            dibujar_portada(doc, portada, F)
            primera = 1
        if args.toc and marcadores:
            toc = [[1, _limpiar_titulo(re.sub(r"\s{2,}", " ", t)), pg + 1 + primera]
                   for t, pg in marcadores]
            if portada:
                toc.insert(0, [1, "Portada", 1])
            doc.set_toc(toc)
        titulo_corto = portada["eyebrow"] if portada else md_path.stem
        decorar_paginas(doc, titulo_corto, F, primera)
        doc.save(str(out_path), garbage=3, deflate=True)
    except Exception as e:
        print(f"ERROR: la generación del PDF ha fallado: {e}", file=sys.stderr)
        sys.exit(4)

    print(f"OK: {out_path}")


if __name__ == "__main__":
    main()
