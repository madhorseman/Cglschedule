"""Inline src/ into the single index.html that GitHub Pages serves. Run: python3 build.py"""
from pathlib import Path

root = Path(__file__).parent
src = root / "src"
html = (src / "index.template.html").read_text()
engine = (src / "engine.js").read_text()
# engine.js ends with a CommonJS export for testing; harmless in the browser but strip it anyway
engine = engine.split("if (typeof module !== 'undefined')")[0].rstrip() + "\n"
html = (html.replace("/*STYLES*/", (src / "styles.css").read_text())
            .replace("/*ENGINE*/", engine)
            .replace("/*APP*/", (src / "app.js").read_text()))
out = root / "index.html"
out.write_text(html)
print(f"wrote {out} ({len(html)//1024} KB)")
