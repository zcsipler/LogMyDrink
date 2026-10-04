#!/usr/bin/env python3
"""Round 3, from concept 11: a foamy beer mug with the curve mostly inside
it, but the start of the rise and the end of the fall run out past the
glass. Inside the mug the curve is filled; outside only the line continues.
The variants differ in how the outside part is drawn."""
from make_icons import (
    BG, SURF, TEXT, TEAL, AMBER, CORAL, RED,
    curve_points, path_from, level_gradient, background, svg,
)
from make_icons_r2 import beer_mug, soft_fill, STROKE


def overflow(name, *, outside_opacity=0.55, outside_fill=0.0, dashed=False,
             mirrored=False, line=38):
    m = beer_mug(cx=440)   # mirrored variants flip the whole mug with a transform
    x0t, x1t, x0b, x1b, top, bottom = m["box"]
    base = bottom - 40
    # the curve spans nearly the whole icon; its peak lands inside the mug
    # (peak at ~24 % of the span) and the tail runs out past the handle
    # the mirrored mug sits on the right (visual x 354..814), so the curve starts
    # later to keep its peak inside the glass; time still runs left to right
    pts = curve_points(260, 1000, base, 430) if mirrored else curve_points(110, 990, base, 430)
    peak = min(p[1] for p in pts)
    mirror = f' transform="translate(1024 0) scale(-1 1)"' if mirrored else ""
    defs = level_gradient("lvl", peak, base) + soft_fill("fill", base, peak) + f"""
  <clipPath id="clip"><path d="{m['body']}"{mirror}/></clipPath>"""
    dash = ' stroke-dasharray="2 70"' if dashed else ""
    curve_d = path_from(pts)
    fill_d = path_from(pts, close_to_base=bottom)
    body = background() + f"""
  <g id="CurveOutside" opacity="{outside_opacity}">
    {f'<path d="{fill_d}" fill="url(#fill)" opacity="{outside_fill}"/>' if outside_fill else ''}
    <path d="{curve_d}" fill="none" stroke="url(#lvl)" stroke-width="{line}" stroke-linecap="round" stroke-linejoin="round"{dash}/>
  </g>
  <g id="Mug"{mirror}>
    <path d="{m['handle']}" fill="none" stroke="{TEXT}" stroke-width="{STROKE + 10}" stroke-linecap="round"/>
    <path d="{m['body']}" fill="{SURF}" stroke="{TEXT}" stroke-width="{STROKE}" stroke-linejoin="round"/>
  </g>
  <g id="CurveInside" clip-path="url(#clip)">
    <path d="{fill_d}" fill="url(#fill)"/>
    <path d="{curve_d}" fill="none" stroke="url(#lvl)" stroke-width="{line}" stroke-linecap="round" stroke-linejoin="round"/>
  </g>
  <g id="Rim"{mirror}>
    <path d="{m['body']}" fill="none" stroke="{TEXT}" stroke-width="{STROKE}" stroke-linejoin="round"/>
  </g>
  <g id="Foam"{mirror}><path d="{m['foam']}" fill="{TEXT}"/></g>"""
    svg(name, body, defs)


if __name__ == "__main__":
    # 21: the line simply continues outside, dimmed so the mug stays primary
    overflow("21-mug-overflow", outside_opacity=0.55)
    # 22: full-strength outside, with a faint fill — the chart is the hero, the mug the frame
    overflow("22-mug-overflow-bold", outside_opacity=1.0, outside_fill=0.25)
    # 23: dotted outside — what is outside the glass is the forecast, not the record
    overflow("23-mug-overflow-dotted", outside_opacity=0.9, dashed=True)
    # 24: mirrored mug, handle on the left, so the long tail leaves cleanly on the right
    overflow("24-mug-overflow-mirrored", outside_opacity=0.55, mirrored=True)
    print("round 3 written")
