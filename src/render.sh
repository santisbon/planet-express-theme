#!/bin/bash
# Regenerates the Planet Express wallpapers: gen.py (in the same folder as this
# script) writes each wallpaper as an SVG file, headless Chromium renders the SVG
# to PNG (ImageMagick's built-in SVG renderer drops gradients and clip paths),
# and ImageMagick converts the PNG to WebP in ../backgrounds/.
set -euo pipefail
src=$(cd "$(dirname "$0")" && pwd)
out="$src/../backgrounds"
work=$(mktemp -d)
trap 'rm -rf "$work"' EXIT

render() {
  local name="$1" target="$2"
  python3 -I "$src/gen.py" "$work/$name.svg"
  printf '<html><body style="margin:0;background:#0b0a11"><img src="%s.svg" width="5120" height="2880" style="display:block"></body></html>' "$name" > "$work/$name.html"
  chromium --headless=new --disable-gpu --no-sandbox --user-data-dir="$work/chromium" \
    --hide-scrollbars --force-device-scale-factor=1 --window-size=5120,2880 \
    --screenshot="$work/$name.png" "file://$work/$name.html"
  magick "$work/$name.png" -quality 92 "$out/$target"
}

render space 1-deep-space.webp
render grid 2-crt-grid.webp
