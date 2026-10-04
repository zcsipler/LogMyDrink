#!/usr/bin/env python3
"""Generate the LogMyDrink app-icon concepts as 1024x1024 SVGs.

Colours come from Theme.swift so the icon speaks the app's own language:
dark ground, and a curve coloured by level (teal -> amber -> coral -> red).
Every concept is built on the same BAC curve so they can be compared on
motif alone.
"""
import math
from pathlib import Path

OUT = Path(__file__).parent / "svg"
OUT.mkdir(exist_ok=True)

S = 1024
BG = "#0B0D12"        # Theme.background
SURF = "#161925"      # Theme.surface
RAISED = "#21252F"    # Theme.surfaceRaised
TEXT = "#EFF1F5"      # Theme.primaryText
TEAL = "#45BFB4"      # calm
AMBER = "#F2B64F"     # caution
CORAL = "#EF6D65"     # elevated
RED = "#EC2D32"       # alarm


def bac(x, k=9.0, b=1.0):
    """One-compartment shape: first-order rise, near-linear fall."""
    return max(0.0, (1 - math.exp(-k * x)) - b * x)


def curve_points(x0, x1, y_base, height, b=1.0, n=120, xmax=1.0):
    """Points of the curve mapped into a box, peak normalised to `height`."""
    peak = max(bac(i / 400, b=b) for i in range(401))
    pts = []
    for i in range(n + 1):
        u = i / n
        y = bac(u * xmax, b=b) / peak
        pts.append((x0 + (x1 - x0) * u, y_base - height * y))
    return pts


def path_from(pts, close_to_base=None):
    d = "M %.1f %.1f " % pts[0] + " ".join("L %.1f %.1f" % p for p in pts[1:])
    if close_to_base is not None:
        d += " L %.1f %.1f L %.1f %.1f Z" % (pts[-1][0], close_to_base, pts[0][0], close_to_base)
    return d


def band_path(upper, lower):
    d = "M %.1f %.1f " % upper[0] + " ".join("L %.1f %.1f" % p for p in upper[1:])
    d += " " + " ".join("L %.1f %.1f" % p for p in reversed(lower)) + " Z"
    return d


def level_gradient(gid, y_top, y_bottom):
    """Vertical gradient, calm at the base to alarm at the top — Theme's ramp."""
    return f"""
  <linearGradient id="{gid}" gradientUnits="userSpaceOnUse" x1="0" y1="{y_bottom}" x2="0" y2="{y_top}">
    <stop offset="0" stop-color="{TEAL}"/>
    <stop offset="0.55" stop-color="{AMBER}"/>
    <stop offset="0.85" stop-color="{CORAL}"/>
    <stop offset="1" stop-color="{RED}"/>
  </linearGradient>"""


def background():
    return f"""
  <g id="Background"><rect width="{S}" height="{S}" fill="url(#bg)"/></g>"""


BG_DEFS = f"""
  <radialGradient id="bg" cx="0.5" cy="0.2" r="0.9">
    <stop offset="0" stop-color="{RAISED}"/>
    <stop offset="1" stop-color="{BG}"/>
  </radialGradient>"""


def svg(name, body, defs=""):
    doc = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {S} {S}" width="{S}" height="{S}">
  <defs>{BG_DEFS}{defs}</defs>{body}
