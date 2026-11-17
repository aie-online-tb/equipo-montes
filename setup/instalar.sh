#!/usr/bin/env bash
# Instala o actualiza el plugin aie-equipo desde esta copia del repo.
# Se puede ejecutar varias veces: si ya está instalado, lo actualiza.
set -euo pipefail

RAIZ="$(cd "$(dirname "$0")/.." && pwd)"
MARKETPLACE="equipo-montes"
PLUGIN="aie-equipo@${MARKETPLACE}"

if ! command -v claude >/dev/null 2>&1; then
  echo "Falta Claude Code. Instálalo y vuelve a ejecutar este script." >&2
  exit 1
fi

echo "Repo: ${RAIZ} (rama $(git -C "${RAIZ}" branch --show-current))"

if claude plugin marketplace list 2>/dev/null | grep -q "${MARKETPLACE}"; then
  echo "Actualizando el marketplace ${MARKETPLACE}…"
  claude plugin marketplace update "${MARKETPLACE}"
else
  echo "Añadiendo el marketplace ${MARKETPLACE} desde esta carpeta…"
  claude plugin marketplace add "${RAIZ}"
fi

if claude plugin list 2>/dev/null | grep -q "aie-equipo"; then
  echo "Actualizando el plugin…"
  claude plugin update "${PLUGIN}"
else
  echo "Instalando el plugin…"
  claude plugin install "${PLUGIN}"
fi

echo
echo "Hecho. Reinicia Claude Code y ejecuta: bash setup/comprobar.sh"
