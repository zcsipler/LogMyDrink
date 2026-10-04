#!/usr/bin/env python3
"""Round 2: the drink has to be recognisably alcohol — a beer mug with a
handle, facets and a foam head, or a stemmed wine glass — and the BAC curve
lives inside or behind it. Reuses the curve and palette from make_icons.py."""
from make_icons import (
    S, BG, SURF, TEXT, TEAL, AMBER, CORAL, RED,
    curve_points, path_from, band_path, level_gradient, background, svg,
)

STROKE = 34


# ----------------------------------------------------------------- shapes
def beer_mug(cx=440):
    """A tapered stein: wider at the rim, rounded foot, a D handle on the
    right and three facet lines. Returns paths and the body box."""
    top, bottom = 250, 860
    tw, bw, r = 460, 400, 40          # rim width, foot width, corner radius
    x0t, x1t = cx - tw / 2, cx + tw / 2
    x0b, x1b = cx - bw / 2, cx + bw / 2
    body = (f"M {x0t} {top} H {x1t} L {x1b} {bottom - r} Q {x1b} {bottom} {x1b - r} {bottom} "
            f"H {x0b + r} Q {x0b} {bottom} {x0b} {bottom - r} Z")
    handle = f"M {x1t - 6} {top + 110} C {x1t + 250} {top + 90}, {x1t + 250} {bottom - 110}, {x1b - 6} {bottom - 130}"
    facets = " ".join(
        f"M {x0t + tw * f} {top + 60} L {x0b + bw * f} {bottom - 60}" for f in (0.3, 0.5, 0.7)
    )
    # foam head: bumps over the rim, merged into one cap by a slab beneath them
    bumps = ((x0t + 30, 64), (x0t + 145, 84), (x0t + 262, 72), (x0t + 372, 82), (x1t - 24, 60))
    foam = " ".join(
        f"M {x} {top - 10} m -{rr} 0 a {rr} {rr} 0 1 1 {2 * rr} 0 a {rr} {rr} 0 1 1 -{2 * rr} 0"
        for x, rr in bumps
    )
    foam += f" M {x0t - 34} {top - 10} H {x1t + 34} V {top + 30} H {x0t - 34} Z"
    return dict(body=body, handle=handle, facets=facets, foam=foam,
                box=(x0t, x1t, x0b, x1b, top, bottom))


def wine_glass(cx=512):
    rim, bottom, hw = 150, 640, 300
    x0, x1 = cx - hw, cx + hw
    bowl = (f"M {x0} {rim} C {x0} {rim + 360}, {cx - 130} {bottom}, {cx} {bottom} "
            f"C {cx + 130} {bottom}, {x1} {rim + 360}, {x1} {rim} Z")
    stem = f"M {cx} {bottom} V 830 M {cx - 150} 860 H {cx + 150}"
    return bowl, stem, (x0, x1, rim, bottom)


def mug_outline(m, with_foam=True, fill="none", facets=True):
    parts = f"""
    <path d="{m['handle']}" fill="none" stroke="{TEXT}" stroke-width="{STROKE + 10}" stroke-linecap="round"/>
    <path d="{m['body']}" fill="{fill}" stroke="{TEXT}" stroke-width="{STROKE}" stroke-linejoin="round"/>"""
    if facets:
        parts += f"""
    <path d="{m['facets']}" fill="none" stroke="{TEXT}" stroke-opacity="0.35" stroke-width="12" stroke-linecap="round"/>"""
    if with_foam:
        parts += f"""
    <path d="{m['foam']}" fill="{TEXT}"/>"""
    return parts


def glass_outline(bowl, stem, fill="none"):
    return f"""
    <path d="{bowl}" fill="{fill}" stroke="{TEXT}" stroke-width="{STROKE}" stroke-linejoin="round"/>
    <path d="{stem}" fill="none" stroke="{TEXT}" stroke-width="{STROKE}" stroke-linecap="round"/>"""


def soft_fill(gid, base, peak):
    return f"""
  <linearGradient id="{gid}" gradientUnits="userSpaceOnUse" x1="0" y1="{base}" x2="0" y2="{peak}">
    <stop offset="0" stop-color="{TEAL}" stop-opacity="0.5"/>
    <stop offset="0.55" stop-color="{AMBER}" stop-opacity="0.5"/>
    <stop offset="1" stop-color="{RED}" stop-opacity="0.6"/>
  </linearGradient>"""


def liquid_fill(gid, bottom, peak):
    return f"""
  <linearGradient id="{gid}" gradientUnits="userSpaceOnUse" x1="0" y1="{bottom}" x2="0" y2="{peak}">
    <stop offset="0" stop-color="{TEAL}"/>
    <stop offset="0.6" stop-color="{AMBER}"/>
    <stop offset="0.86" stop-color="{CORAL}"/>
    <stop offset="1" stop-color="{RED}"/>
  </linearGradient>"""


# ------------------------------------------- 11. Beer mug, chart inside
def mug_chart():
    m = beer_mug()
    x0t, x1t, x0b, x1b, top, bottom = m["box"]
    base = bottom - 40
    pts = curve_points(x0b + 20, x1b - 20, base, 520)
    peak = min(p[1] for p in pts)
    defs = level_gradient("lvl", peak, base) + soft_fill("fill", base, peak) + f"""
  <clipPath id="clip"><path d="{m['body']}"/></clipPath>"""
    body = background() + f"""
  <g id="Mug">{mug_outline(m, with_foam=False, fill=SURF, facets=False)}
  </g>
  <g id="Curve" clip-path="url(#clip)">
    <path d="{path_from(pts, close_to_base=bottom)}" fill="url(#fill)"/>
    <path d="{path_from(pts)}" fill="none" stroke="url(#lvl)" stroke-width="38" stroke-linecap="round" stroke-linejoin="round"/>
  </g>
  <g id="Foam"><path d="{m['foam']}" fill="{TEXT}"/></g>"""
    svg("11-mug-chart", body, defs)