</svg>
"""
    (OUT / f"{name}.svg").write_text(doc)


# ---------------------------------------------------------------- 1. The band
def concept_band():
    x0, x1 = 150, 900
    base = 735
    h = 420
    upper = curve_points(x0, x1, base, h, b=0.72)
    lower = curve_points(x0, x1, base, h, b=1.40)
    top = min(p[1] for p in upper)
    defs = level_gradient("lvl", top, base) + f"""
  <linearGradient id="bandfill" gradientUnits="userSpaceOnUse" x1="0" y1="{base}" x2="0" y2="{top}">
    <stop offset="0" stop-color="{TEAL}" stop-opacity="0.75"/>
    <stop offset="0.55" stop-color="{AMBER}" stop-opacity="0.75"/>
    <stop offset="0.85" stop-color="{CORAL}" stop-opacity="0.8"/>
    <stop offset="1" stop-color="{RED}" stop-opacity="0.85"/>
  </linearGradient>"""
    body = background() + f"""
  <g id="Band">
    <path d="{band_path(upper, lower)}" fill="url(#bandfill)"/>
    <path d="{path_from(upper)}" fill="none" stroke="url(#lvl)" stroke-width="26" stroke-linecap="round" stroke-linejoin="round"/>
    <path d="{path_from(lower)}" fill="none" stroke="url(#lvl)" stroke-width="26" stroke-linecap="round" stroke-linejoin="round" opacity="0.9"/>
  </g>
  <g id="Baseline">
    <line x1="{x0}" y1="{base}" x2="{x1}" y2="{base}" stroke="{TEXT}" stroke-opacity="0.22" stroke-width="14" stroke-linecap="round"/>
  </g>"""
    svg("01-band", body, defs)


# ------------------------------------------------- 2. Curve inside a glass
def concept_glass_chart():
    gx0, gx1 = 262, 762           # rim
    bx0, bx1 = 300, 724           # foot
    gy0, gy1 = 180, 850
    glass = (f"M {gx0} {gy0} L {bx0} {gy1-40} Q {bx0} {gy1} {bx0+40} {gy1} "
             f"L {bx1-40} {gy1} Q {bx1} {gy1} {bx1} {gy1-40} L {gx1} {gy0} Z")
    base = 790
    h = 470
    pts = curve_points(gx0 + 30, gx1 - 30, base, h)
    top = min(p[1] for p in pts)
    defs = level_gradient("lvl", top, base) + f"""
  <clipPath id="glassclip"><path d="{glass}"/></clipPath>
  <linearGradient id="fill" gradientUnits="userSpaceOnUse" x1="0" y1="{base}" x2="0" y2="{top}">
    <stop offset="0" stop-color="{TEAL}" stop-opacity="0.45"/>
    <stop offset="0.55" stop-color="{AMBER}" stop-opacity="0.45"/>
    <stop offset="1" stop-color="{RED}" stop-opacity="0.55"/>
  </linearGradient>"""
    body = background() + f"""
  <g id="Glass">
    <path d="{glass}" fill="{SURF}" stroke="{TEXT}" stroke-width="30" stroke-linejoin="round"/>
  </g>
  <g id="Curve" clip-path="url(#glassclip)">
    <path d="{path_from(pts, close_to_base=gy1)}" fill="url(#fill)"/>
    <path d="{path_from(pts)}" fill="none" stroke="url(#lvl)" stroke-width="34" stroke-linecap="round" stroke-linejoin="round"/>
  </g>"""
    svg("02-glass-chart", body, defs)


# ---------------------------------------------- 3. Glass + the log gesture
def concept_glass_plus():
    gx0, gx1 = 290, 700
    bx0, bx1 = 330, 660
    gy0, gy1 = 190, 830
    glass = (f"M {gx0} {gy0} L {bx0} {gy1-44} Q {bx0} {gy1} {bx0+44} {gy1} "
             f"L {bx1-44} {gy1} Q {bx1} {gy1} {bx1} {gy1-44} L {gx1} {gy0} Z")
    liquid = (f"M {gx0+26} 470 Q 495 430 {gx1-26} 470 L {bx1-10} {gy1-44} "
              f"Q {bx1-10} {gy1-14} {bx1-44} {gy1-14} L {bx0+44} {gy1-14} "
              f"Q {bx0+10} {gy1-14} {bx0+10} {gy1-44} Z")
    cx, cy, r = 752, 300, 150
    body = background() + f"""
  <g id="Glass">
    <path d="{liquid}" fill="{TEAL}"/>
    <path d="{glass}" fill="none" stroke="{TEXT}" stroke-width="34" stroke-linejoin="round"/>
  </g>
  <g id="Plus">
    <circle cx="{cx}" cy="{cy}" r="{r+22}" fill="{BG}"/>
    <circle cx="{cx}" cy="{cy}" r="{r}" fill="{AMBER}"/>
    <path d="M {cx-72} {cy} H {cx+72} M {cx} {cy-72} V {cy+72}" stroke="{BG}" stroke-width="40" stroke-linecap="round"/>
  </g>"""
    svg("03-glass-plus", body)


# -------------------------------------------- 4. Monogram: the L is the axis
def concept_monogram():
    stem_x = 232
    foot_y = 760
    stem_w = 96
    foot_x1 = 820
    x0 = stem_x + stem_w
    base = foot_y - stem_w / 2
    pts = curve_points(x0 + 10, foot_x1 - 20, base, 440)
    top = min(p[1] for p in pts)
    defs = level_gradient("lvl", top, base)
    body = background() + f"""
  <g id="Letter">
    <path d="M {stem_x + stem_w/2} 230 V {foot_y - stem_w/2} H {foot_x1}" fill="none" stroke="{TEXT}" stroke-width="{stem_w}" stroke-linecap="round" stroke-linejoin="round"/>
  </g>
  <g id="Curve">
    <path d="{path_from(pts)}" fill="none" stroke="url(#lvl)" stroke-width="54" stroke-linecap="round" stroke-linejoin="round"/>
  </g>"""
    svg("04-monogram", body, defs)


# ------------------------------------------- 5. Three lines: the band as strokes
def concept_three_lines():
    x0, x1 = 160, 900
    base = 740
    h = 450
    slow = curve_points(x0, x1, base, h, b=0.78)
    mid = curve_points(x0, x1, base, h * 0.92, b=1.0)
    fast = curve_points(x0, x1, base, h * 0.84, b=1.25)
    body = background() + f"""
  <g id="Lines" fill="none" stroke-width="44" stroke-linecap="round" stroke-linejoin="round">
    <path d="{path_from(slow)}" stroke="{CORAL}"/>
    <path d="{path_from(mid)}" stroke="{AMBER}"/>
    <path d="{path_from(fast)}" stroke="{TEAL}"/>
  </g>"""
    svg("05-three-lines", body)


# ------------------------------------ 6. The curve is the surface of the drink
def concept_liquid_curve():
    gx0, gx1 = 190, 834
    bx0, bx1 = 230, 794
    gy0, gy1 = 220, 820
    glass = (f"M {gx0} {gy0} L {bx0} {gy1-48} Q {bx0} {gy1} {bx0+48} {gy1} "
             f"L {bx1-48} {gy1} Q {bx1} {gy1} {bx1} {gy1-48} L {gx1} {gy0} Z")
    base = 700
    pts = curve_points(gx0 - 20, gx1 + 20, base, 360)
    top = min(p[1] for p in pts)
    defs = f"""
  <clipPath id="glassclip"><path d="{glass}"/></clipPath>
  <linearGradient id="liq" gradientUnits="userSpaceOnUse" x1="0" y1="{gy1}" x2="0" y2="{top}">
    <stop offset="0" stop-color="{TEAL}"/>
    <stop offset="0.6" stop-color="{AMBER}"/>
    <stop offset="0.86" stop-color="{CORAL}"/>
    <stop offset="1" stop-color="{RED}"/>
  </linearGradient>"""
    body = background() + f"""
  <g id="Liquid" clip-path="url(#glassclip)">
    <path d="{path_from(pts, close_to_base=gy1 + 10)}" fill="url(#liq)"/>
    <path d="{path_from(pts)}" fill="none" stroke="{TEXT}" stroke-opacity="0.55" stroke-width="14" stroke-linecap="round"/>
  </g>
  <g id="Glass">
    <path d="{glass}" fill="none" stroke="{TEXT}" stroke-width="34" stroke-linejoin="round"/>
  </g>"""
    svg("06-liquid-curve", body, defs)


if __name__ == "__main__":
    concept_band()
    concept_glass_chart()
    concept_glass_plus()
    concept_monogram()
    concept_three_lines()
    concept_liquid_curve()
    print("\n".join(sorted(p.name for p in OUT.glob("*.svg"))))
