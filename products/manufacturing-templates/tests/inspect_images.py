"""Optional visual QA contact sheets; does not edit any product preview.

Requires preinstalled Pillow/pypdfium2; no dependency installation is needed
for the calculation suite. Outputs only into the supplied disposable folder.
"""
import argparse
from pathlib import Path
from PIL import Image, ImageDraw, ImageOps

PRODUCT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("work_dir", type=Path)
    args = parser.parse_args()
    args.work_dir.mkdir(parents=True, exist_ok=True)
    paths = sorted((PRODUCT / "previews").glob("*.png"))
    contact = Image.new("RGB", (900, ((len(paths) + 2) // 3) * 330), "#eeeeee")
    draw = ImageDraw.Draw(contact)
    for i, path in enumerate(paths):
        with Image.open(path) as image:
            # Two diagnostics: literal centered square crop and entire-sheet fit.
            thumb = ImageOps.fit(image.convert("RGB"), (280, 280))
            x, y = (i % 3) * 300 + 10, (i // 3) * 330 + 10
            contact.paste(thumb, (x, y))
            draw.text((x, y + 285), path.name, fill="black")
    contact.save(args.work_dir / "preview-square-crops.png")
    main_paths = ["OEE-Tracker-4.png", "Downtime-Log-and-Pareto-4.png", "Preventive-Maintenance-Schedule-2.png"]
    contact = Image.new("RGB", (900, 330), "#eeeeee")
    draw = ImageDraw.Draw(contact)
    for i, name in enumerate(main_paths):
        with Image.open(PRODUCT / "previews" / name) as image:
            tile = Image.new("RGB", (280, 280), "white")
            fit = ImageOps.contain(image.convert("RGB"), (280, 280))
            tile.paste(fit, ((280 - fit.width) // 2, (280 - fit.height) // 2))
            contact.paste(tile, (i * 300 + 10, 10))
            draw.text((i * 300 + 10, 295), name, fill="black")
    contact.save(args.work_dir / "preview-full-sheet-fit.png")
    try:
        import pypdfium2 as pdfium
    except ImportError:
        print("pypdfium2 unavailable; inspect native PDFs manually")
        return
    for path in args.work_dir.glob("*.pdf"):
        doc = pdfium.PdfDocument(path)
        for i in range(len(doc)):
            page = doc[i]
            bitmap = page.render(scale=1.5)
            bitmap.to_pil().save(path.with_name(path.stem + "-page%d.png" % (i + 1)))
            bitmap.close()
            page.close()
        doc.close()


if __name__ == "__main__":
    main()
