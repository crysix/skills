---
name: discord-news
description: Postet News, Artikel und Ankündigungen in einen festgelegten Discord Channel per Browser-Automatisierung. Immer verwenden wenn der User einen Link teilt und ihn auf Discord posten will, sagt "poste das im DC", "mach discord news", "teile das auf Discord", "poste das in den Channel", "Discord Nachricht", "DC post" oder ähnlich — auch wenn nur eine URL geteilt wird ohne weiteren Kontext. Direkt starten, nicht fragen ob der Skill verwendet werden soll.
---

# Discord News Skill

Postet aufbereitete News-Nachrichten in den konfigurierten Discord Channel via Browser-Automatisierung.

## Konfiguration

- **Server:** DEIN_SERVER_NAME
- **Channel:** DEIN_CHANNEL_NAME
- **Channel-URL:** https://discord.com/channels/DEINE_SERVER_ID/DEINE_CHANNEL_ID

---

## Workflow

### Schritt 1: Artikel extrahieren

Hol den Inhalt des geteilten Links per `web_fetch` oder navigiere im Browser zur URL. Extrahiere:
- **Titel** des Artikels
- **Datum** der Veröffentlichung
- **Hauptaussagen** (2–3 Sätze)
- **Wichtigste Punkte** (3–6 Bullet Points)
- **Original-URL** (für den Link am Ende)

### Schritt 2: Zum Discord Channel navigieren

Navigiere zur Channel-URL:
```
https://discord.com/channels/DEINE_SERVER_ID/DEINE_CHANNEL_ID
```

Warte bis Discord vollständig geladen ist. Falls ein Login erforderlich ist, informiere den User und warte.

### Schritt 3: Eingabefeld finden

Nutze das `find`-Tool mit einer natürlichsprachigen Beschreibung wie:
- „Nachrichteneingabefeld im Discord Channel"
- „Textfeld zum Schreiben einer Nachricht"

Klicke das Feld an, um es zu fokussieren.

### Schritt 4: Nachricht tippen

> ⚠️ **KRITISCH: Zeilenumbrüche in Discord**
> Discord sendet die Nachricht bei `Enter`. Für Zeilenumbrüche **muss `Shift+Enter`** verwendet werden.
> **Niemals** `\n` in einen String packen — jede Zeile einzeln tippen und mit `Shift+Enter` abschließen.

Tippe die Nachricht **zeilenweise** im folgenden Format:

```
[Emoji] **Fetter Titel** [optionales Emoji]
[Shift+Enter]
[Shift+Enter]
Ein bis zwei Sätze Zusammenfassung des Artikels.
[Shift+Enter]
[Shift+Enter]
• Wichtigster Punkt 1
[Shift+Enter]
• Wichtigster Punkt 2
[Shift+Enter]
• Wichtigster Punkt 3
[Shift+Enter]
[ggf. weitere Bullet Points]
[Shift+Enter]
[Shift+Enter]
🔗 https://original-url.de/artikel
```

**Emoji-Auswahl** (passend zum Thema wählen):
- 🔴 Breaking News / Wichtige Meldung
- 🤖 KI / Tech
- 💼 Business / Wirtschaft
- 🔒 Security / Datenschutz
- 🚀 Startups / Launches
- 🌍 Politik / Gesellschaft
- 💡 Innovation / Wissenschaft

**Formatierungsregeln:**
- Titel in `**fett**` (zwei Sternchen)
- Bullet Points mit `•` (Alt+8 oder kopieren)
- Maximal 6 Bullet Points — prägnant bleiben
- Zusammenfassung: 1–2 Sätze, kein Fachjargon
- URL am Ende immer als Klartext (kein Markdown-Link)

### Schritt 5: Screenshot und Bestätigung

Mache einen Screenshot, der die fertige Nachricht im Eingabefeld zeigt. Zeige ihn dem User und frage:

> „Die Nachricht ist fertig. Soll ich sie jetzt senden?"

**Warte auf explizites Ja** — nicht automatisch senden.

### Schritt 6: Senden und bestätigen

Nur nach explizitem „Ja" / „Senden" / „Go":
1. Drücke `Enter` um die Nachricht zu senden
2. Warte kurz bis die Nachricht erscheint
3. Mache einen abschließenden Screenshot zur Bestätigung
4. Informiere den User: „✅ Gepostet!"

---

## Format-Beispiel

```
🔴 **OpenAI und Microsoft — Neue Phase** 🤝

Die Partnerschaft wurde grundlegend überarbeitet. Wichtigste Änderungen im Überblick.

• Microsoft bleibt primärer Cloud Partner
• OpenAI darf jetzt auch andere Clouds nutzen
• Neue Lizenzstruktur gilt bis 2032, aber nicht mehr exklusiv
• Beide Seiten behalten Zugang zu gemeinsam entwickelten Modellen

🔗 https://openai.com/index/next-phase
```

---

## Fehlerfälle

| Problem | Lösung |
|---|---|
| Discord nicht eingeloggt | User informieren, warten bis er sich einloggt |
| Eingabefeld nicht gefunden | Screenshot machen, User um Hilfe bitten |
| Artikel nicht abrufbar | User fragen ob er den Inhalt manuell einfügen will |
| Nachricht zu lang | Bullet Points kürzen, max. 4 statt 6 |
