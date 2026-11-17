#!/usr/bin/env python3
"""Guarda del plugin aie-equipo.

Se ejecuta antes de cada uso de Bash, Read, Edit o Write en Claude Code:
- Bloquea leer, editar o mostrar ficheros .env.
- Pide confirmación antes de un push directo a main o develop.
- Pide confirmación antes de abrir una PR a main desde una rama que no sea develop.
- Pide confirmación antes de un push forzado.

Si algo falla al leer la entrada, no bloquea nada.
"""
import json
import re
import sys


def responder(decision, motivo):
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": decision,
            "permissionDecisionReason": motivo,
        }
    }, ensure_ascii=False))
    sys.exit(0)


ENV = re.compile(r"(^|[\s/'\"=])\.env(\.[A-Za-z0-9_-]+)?($|[\s'\";|&)])")
ENV_PERMITIDO = re.compile(r"\.env\.(example|ejemplo|sample)\b")


def es_env(ruta):
    nombre = ruta.rstrip("/").split("/")[-1]
    if re.fullmatch(r"\.env\.(example|ejemplo|sample)", nombre):
        return False
    return re.fullmatch(r"\.env(\.[A-Za-z0-9_-]+)?", nombre) is not None


def revisar_bash(cmd):
    sin_permitidos = ENV_PERMITIDO.sub("", cmd)
    if ENV.search(sin_permitidos) and re.search(r"\b(cat|less|more|head|tail|bat|grep|sed|awk|cp|mv|nano|vim?|code|open|source|export|echo|printenv)\b", sin_permitidos):
        responder("deny", "Norma del equipo: no se leen ni se muestran ficheros .env. Las claves se cargan con python-dotenv sin imprimirlas.")
    if re.search(r"\bgit\s+push\b", cmd):
        if re.search(r"(\s--force\b|\s-f\b|--force-with-lease)", cmd):
            responder("ask", "Push forzado: confirma que es lo que quieres.")
        if re.search(r"\b(origin|upstream)\s+(HEAD:)?(main|develop)\b", cmd) or re.search(r":(main|develop)\b", cmd):
            responder("ask", "Push directo a main o develop. Lo normal es una rama de trabajo y una PR. Confirma si es intencionado.")
    if re.search(r"\bgh\s+pr\s+create\b", cmd):
        base = re.search(r"(--base|-B)[=\s]+(\S+)", cmd)
        head = re.search(r"(--head|-H)[=\s]+(\S+)", cmd)
        if base and base.group(2).strip("'\"") == "main":
            if not head or head.group(2).strip("'\"") != "develop":
                responder("ask", "Las PR a main solo pueden venir de develop. Revisa la rama de origen.")


def main():
    try:
        datos = json.load(sys.stdin)
    except Exception:
        sys.exit(0)
    herramienta = datos.get("tool_name", "")
    entrada = datos.get("tool_input", {}) or {}
    if herramienta in ("Read", "Edit", "Write"):
        ruta = entrada.get("file_path", "") or ""
        if es_env(ruta):
            responder("deny", "Norma del equipo: no se leen ni se editan ficheros .env con Claude.")
    elif herramienta == "Bash":
        revisar_bash(entrada.get("command", "") or "")
    sys.exit(0)


if __name__ == "__main__":
    main()
