# Frachtbriefe GUI

Ein Python-Programm zur Verwaltung und Anzeige von internationalen und nationalen Frachtbriefen. Die GUI wurde mit PyQt5 erstellt und ermöglicht das Erfassen, Abrufen und Erstellen von Frachtbriefen als HTML-Dateien.

## Funktionen

- Erfassen von internationalen und nationalen Frachtbriefen
- Abrufen und Durchsuchen von Frachtbriefdaten
- Erstellen von HTML-Frachtbriefen basierend auf Daten aus der SQLite-Datenbank
- Konfigurierbare Spaltenbreite durch Kontextmenü
- Speichern der Frachtbriefe unter einem Dateinamen, der die Frachtbriefnummer, das Ausstellungsdatum und den Empfängernamen enthält

## Voraussetzungen

- Python 3.12 oder höher
- PyQt5
- SQLite

## Installation

1. Klonen Sie das Repository:

```sh
git clone https://github.com/username/frachtbriefe-gui.git
cd frachtbriefe-gui
```

Installieren Sie die erforderlichen Bibliotheken:

```python
pip install PyQt5
```
Starten Sie das Programm:

```python
python main.py
```

Verwenden Sie das Menü, um internationale oder nationale Frachtbriefe zu erfassen oder abzurufen.
Erfassen von Frachtbriefen
Wählen Sie im Menü "Internationaler Frachtbrief" oder "Nationaler Frachtbrief" und dann "Daten erfassen".
Füllen Sie das Formular aus und klicken Sie auf "Speichern".
Abrufen von Frachtbriefen
Wählen Sie im Menü "Internationaler Frachtbrief" oder "Nationaler Frachtbrief" und dann "Daten abrufen".
Verwenden Sie die Suchfelder, um nach bestimmten Frachtbriefen zu suchen.
Die Ergebnisse werden in einer Tabelle angezeigt.
Erstellen eines HTML-Frachtbriefs
Klicken Sie mit der rechten Maustaste auf eine Zeile in der Ergebnistabelle und wählen Sie "Erstelle Frachtbrief".
Der Frachtbrief wird als HTML-Datei gespeichert und im Standard-Webbrowser geöffnet. Der Dateiname enthält die Frachtbriefnummer, das Ausstellungsdatum und den Empfängernamen.
HTML-Templates
Die HTML-Templates (nf.html und if.html) enthalten Platzhalter, die durch die Daten aus der Datenbank ersetzt werden. Stellen Sie sicher, dass diese Templates im selben Verzeichnis wie das Python-Skript vorhanden sind.

Beispiel if.html

```html
<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Internationaler Frachtbrief</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        .container {
            width: 80%;
            margin: 20px auto;
            padding: 20px;
            border: 1px solid #000;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        h1 {
            text-align: center;
        }
        .section {
            margin-bottom: 20px;
        }
        .section h2 {
            border-bottom: 1px solid #000;
            padding-bottom: 5px;
        }
        .form-group {
            margin-bottom: 15px;
        }
        .form-group label {
            display: block;
            font-weight: bold;
        }
        .form-group input, .form-group textarea {
            width: 100%;
            padding: 8px;
            margin-top: 5px;
            border: 1px solid #000;
            border-radius: 4px;
        }
        .form-group textarea {
            resize: vertical;
            height: 100px;
        }
        .signatures {
            display: flex;
            justify-content: space-between;
        }
        .signature {
            width: 30%;
            text-align: center;
        }
        .signature input {
            margin-top: 20px;
        }
    </style>
</head>
<body>

<div class="container">
    <h1>Internationaler Frachtbrief</h1>

    <div class="section">
        <div class="form-group">
            <label for="frachtbriefnummer">Frachtbriefnummer</label>
            <input type="text" id="frachtbriefnummer" name="frachtbriefnummer" value="{{ FrachtbriefID }}">
        </div>
    </div>

    <!-- Weitere Abschnitte für Absender-, Empfänger- und Frachtführerinformationen -->

</div>

</body>
</html>
```

Beispiel nf.html

```html
<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Nationaler Frachtbrief</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        .container {
            width: 80%;
            margin: 20px auto;
            padding: 20px;
            border: 1px solid #000;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        h1 {
            text-align: center;
        }
        .section {
            margin-bottom: 20px;
        }
        .section h2 {
            border-bottom: 1px solid #000;
            padding-bottom: 5px;
        }
        .form-group {
            margin-bottom: 15px;
        }
        .form-group label {
            display: block;
            font-weight: bold.
        }
        .form-group input, .form-group textarea {
            width: 100%;
            padding: 8px;
            margin-top: 5px;
            border: 1px solid #000;
            border-radius: 4px.
        }
        .form-group textarea {
            resize: vertical;
            height: 100px.
        }
        .signatures {
            display: flex;
            justify-content: space-between.
        }
        .signature {
            width: 30%;
            text-align: center.
        }
        .signature input {
            margin-top: 20px.
        }
    </style>
</head>
<body>

<div class="container">
    <h1>Nationaler Frachtbrief</h1>

    <div class="section">
        <div class="form-group">
            <label for="frachtbriefnummer">Frachtbriefnummer</label>
            <input type="text" id="frachtbriefnummer" name="frachtbriefnummer" value="{{ FrachtbriefID }}">
        </div>
    </div>

    <!-- Weitere Abschnitte für Absender-, Empfänger- und Frachtführerinformationen -->

</div>

</body>
</html>
```


Lizenz
Dieses Projekt ist lizenziert unter der MIT-Lizenz - siehe die LICENSE Datei für Details.
