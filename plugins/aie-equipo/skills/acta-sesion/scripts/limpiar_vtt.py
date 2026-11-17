#!/usr/bin/env python3
"""Parsea un archivo .vtt (WebVTT) y produce un texto limpio por tramos
de minuto, con el formato:

    [HH:MM] Hablante: texto consolidado del minuto

- Lee en UTF-8.
- Normaliza nombres de hablante (quita prefijos tipo "Audio shared by ").
- Agrupa cues contiguos del mismo hablante dentro del mismo minuto.
- No ejecuta nada ni toca el archivo original.

Uso:
    python limpiar_vtt.py <archivo.vtt> [--out <archivo.txt>]
    python limpiar_vtt.py <archivo.vtt> --stdout
"""
import argparse
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

TS_RE = re.compile(
    r"^(\d{2}):(\d{2}):(\d{2})\.\d{3}\s*-->\s*(\d{2}):(\d{2}):(\d{2})\.\d{3}"
)
SPEAKER_RE = re.compile(r"^(?P<speaker>[^:]{1,60}):\s*(?P<text>.*)$")


def norm_speaker(name: str) -> str:
    name = name.strip()
    name = re.sub(r"^Audio shared by\s+", "", name, flags=re.IGNORECASE)
    name = re.sub(r"^Video shared by\s+", "", name, flags=re.IGNORECASE)
    return name.strip()


def parse_vtt(path: Path):
    """Yield (start_seconds, speaker, text) tuples."""
    text = path.read_text(encoding="utf-8", errors="replace")
    # Normaliza finales de línea
    lines = text.replace("\r\n", "\n").split("\n")
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        m = TS_RE.match(line)
        if not m:
            i += 1
            continue
        h, mn, s = int(m.group(1)), int(m.group(2)), int(m.group(3))
        start = h * 3600 + mn * 60 + s
        # Lee el bloque de texto hasta línea vacía
        i += 1
        buf = []
        while i < len(lines) and lines[i].strip() != "":
            buf.append(lines[i].strip())
            i += 1
        if not buf:
            continue
        raw = " ".join(buf).strip()
        sp_match = SPEAKER_RE.match(raw)
        if sp_match:
            speaker = norm_speaker(sp_match.group("speaker"))
            content = sp_match.group("text").strip()
        else:
            speaker = ""
            content = raw
        if content:
            yield start, speaker, content


def group_by_minute(cues):
    """Agrupa cues contiguos por (minuto, hablante)."""
    current = None  # dict con minute, speaker, parts
    for start, speaker, content in cues:
        minute = start // 60
        if current is None or current["minute"] != minute or current["speaker"] != speaker:
            if current is not None:
                yield current
            current = {"minute": minute, "speaker": speaker, "parts": [content]}
        else:
            current["parts"].append(content)
    if current is not None:
        yield current


def format_minute_block(block) -> str:
    minute = block["minute"]
    hh = minute // 60
    mm = minute % 60
    ts = f"{hh:02d}:{mm:02d}"
    speaker = block["speaker"] or "¿?"
    text = " ".join(block["parts"]).strip()
    text = re.sub(r"\s+", " ", text)
    return f"[{ts}] {speaker}: {text}"


def speaker_stats(cues_list):
    counts = {}
    for _, speaker, _ in cues_list:
        if not speaker:
            continue
        counts[speaker] = counts.get(speaker, 0) + 1
    return sorted(counts.items(), key=lambda x: -x[1])


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("vtt", help="Ruta al archivo .vtt")
    g = p.add_mutually_exclusive_group()
    g.add_argument("--out", help="Ruta de salida .txt (por defecto: stdout)")
    g.add_argument("--stdout", action="store_true", help="Imprime a stdout")
    p.add_argument(
        "--stats",
        action="store_true",
        help="Añade al final un bloque con el conteo de intervenciones por hablante",
    )
    args = p.parse_args()

    vtt_path = Path(args.vtt)
    if not vtt_path.exists():
        print(f"ERROR: no existe el archivo {vtt_path}", file=sys.stderr)
        sys.exit(1)
    if vtt_path.suffix.lower() != ".vtt":
        print(f"AVISO: el archivo no termina en .vtt ({vtt_path.suffix})", file=sys.stderr)

    cues = list(parse_vtt(vtt_path))
    if not cues:
        print("ERROR: no se han encontrado cues en el VTT. ¿Está vacío o mal formado?", file=sys.stderr)
        sys.exit(2)

    blocks = list(group_by_minute(cues))
    out_lines = [format_minute_block(b) for b in blocks]

    header = [
        f"# Transcripción limpia de {vtt_path.name}",
        f"# cues: {len(cues)} · bloques por minuto: {len(blocks)}",
        "",
    ]

    body = "\n".join(header + out_lines)

    if args.stats:
        body += "\n\n# Hablantes (intervenciones):\n"
        for sp, n in speaker_stats(cues):
            body += f"#   {sp}: {n}\n"

    if args.out:
        out_path = Path(args.out)
        out_path.write_text(body, encoding="utf-8")
        print(f"OK: escrito {out_path}")
    else:
        print(body)


if __name__ == "__main__":
    main()
