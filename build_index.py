"""Régénère index.html (GitHub Pages) à partir de ../claude-code-work.html."""
import pathlib
here = pathlib.Path(__file__).parent
s = (here.parent / "claude-code-work.html").read_text()
i = s.index("</style>") + len("</style>")
reset = """
<style>
:root{color-scheme:light;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}
body{margin:0}
img{max-width:100%}
[hidden]{display:none!important}
</style>
"""
doc = ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
       '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
       '<meta name="robots" content="noindex, nofollow">\n'
       '<meta name="description" content="What Olivier Malherbe built with Claude Code in a regulated asset management company: case studies, architecture diagrams, synthetic examples and product feedback.">\n'
       + reset + s[:i] + '\n</head>\n<body>\n' + s[i:] + '\n</body>\n</html>\n')
(here / "index.html").write_text(doc)
print("index.html régénéré")
