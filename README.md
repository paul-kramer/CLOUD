# Leitlinien zum Kompendium

Durchsuchbare Sammlung der AWMF-Leitlinien zu den Notfallbildern des
*Gemeinsamen Kompendiums Rettungsdienst 2026* (inoffiziell).

**Live:** https://paul-kramer.github.io/CLOUD/

- **Suche:** Freitext und Schlagworte über Titel, Kurzbeschreibung, Registernummer und Notfallbild, mit Filtern nach Klasse (S1–S3) und Status.
- **Nach Notfallbild:** alle 53 Notfallbilder mit den passenden Leitlinien; Lücken sind markiert, mit Hinweis auf ERC/GRC bzw. ESC.
- **Volltext:** Die PDFs lädst du selbst herunter (Download-Liste auf der Seite) und ziehst sie in die Seite. Dein Browser liest den Text mit pdf.js aus und speichert ihn lokal (IndexedDB). Nichts wird hochgeladen. Treffer verlinken auf die Seite im Original-PDF.

Dieses Repository enthält **keine Leitlinientexte**, nur Metadaten und Links. Die Leitlinien sind urheberrechtlich geschützt; die AWMF behält sich Text- und Datamining vor.

Stand der Recherche: 11/2026. Status und PDF-Links vor Verwendung auf der AWMF-Registerseite prüfen. Keine medizinische Empfehlung.

## Aufbau

- `leitlinien-datenbank/index.html` ist die Quelle (als Claude-Artifact geschrieben, ohne eigenes `<head>`).
- `index.html` wird daraus gebaut: `python3 tools/build-pages.py`
