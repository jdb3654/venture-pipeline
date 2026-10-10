"""Render the TaktTools mark (concept A: Pareto bars) to PNG and SVG.
Geometry is in a 100x100 box, matching the design canvas."""
from PIL import Image, ImageDraw

NAVY = (0x1F, 0x3A, 0x5F)
ORANGE = (0xF0, 0x7C, 0x0A)
WHITE = (255, 255, 255)
BARS = [(17, 30, 18, 52), (41, 48, 18, 34), (65, 64, 18, 18)]
LINE = [(26, 52), (50, 32), (74, 22)]


def mark(draw, ox, oy, s, bar, line_w=5, dot_r=5):
    """Draw the mark scaled by s (pixels per unit) with its 100x100 box at (ox, oy)."""
    for x, y, w, h in BARS:
        draw.rounded_rectangle([ox + x * s, oy + y * s, ox + (x + w) * s, oy + (y + h) * s], radius=2 * s, fill=bar)
    pts = [(ox + x * s, oy + y * s) for x, y in LINE]
    draw.line(pts, fill=ORANGE, width=round(line_w * s), joint="curve")
    for x, y in pts:  # round caps and dots
        r = dot_r * s
        draw.ellipse([x - r, y - r, x + r, y + r], fill=ORANGE)


def icon(size, out, scale_of_box=0.78):
    ss = 4  # supersample
    big = size * ss
    img = Image.new("RGB", (big, big), NAVY)
    d = ImageDraw.Draw(img)
    box = big * scale_of_box
    s = box / 100
    off = (big - box) / 2
    mark(d, off, off, s, WHITE)
    img.resize((size, size), Image.LANCZOS).save(out, optimize=True)


def svg(out, background):
    bars = "".join(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="2" fill="{"#FFFFFF" if background else "#1F3A5F"}"/>' for x, y, w, h in BARS)
    pts = " ".join(f"{x},{y}" for x, y in LINE)
    dots = "".join(f'<circle cx="{x}" cy="{y}" r="5" fill="#F07C0A"/>' for x, y in LINE)
    bg = '<rect width="100" height="100" fill="#1F3A5F"/>' if background else ""
    open(out, "w").write(
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" role="img" aria-label="TaktTools">{bg}{bars}'
        f'<polyline points="{pts}" fill="none" stroke="#F07C0A" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>{dots}</svg>\n')


if __name__ == "__main__":
    icon(500, "takttools-shop-icon-500.png")
    icon(1000, "takttools-icon-1000.png")
    svg("takttools-mark.svg", background=False)
    svg("takttools-icon.svg", background=True)
    print("done")