# ------------------------------- 12. Beer mug, the beer's surface is the curve
def mug_liquid():
    m = beer_mug()
    x0t, x1t, x0b, x1b, top, bottom = m["box"]
    base = bottom - 120
    pts = curve_points(x0t - 30, x1t + 30, base, 420)
    peak = min(p[1] for p in pts)
    defs = liquid_fill("beer", bottom, peak) + f"""
  <clipPath id="clip"><path d="{m['body']}"/></clipPath>"""
    body = background() + f"""
  <g id="Handle"><path d="{m['handle']}" fill="none" stroke="{TEXT}" stroke-width="{STROKE + 10}" stroke-linecap="round"/></g>
  <g id="Beer" clip-path="url(#clip)">
    <path d="{path_from(pts, close_to_base=bottom + 10)}" fill="url(#beer)"/>
    <path d="{path_from(pts)}" fill="none" stroke="{TEXT}" stroke-width="56" stroke-linecap="round" stroke-linejoin="round"/>
  </g>
  <g id="Mug">
    <path d="{m['body']}" fill="none" stroke="{TEXT}" stroke-width="{STROKE}" stroke-linejoin="round"/>
    <path d="{m['facets']}" fill="none" stroke="{TEXT}" stroke-opacity="0.25" stroke-width="12" stroke-linecap="round"/>
  </g>"""
    svg("12-mug-liquid", body, defs)


# ------------------------------------------ 13. Wine glass, chart inside
def wine_chart():
    bowl, stem, (x0, x1, rim, bottom) = wine_glass()
    base = bottom - 60
    pts = curve_points(x0 + 10, x1 - 10, base, 420)
    peak = min(p[1] for p in pts)
    defs = level_gradient("lvl", peak, base) + soft_fill("fill", base, peak) + f"""
  <clipPath id="clip"><path d="{bowl}"/></clipPath>"""
    body = background() + f"""
  <g id="Glass">{glass_outline(bowl, stem, fill=SURF)}
  </g>
  <g id="Curve" clip-path="url(#clip)">
    <path d="{path_from(pts, close_to_base=bottom)}" fill="url(#fill)"/>
    <path d="{path_from(pts)}" fill="none" stroke="url(#lvl)" stroke-width="36" stroke-linecap="round" stroke-linejoin="round"/>
  </g>"""
    svg("13-wine-chart", body, defs)


# ------------------------------- 14. Wine glass, the wine's surface is the curve
def wine_liquid():
    bowl, stem, (x0, x1, rim, bottom) = wine_glass()
    base = bottom - 150
    pts = curve_points(x0 - 30, x1 + 30, base, 300)
    peak = min(p[1] for p in pts)
    defs = liquid_fill("wine", bottom, peak) + f"""
  <clipPath id="clip"><path d="{bowl}"/></clipPath>"""
    body = background() + f"""
  <g id="Wine" clip-path="url(#clip)">
    <path d="{path_from(pts, close_to_base=bottom + 10)}" fill="url(#wine)"/>
    <path d="{path_from(pts)}" fill="none" stroke="{TEXT}" stroke-opacity="0.6" stroke-width="14" stroke-linecap="round"/>
  </g>
  <g id="Glass">{glass_outline(bowl, stem)}
  </g>"""
    svg("14-wine-liquid", body, defs)


# ---------------------------- 15. Wine glass in front of the band
def wine_behind():
    bowl, stem, (x0, x1, rim, bottom) = wine_glass()
    bx0, bx1, base, h = 60, 980, 760, 560
    upper = curve_points(bx0, bx1, base, h, b=0.72)
    lower = curve_points(bx0, bx1, base, h, b=1.40)
    peak = min(p[1] for p in upper)
    defs = liquid_fill("band", base, peak) + f"""
  <clipPath id="clip"><path d="{bowl}"/></clipPath>"""
    band = band_path(upper, lower)
    body = background() + f"""
  <g id="BandBehind" opacity="0.32"><path d="{band}" fill="url(#band)"/></g>
  <g id="BandInside" clip-path="url(#clip)"><path d="{band}" fill="url(#band)"/></g>
  <g id="Glass">{glass_outline(bowl, stem)}
  </g>"""
    svg("15-wine-behind", body, defs)


# ------------------------------ 16. Beer mug in front of the band
def mug_behind():
    m = beer_mug(cx=420)
    x0t, x1t, x0b, x1b, top, bottom = m["box"]
    bx0, bx1, base, h = 40, 990, 800, 600
    upper = curve_points(bx0, bx1, base, h, b=0.72)
    lower = curve_points(bx0, bx1, base, h, b=1.40)
    peak = min(p[1] for p in upper)
    defs = liquid_fill("band", base, peak) + f"""
  <clipPath id="clip"><path d="{m['body']}"/></clipPath>"""
    band = band_path(upper, lower)
    body = background() + f"""
  <g id="BandBehind" opacity="0.32"><path d="{band}" fill="url(#band)"/></g>
  <g id="BandInside" clip-path="url(#clip)"><path d="{band}" fill="url(#band)"/></g>
  <g id="Mug">{mug_outline(m, with_foam=True)}
  </g>"""
    svg("16-mug-behind", body, defs)


if __name__ == "__main__":
    mug_chart(); mug_liquid(); wine_chart(); wine_liquid(); wine_behind(); mug_behind()
    print("round 2 written")
