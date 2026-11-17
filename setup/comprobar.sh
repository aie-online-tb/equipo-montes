#!/usr/bin/env bash
# Comprueba la puesta en marcha. Solo lee: no instala ni cambia nada.
set -u

RAIZ="$(cd "$(dirname "$0")/.." && pwd)"
cd "${RAIZ}"
fallos=0

bien() { echo "  ✓ $1"; }
mal()  { echo "  ✗ $1"; echo "    → $2"; fallos=$((fallos + 1)); }
info() { echo "  · $1"; }

echo "Equipo Montes · comprobación de la puesta en marcha"
echo

echo "Herramientas"
for c in git python3 claude; do
  if command -v "$c" >/dev/null 2>&1; then bien "$c"; else mal "Falta $c" "Instálalo y repite"; fi
done

echo
echo "Repo"
url="$(git remote get-url origin 2>/dev/null || true)"
case "$url" in
  *aie-online-tb/equipo-montes*) bien "Clon de aie-online-tb/equipo-montes" ;;
  *) mal "Esta carpeta no es un clon de equipo-montes" "Clónalo con el paso 1 de setup/README.md" ;;
esac
rama="$(git branch --show-current)"
info "Rama actual: ${rama}"
if git fetch -q origin "${rama}" 2>/dev/null; then
  atras="$(git rev-list --count "HEAD..origin/${rama}" 2>/dev/null || echo 0)"
  if [ "${atras}" = "0" ]; then bien "Al día con origin/${rama}"; else mal "${atras} commits por detrás de origin/${rama}" "git pull"; fi
else
  info "No he podido consultar GitHub; no compruebo si estás al día"
fi
if git ls-files | grep -qE '(^|/)\.env$'; then
  mal "Hay un .env en el repo" "Sácalo del repo y rota las claves que tuviera"
else
  bien "Sin .env en el repo"
fi

echo
echo "Plugin"
if command -v claude >/dev/null 2>&1; then
  if claude plugin marketplace list 2>/dev/null | grep -q "equipo-montes"; then
    bien "Marketplace equipo-montes añadido"
  else
    mal "Falta el marketplace equipo-montes" "bash setup/instalar.sh"
  fi
  instalados="$(claude plugin list 2>/dev/null || true)"
  if echo "${instalados}" | grep -q "aie-equipo"; then
    bien "Plugin aie-equipo instalado"
    esperada="$(python3 -c 'import json;print(json.load(open("plugins/aie-equipo/.claude-plugin/plugin.json"))["version"])')"
    if echo "${instalados}" | grep -A3 "aie-equipo" | grep -q "${esperada}"; then
      bien "Versión ${esperada}, la de esta rama"
    else
      info "No he podido confirmar que la versión instalada sea la ${esperada}; si dudas, bash setup/instalar.sh"
    fi
  else
    mal "Falta el plugin aie-equipo" "bash setup/instalar.sh"
  fi
fi

echo
echo "Guardas"
salida="$(echo '{"tool_name":"Read","tool_input":{"file_path":"/tmp/prueba/.env"}}' | python3 plugins/aie-equipo/scripts/guarda.py 2>/dev/null || true)"
if echo "${salida}" | grep -q '"deny"'; then
  bien "La guarda bloquea leer un .env"
else
  mal "La guarda no bloquea leer un .env" "Revisa plugins/aie-equipo/scripts/guarda.py"
fi

echo
if [ "${fallos}" -eq 0 ]; then
  echo "Todo bien. Sigue con el paso 4 de setup/README.md (conectores)."
else
  echo "${fallos} cosas por arreglar. Arréglalas y vuelve a ejecutar este script."
  exit 1
fi
