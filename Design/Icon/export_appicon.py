#!/usr/bin/env python3
"""Export the chosen concept (21) as the three iOS 18+ icon appearances.

- default: the icon as designed, opaque dark ground
- dark:    the glyph alone on a transparent ground; iOS supplies its own dark
           gradient behind it, so an opaque near-black square would look like
           a hole in the grid
- tinted:  the glyph in greyscale on transparent; iOS colours it with the
           user's tint, so colour information is discarded on purpose
"""
import re
from pathlib import Path
import cairosvg
from PIL import Image, ImageOps

ROOT = Path(__file__).parent
SRC = ROOT / "svg" / "21-mug-overflow.svg"
OUT = ROOT / "appicon"
OUT.mkdir(exist_ok=True)

svg = SRC.read_text()
# strip the Background layer for the transparent variants
glyph_only = re.sub(r'<g id="Background">.*?</g>', "", svg, flags=re.S)


def render(text, name):
    path = OUT / name
    cairosvg.svg2png(bytestring=text.encode(), write_to=str(path), output_width=1024, output_height=1024)
    return path


render(svg, "AppIcon-Default.png")
render(glyph_only, "AppIcon-Dark.png")

tinted = Image.open(render(glyph_only, "AppIcon-Tinted.png")).convert("RGBA")
alpha = tinted.getchannel("A")
grey = ImageOps.grayscale(tinted.convert("RGB"))
# lift the mid-tones so the curve stays visible once the system tints it
grey = grey.point(lambda v: min(255, int(v * 1.25)))
Image.merge("RGBA", (grey, grey, grey, alpha)).save(OUT / "AppIcon-Tinted.png")

# the default image must be fully opaque — App Store Connect rejects alpha
default = Image.open(OUT / "AppIcon-Default.png").convert("RGB")
default.save(OUT / "AppIcon-Default.png")
print("exported", sorted(p.name for p in OUT.iterdir()))
