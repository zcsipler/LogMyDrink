#!/usr/bin/env python3
"""Render the SVG concepts to PNG and build a contact sheet at iOS sizes."""
from pathlib import Path
import cairosvg
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).parent
SVG = ROOT / "svg"
PNG = ROOT / "png"
PNG.mkdir(exist_ok=True)


def rounded(img, radius_frac=0.2237):
    """Approximate the iOS icon mask (continuous corner ~22.37 % of the side)."""
    w, h = img.size
    r = int(w * radius_frac)
    mask = Image.new("L", (w * 4, h * 4), 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, w * 4 - 1, h * 4 - 1), radius=r * 4, fill=255)
    mask = mask.resize((w, h), Image.LANCZOS)
    out = img.copy().convert("RGBA")
    out.putalpha(mask)
    return out


import sys
# Optional glob prefix (e.g. "1" for round 2) selects which concepts go on the sheet.
prefix = sys.argv[1] if len(sys.argv) > 1 else ""
sheet_name = f"contact-sheet{'-' + prefix if prefix else ''}.png"

icons = []
for svg in sorted(SVG.glob(f"{prefix}*.svg")):
    out = PNG / (svg.stem + ".png")
    cairosvg.svg2png(url=str(svg), write_to=str(out), output_width=1024, output_height=1024)
    icons.append((svg.stem, Image.open(out).convert("RGBA")))

# Contact sheet: wallpaper-ish grey ground, one row per concept, three sizes.
sizes = [180, 120, 60]
pad = 48
row_h = 260
sheet = Image.new("RGBA", (pad * 2 + 180 + 60 + sum(sizes) + 48 * (len(sizes) - 1), pad * 2 + row_h * len(icons)), (232, 234, 238, 255))
d = ImageDraw.Draw(sheet)
try:
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 22)
except OSError:
    font = ImageFont.load_default()

for i, (name, img) in enumerate(icons):
    y = pad + i * row_h
    x = pad
    for s in sizes:
        tile = rounded(img.resize((s, s), Image.LANCZOS))
        sheet.alpha_composite(tile, (x, y + (180 - s) // 2))
        x += s + 48
    d.text((x + 10, y + 70), name, fill=(40, 44, 52, 255), font=font)

sheet.save(PNG / sheet_name)
print("rendered", len(icons), "icons")
