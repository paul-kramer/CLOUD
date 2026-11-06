#!/usr/bin/env python3
"""Baut index.html (GitHub Pages) aus leitlinien-datenbank/index.html.

Die Quelldatei ist als Claude-Artifact geschrieben und hat kein eigenes
<!doctype>/<head>. Für GitHub Pages wird sie hier in ein vollständiges
HTML-Dokument mit Zeichensatz und Viewport eingebettet.
"""
from pathlib import Path

root = Path(__file__).resolve().parent.parent
src = (root / "leitlinien-datenbank" / "index.html").read_text(encoding="utf-8")
head = """<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="description" content="AWMF-Leitlinien zu den Notfallbildern des Gemeinsamen Kompendiums Rettungsdienst 2026: Schlagwortsuche, Zuordnung nach Notfallbild und lokale Volltextsuche.">
<style>:root{box-sizing:border-box;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}body{margin:0;font:14px system-ui,sans-serif}img{max-width:100%}[hidden]{display:none!important}</style>
</head>
<body>
"""
out = head + src + "\n</body>\n</html>\n"
(root / "index.html").write_text(out, encoding="utf-8")
print("index.html geschrieben,", len(out), "Zeichen")
