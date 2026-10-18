---
name: kleinanzeigen-listing
description: Generiert eine vollständige, verkaufsfertige Kleinanzeige für Kleinanzeigen.de aus einem Foto oder einer Artikelbeschreibung. Immer verwenden wenn der User ein Foto eines Gegenstands hochlädt und verkaufen möchte, Phrasen wie "mach eine Kleinanzeige", "ich will das verkaufen", "Anzeigentext schreiben", "Anzeige erstellen", "bei Kleinanzeigen einstellen" oder "eBay Kleinanzeigen" verwendet — auch wenn kein Bild vorhanden ist. Direkt starten, nicht fragen ob der Skill verwendet werden soll.
---

# Kleinanzeigen-Listing Generator

Erstellt professionelle, ehrliche Kleinanzeigen für Kleinanzeigen.de. Kein Marketing-Sprech, keine Übertreibungen — Käufer auf Kleinanzeigen sind skeptisch.

---

## Schritt 1: Artikel analysieren

**Wenn ein Bild vorhanden ist:**
Analysiere den Artikel systematisch:
- **Marke & Modell**: Erkenne Logos, Aufdrucke, Typenschilder
- **Kategorie**: z.B. Elektronik, Möbel, Kleidung, Sport, Haushalt
- **Zustand**: Sehr gut erhalten / Gut erhalten / Schlecht erhalten / Defekt
  - Sehr gut erhalten = kaum Gebrauchsspuren, wie neu
  - Gut erhalten = normale Gebrauchsspuren, voll funktionsfähig
  - Schlecht erhalten = sichtbare Mängel, aber funktionsfähig
  - Defekt = nicht oder eingeschränkt funktionsfähig
- **Material, Farbe, Größe** (wenn erkennbar)
- **Besondere Merkmale**: Ausstattung, Extras, Besonderheiten
- **Sichtbare Mängel**: Kratzer, Risse, Flecken — ehrlich benennen

**Wenn kein Bild vorhanden ist:**
Frage kurz nach: "Schick mir ein Foto des Artikels, dann erstelle ich die Anzeige. Alternativ beschreib mir kurz was du verkaufen möchtest."

---

## Schritt 2: Drei Rückfragen in einer Nachricht

Stelle **genau diese drei Fragen** in einer einzigen Nachricht, kompakt:

```
Um die Anzeige zu vervollständigen, kurz drei Fragen:

1. Wann ungefähr gekauft / wie alt ist der Artikel?
2. Was hat er neu gekostet (Originalpreis)?
3. Gibt es Zubehör oder Originalverpackung dabei?

Falls du einzelnes nicht weißt — kein Problem, einfach "weiß nicht" schreiben.
```

Wenn der User mit "weiß nicht" antwortet oder Angaben fehlen: weitermachen ohne diese Information.

---

## Schritt 3: Verkaufspreis berechnen

**Mit Originalpreis:**
| Zustand | Abzug vom Neupreis |
|---|---|
| Sehr gut erhalten | − 20 % |
| Gut erhalten | − 30 % |
| Schlecht erhalten | − 50 % |
| Defekt | − 80 % |

Runde auf glatte Beträge (z.B. 45 €, nicht 47,50 €).

**Ohne Originalpreis:**
Schätze den aktuellen Neupreis anhand von Marke/Modell/Kategorie. Weise klar darauf hin: *(Neupreis geschätzt, da nicht bekannt)*

**Hinweis:** Der berechnete Preis ist ein Vorschlag als VB (Verhandlungsbasis). Der User kann ihn anpassen.

---

## Schritt 4: Anzeige generieren

Ausgabe als Copy-Paste-Block mit Trennlinien:

```
════════════════════════════════════════
KLEINANZEIGE – BEREIT ZUM EINSTELLEN
════════════════════════════════════════

TITEL (max. 65 Zeichen):
[Artikel] – [Marke/Modell] – [Zustand kurz]

BESCHREIBUNG:
[Absatz 1 – Was ist es & Zustand]
Sachliche Beschreibung des Artikels. Zustand ehrlich angeben inkl. Mängel. Keine Superlative.

[Absatz 2 – Besonderheiten & Verkaufsgrund]
Warum wird verkauft (optional: "wird nicht mehr gebraucht", "Upgrade", o.ä.). Enthaltenes Zubehör, Originalverpackung.

[Absatz 3 – Abwicklung]
Abholung bevorzugt. Versand möglich gegen Aufpreis (Käufer trägt Versandkosten). Privatverkauf – keine Garantie, keine Rücknahme.

PREIS:
XX € VB
(Neupreis: XX € → Abzug XX % für Zustand "[Zustand]")

KATEGORIE:
[Passende Hauptkategorie auf Kleinanzeigen.de]

════════════════════════════════════════
```

---

## Tonalität & Regeln

- **Sachlich und direkt** — keine Adjektive wie "traumhaft", "top", "mega"
- **Kein "Hallo zusammen"**, keine Smileys, keine Ausrufezeichen
- **Mängel nicht verschweigen** — das schützt vor schlechten Bewertungen
- **Keine Floskeln** wie "Nur wegen Umzug", außer es ist wahr
- **Privatverkauf-Hinweis immer einbauen** — rechtlich wichtig
- **Versand**: Wenn unklar, Standard-Formulierung verwenden

---

## Kategorien-Referenz (Kleinanzeigen.de)

Häufige Hauptkategorien:
- Elektronik → Handys, Laptops, TV, Audio
- Möbel & Wohnen → Sofas, Tische, Lampen
- Kleidung & Accessoires → nach Zielgruppe
- Sport & Camping → Fahrräder, Fitnessgeräte
- Haushalt → Küchengeräte, Haushaltsgeräte
- Garten & Heimwerken → Werkzeug, Pflanzen
- Spielzeug & Kinderbedarf → Alter angeben
- Auto & Zubehör → KFZ-Teile, Zubehör
- Freizeit → Bücher, Musik, Sammler
