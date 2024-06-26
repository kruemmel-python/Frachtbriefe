Hier ist eine einfache Erklärung des Codes, die für jemanden ohne Programmiererfahrung verständlich ist:

### Einleitung
Ein Programm, das dir hilft, Frachtbriefe zu verwalten. Ein Frachtbrief ist ein Dokument, das
Informationen über eine Sendung enthält, z.B. wer der Absender und der Empfänger sind, was 
versendet wird und wie es verpackt ist. Dein Programm ermöglicht es, diese Informationen einzugeben,
zu speichern und wieder abzurufen. 

### Der Code

#### Importe und Bibliotheken
- **`import sys`**: Das wird benötigt, um das Programm zu starten und zu beenden.
- **`import sqlite3`**: Damit kannst du eine Datenbank nutzen, um die Frachtbriefinformationen zu speichern.
- **`import webbrowser`**: Damit kannst du HTML-Dateien in deinem Standard-Webbrowser öffnen.
- **`from PyQt5.QtWidgets import ...`**: Das sind Werkzeuge, um die Benutzeroberfläche (die Fenster und Buttons) deines Programms
- zu erstellen.
- **`from PyQt5.QtCore import Qt, QPoint`**: Zusätzliche Werkzeuge für die Benutzeroberfläche.

#### Die Hauptklasse (`MainWindow`)
- **`class MainWindow(QMainWindow):`**: Das ist die Hauptklasse deines Programms. Sie erstellt das Hauptfenster.
- **`def __init__(self):`**: Das ist der Konstruktor der Klasse. Er wird aufgerufen, wenn du eine neue Instanz von `MainWindow`
- erstellst.
- **`self.initUI()`**: Diese Methode richtet die Benutzeroberfläche ein.

#### Benutzeroberfläche einrichten (`initUI`)
- **`self.setWindowTitle('Frachtbriefe / Waybills')`**: Legt den Titel des Fensters fest.
- **`self.setGeometry(100, 100, 1200, 800)`**: Setzt die Position und Größe des Fensters.
- **`menubar = self.menuBar()`**: Erstellt eine Menüleiste.
- **`self.createMenu(...)`**: Fügt Menüs für internationale und nationale Frachtbriefe hinzu.

#### Menüs erstellen (`createMenu`)
- **`def createMenu(self, menubar, title, erfassen, abrufen):`**: Diese Methode erstellt ein Menü.
- **`menu.addAction(erfassenAction)`**: Fügt eine Aktion hinzu, um Daten einzugeben.
- **`menu.addAction(abrufenAction)`**: Fügt eine Aktion hinzu, um Daten abzurufen.

#### Daten eingeben und abrufen
- **`ErfassenForm` und `AbrufenForm`**: Diese Klassen erstellen Formulare, um Daten einzugeben und abzurufen.
- **`self.fields`**: Ein Wörterbuch, das die Felder des Formulars definiert, z.B. "AbsenderName / Sender Name".
- **`submitData`**: Diese Methode speichert die eingegebenen Daten in der Datenbank.
- **`searchData`**: Diese Methode sucht nach Daten in der Datenbank.

#### Frachtbriefe anzeigen und erstellen
- **`createFrachtbrief`**: Diese Methode erstellt einen Frachtbrief und öffnet ihn im Browser.
- **`showHeaderContextMenu` und `showRowContextMenu`**: Diese Methoden zeigen Kontextmenüs an, wenn du mit der rechten
-  Maustaste auf Tabellenüberschriften oder -zeilen klickst.

#### Einfache Erklärung der Schlüsselkonzepte
- **`self`**: Bezieht sich auf das aktuelle Objekt der Klasse. Es wird verwendet, um auf Variablen und Methoden des Objekts
-  zuzugreifen.
- **`row`**: Eine Zeile in der Tabelle, die Daten anzeigt. Jede Zeile stellt einen Datensatz (einen Frachtbrief) dar.

### Zusammenfassung
Du hast ein Programm geschrieben, das dir hilft, Frachtbriefe zu verwalten. Du kannst Daten eingeben, speichern, suchen und 
anzeigen. Die Benutzeroberfläche ist mit PyQt5 erstellt, und die Daten werden in einer SQLite-Datenbank gespeichert. Das 
Programm kann auch HTML-Dateien erstellen, die den Frachtbrief darstellen, und diese im Browser öffnen.






-----------------------------------------------------------------------------------------------------------------------------


Die Zusammenhänge zwischen den einzelnen Codezeilen, Funktionen und Definitionen im Detail erklärt:

### Importe und Bibliotheken
```python
import sys
import sqlite3
import webbrowser
from PyQt5.QtWidgets import (QApplication, QMainWindow, QAction, QMenu, QWidget,
                             QVBoxLayout, QFormLayout, QLineEdit, QPushButton,
                             QTableWidget, QTableWidgetItem, QHeaderView, QHBoxLayout, QSplitter)
from PyQt5.QtCore import Qt, QPoint
```
- **`import sys`**: Ermöglicht den Zugriff auf Systemfunktionen wie das Beenden des Programms.
- **`import sqlite3`**: Ermöglicht die Verwendung einer SQLite-Datenbank zur Speicherung der Frachtbriefdaten.
- **`import webbrowser`**: Ermöglicht das Öffnen von HTML-Dateien im Webbrowser.
- **`from PyQt5.QtWidgets import ...`**: Importiert verschiedene Widgets und Layouts aus der PyQt5-Bibliothek, um die Benutzeroberfläche zu erstellen.
- **`from PyQt5.QtCore import Qt, QPoint`**: Importiert grundlegende Qt-Funktionen und -Typen.

### Die Hauptklasse (`MainWindow`)
```python
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
```
- **`class MainWindow(QMainWindow):`**: Definiert eine Klasse namens `MainWindow`, die von `QMainWindow` erbt. `QMainWindow` ist ein Standard-Fenstertyp in PyQt5.
- **`def __init__(self):`**: Konstruktor der Klasse, wird aufgerufen, wenn eine Instanz von `MainWindow` erstellt wird.
- **`super().__init__()`**: Ruft den Konstruktor der Basisklasse `QMainWindow` auf, um sicherzustellen, dass alle Initialisierungen der Basisklasse durchgeführt werden.
- **`self.initUI()`**: Ruft die Methode `initUI` auf, um die Benutzeroberfläche einzurichten.

### Benutzeroberfläche einrichten (`initUI`)
```python
def initUI(self):
    self.setWindowTitle('Frachtbriefe / Waybills')
    self.setGeometry(100, 100, 1200, 800)
    menubar = self.menuBar()
    self.createMenu(menubar, 'Internationaler Frachtbrief / International Waybill', self.erfassenInternational, self.abrufenInternational)
    self.createMenu(menubar, 'Nationaler Frachtbrief / National Waybill', self.erfassenNational, self.abrufenNational)
```
- **`def initUI(self):`**: Methode zur Initialisierung der Benutzeroberfläche.
- **`self.setWindowTitle('Frachtbriefe / Waybills')`**: Setzt den Fenstertitel auf "Frachtbriefe / Waybills".
- **`self.setGeometry(100, 100, 1200, 800)`**: Setzt die Position und Größe des Fensters (x=100, y=100, Breite=1200, Höhe=800).
- **`menubar = self.menuBar()`**: Erstellt eine Menüleiste.
- **`self.createMenu(...)`**: Fügt Menüs für internationale und nationale Frachtbriefe hinzu.

### Menüs erstellen (`createMenu`)
```python
def createMenu(self, menubar, title, erfassen, abrufen):
    menu = menubar.addMenu(title)
    erfassenAction = QAction('Daten erfassen / Enter Data', self)
    erfassenAction.triggered.connect(erfassen)
    menu.addAction(erfassenAction)
    abrufenAction = QAction('Daten abrufen / Retrieve Data', self)
    abrufenAction.triggered.connect(abrufen)
    menu.addAction(abrufenAction)
```
- **`def createMenu(self, menubar, title, erfassen, abrufen):`**: Methode zur Erstellung eines Menüs.
- **`menu = menubar.addMenu(title)`**: Fügt ein Menü mit dem gegebenen Titel zur Menüleiste hinzu.
- **`erfassenAction = QAction('Daten erfassen / Enter Data', self)`**: Erstellt eine Aktion "Daten erfassen".
- **`erfassenAction.triggered.connect(erfassen)`**: Verbindet das Auslösen der Aktion mit der Methode `erfassen`.
- **`menu.addAction(erfassenAction)`**: Fügt die Aktion zum Menü hinzu.
- **`abrufenAction = QAction('Daten abrufen / Retrieve Data', self)`**: Erstellt eine Aktion "Daten abrufen".
- **`abrufenAction.triggered.connect(abrufen)`**: Verbindet das Auslösen der Aktion mit der Methode `abrufen`.
- **`menu.addAction(abrufenAction)`**: Fügt die Aktion zum Menü hinzu.

### Daten eingeben und abrufen
#### ErfassenForm
```python
class ErfassenForm(QWidget):
    def __init__(self, table):
        super().__init__()
        self.table = table
        self.initUI()
```
- **`class ErfassenForm(QWidget):`**: Definiert eine Klasse `ErfassenForm`, die von `QWidget` erbt. `QWidget` ist ein Basiskomponentenklasse für alle GUI-Elemente in PyQt5.
- **`def __init__(self, table):`**: Konstruktor der Klasse `ErfassenForm`.
- **`self.table = table`**: Speichert den Namen der Tabelle, in der die Daten gespeichert werden sollen.
- **`self.initUI()`**: Initialisiert die Benutzeroberfläche des Formulars.

```python
def initUI(self):
    layout = QVBoxLayout()
    formLayout = QFormLayout()
    self.fields = {
        'AusstellungsDatum / Date of Issue': QLineEdit(),
        'Ausstellungsort / Place of Issue': QLineEdit(),
        ...
    }
    for field, widget in self.fields.items():
        formLayout.addRow(field, widget)
    self.submitButton = QPushButton('Speichern / Save')
    self.submitButton.clicked.connect(self.submitData)
    layout.addLayout(formLayout)
    layout.addWidget(self.submitButton)
    self.setLayout(layout)
```
- **`def initUI(self):`**: Methode zur Initialisierung der Benutzeroberfläche des Formulars.
- **`layout = QVBoxLayout()`**: Erstellt ein vertikales Layout.
- **`formLayout = QFormLayout()`**: Erstellt ein Formularlayout für die Eingabefelder.
- **`self.fields = { ... }`**: Ein Wörterbuch mit den Feldnamen und den entsprechenden Eingabefeldern.
- **`for field, widget in self.fields.items():`**: Fügt die Felder und Widgets zum Formularlayout hinzu.
- **`self.submitButton = QPushButton('Speichern / Save')`**: Erstellt einen Speichern-Button.
- **`self.submitButton.clicked.connect(self.submitData)`**: Verbindet das Klicken des Buttons mit der Methode `submitData`.
- **`layout.addLayout(formLayout)`**: Fügt das Formularlayout zum vertikalen Layout hinzu.
- **`layout.addWidget(self.submitButton)`**: Fügt den Speichern-Button zum Layout hinzu.
- **`self.setLayout(layout)`**: Setzt das Layout für das Widget.

#### AbrufenForm
```python
class AbrufenForm(QWidget):
    def __init__(self, table):
        super().__init__()
        self.table = table
        self.initUI()
```
- **`class AbrufenForm(QWidget):`**: Definiert eine Klasse `AbrufenForm`, die von `QWidget` erbt.
- **`def __init__(self, table):`**: Konstruktor der Klasse `AbrufenForm`.
- **`self.table = table`**: Speichert den Namen der Tabelle, aus der die Daten abgerufen werden sollen.
- **`self.initUI()`**: Initialisiert die Benutzeroberfläche des Formulars.

```python
def initUI(self):
    layout = QHBoxLayout()
    splitter = QSplitter(Qt.Horizontal)
    searchWidget = QWidget()
    searchLayout = QFormLayout()
    self.searchFields = {
        'FrachtbriefID / Waybill ID': QLineEdit(),
        'AusstellungsDatum / Date of Issue': QLineEdit(),
        ...
    }
    for field, widget in self.searchFields.items():
        searchLayout.addRow(field, widget)
    self.searchButton = QPushButton('Suchen / Search')
    self.searchButton.clicked.connect(self.searchData)
    searchLayout.addWidget(self.searchButton)
    searchWidget.setLayout(searchLayout)
    splitter.addWidget(searchWidget)
    self.tableWidget = QTableWidget()
    self.tableWidget.setColumnCount(len(self.searchFields))
    self.tableWidget.setHorizontalHeaderLabels(self.searchFields.keys())
    self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)
    self.tableWidget.horizontalHeader().setContextMenuPolicy(Qt.CustomContextMenu)
    self.tableWidget.horizontalHeader().customContextMenuRequested.connect(self.showHeaderContextMenu)
    self.tableWidget.setContextMenuPolicy(Qt.CustomContextMenu)
    self.tableWidget.customContextMenuRequested.connect(self.showRowContextMenu)
    splitter.addWidget(self.tableWidget)
    layout.addWidget(splitter)
    self.setLayout(layout)
```
- **`def initUI(self):`**: Methode zur Initialisierung der Benutzeroberfläche des Formulars.
- **`layout = QHBoxLayout

()`**: Erstellt ein horizontales Layout.
- **`splitter = QSplitter(Qt.Horizontal)`**: Erstellt einen horizontalen Splitter, der die Widgets nebeneinander anordnet.
- **`searchWidget = QWidget()`**: Erstellt ein Widget für die Suchfelder.
- **`searchLayout = QFormLayout()`**: Erstellt ein Formularlayout für die Suchfelder.
- **`self.searchFields = { ... }`**: Ein Wörterbuch mit den Feldnamen und den entsprechenden Eingabefeldern für die Suche.
- **`for field, widget in self.searchFields.items():`**: Fügt die Suchfelder und Widgets zum Formularlayout hinzu.
- **`self.searchButton = QPushButton('Suchen / Search')`**: Erstellt einen Such-Button.
- **`self.searchButton.clicked.connect(self.searchData)`**: Verbindet das Klicken des Buttons mit der Methode `searchData`.
- **`searchLayout.addWidget(self.searchButton)`**: Fügt den Such-Button zum Layout hinzu.
- **`searchWidget.setLayout(searchLayout)`**: Setzt das Layout für das Such-Widget.
- **`splitter.addWidget(searchWidget)`**: Fügt das Such-Widget zum Splitter hinzu.
- **`self.tableWidget = QTableWidget()`**: Erstellt eine Tabelle zur Anzeige der Suchergebnisse.
- **`self.tableWidget.setColumnCount(len(self.searchFields))`**: Setzt die Anzahl der Spalten in der Tabelle.
- **`self.tableWidget.setHorizontalHeaderLabels(self.searchFields.keys())`**: Setzt die Spaltenüberschriften der Tabelle.
- **`self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)`**: Erlaubt das Anpassen der Spaltenbreite.
- **`self.tableWidget.horizontalHeader().setContextMenuPolicy(Qt.CustomContextMenu)`**: Setzt das Kontextmenü für die Spaltenüberschriften.
- **`self.tableWidget.horizontalHeader().customContextMenuRequested.connect(self.showHeaderContextMenu)`**: Verbindet das Kontextmenü der Spaltenüberschriften mit der Methode `showHeaderContextMenu`.
- **`self.tableWidget.setContextMenuPolicy(Qt.CustomContextMenu)`**: Setzt das Kontextmenü für die Tabellenzeilen.
- **`self.tableWidget.customContextMenuRequested.connect(self.showRowContextMenu)`**: Verbindet das Kontextmenü der Tabellenzeilen mit der Methode `showRowContextMenu`.
- **`splitter.addWidget(self.tableWidget)`**: Fügt die Tabelle zum Splitter hinzu.
- **`layout.addWidget(splitter)`**: Fügt den Splitter zum Layout hinzu.
- **`self.setLayout(layout)`**: Setzt das Layout für das Widget.

### Datenbankoperationen
#### Daten speichern (`submitData`)
```python
def submitData(self):
    conn = sqlite3.connect('frachtbriefe.db')
    cursor = conn.cursor()
    columns = ', '.join(self.fields.keys())
    placeholders = ', '.join('?' * len(self.fields))
    query = f'INSERT INTO {self.table} ({columns}) VALUES ({placeholders})'
    values = [widget.text() for widget in self.fields.values()]
    cursor.execute(query, values)
    conn.commit()
    conn.close()
```
- **`def submitData(self):`**: Methode zum Speichern der eingegebenen Daten in der Datenbank.
- **`conn = sqlite3.connect('frachtbriefe.db')`**: Stellt eine Verbindung zur SQLite-Datenbank her.
- **`cursor = conn.cursor()`**: Erstellt einen Cursor zum Ausführen von SQL-Befehlen.
- **`columns = ', '.join(self.fields.keys())`**: Erstellt eine durch Kommas getrennte Liste der Spaltennamen.
- **`placeholders = ', '.join('?' * len(self.fields))`**: Erstellt Platzhalter für die Werte.
- **`query = f'INSERT INTO {self.table} ({columns}) VALUES ({placeholders})'`**: Erstellt die SQL-Abfrage zum Einfügen der Daten.
- **`values = [widget.text() for widget in self.fields.values()]`**: Erstellt eine Liste der eingegebenen Werte.
- **`cursor.execute(query, values)`**: Führt die SQL-Abfrage aus und fügt die Daten in die Tabelle ein.
- **`conn.commit()`**: Speichert die Änderungen in der Datenbank.
- **`conn.close()`**: Schließt die Datenbankverbindung.

#### Daten suchen (`searchData`)
```python
def searchData(self):
    conn = sqlite3.connect('frachtbriefe.db')
    cursor = conn.cursor()
    conditions = [f"{field.split(' / ')[0]} LIKE ?" for field, widget in self.searchFields.items() if widget.text()]
    values = [f"{widget.text()}%" for widget in self.searchFields.values() if widget.text()]
    query = f"SELECT * FROM {self.table}" + (" WHERE " + " AND ".join(conditions) if conditions else "")
    cursor.execute(query, values)
    results = cursor.fetchall()
    self.tableWidget.setRowCount(len(results))
    for row_idx, row_data in enumerate(results):
        for col_idx, col_data in enumerate(row_data):
            self.tableWidget.setItem(row_idx, col_idx, QTableWidgetItem(str(col_data)))
    conn.close()
```
- **`def searchData(self):`**: Methode zum Suchen von Daten in der Datenbank.
- **`conn = sqlite3.connect('frachtbriefe.db')`**: Stellt eine Verbindung zur SQLite-Datenbank her.
- **`cursor = conn.cursor()`**: Erstellt einen Cursor zum Ausführen von SQL-Befehlen.
- **`conditions = [f"{field.split(' / ')[0]} LIKE ?" for field, widget in self.searchFields.items() if widget.text()]`**: Erstellt eine Liste von Bedingungen für die SQL-Abfrage.
- **`values = [f"{widget.text()}%" for widget in self.searchFields.values() if widget.text()]`**: Erstellt eine Liste der Suchwerte.
- **`query = f"SELECT * FROM {self.table}" + (" WHERE " + " AND ".join(conditions) if conditions else "")`**: Erstellt die SQL-Abfrage zum Abrufen der Daten.
- **`cursor.execute(query, values)`**: Führt die SQL-Abfrage aus und ruft die Daten ab.
- **`results = cursor.fetchall()`**: Holt alle Ergebnisse der Abfrage.
- **`self.tableWidget.setRowCount(len(results))`**: Setzt die Anzahl der Zeilen in der Tabelle auf die Anzahl der Ergebnisse.
- **`for row_idx, row_data in enumerate(results):`**: Durchläuft die Ergebnisse.
- **`for col_idx, col_data in enumerate(row_data):`**: Durchläuft die Spalten der Ergebnisse.
- **`self.tableWidget.setItem(row_idx, col_idx, QTableWidgetItem(str(col_data)))`**: Fügt die Daten in die Tabelle ein.
- **`conn.close()`**: Schließt die Datenbankverbindung.

### Kontextmenüs
#### Kontextmenü für Spaltenüberschriften (`showHeaderContextMenu`)
```python
def showHeaderContextMenu(self, pos: QPoint):
    header = self.tableWidget.horizontalHeader()
    logicalIndex = header.logicalIndexAt(pos)
    menu = QMenu()
    resizeAction = QAction('Optimale Breite / Optimal Width', self)
    resizeAction.triggered.connect(lambda: self.tableWidget.resizeColumnToContents(logicalIndex))
    menu.addAction(resizeAction)
    menu.exec(header.mapToGlobal(pos))
```
- **`def showHeaderContextMenu(self, pos: QPoint):`**: Methode zum Anzeigen eines Kontextmenüs für die Spaltenüberschriften.
- **`header = self.tableWidget.horizontalHeader()`**: Holt die horizontale Kopfzeile der Tabelle.
- **`logicalIndex = header.logicalIndexAt(pos)`**: Holt den Index der Spalte, an der das Kontextmenü angezeigt wird.
- **`menu = QMenu()`**: Erstellt ein Kontextmenü.
- **`resizeAction = QAction('Optimale Breite / Optimal Width', self)`**: Erstellt eine Aktion zum Anpassen der Spaltenbreite.
- **`resizeAction.triggered.connect(lambda: self.tableWidget.resizeColumnToContents(logicalIndex))`**: Verbindet die Aktion mit der Methode zum Anpassen der Spaltenbreite.
- **`menu.addAction(resizeAction)`**: Fügt die Aktion zum Kontextmenü hinzu.
- **`menu.exec(header.mapToGlobal(pos))`**: Zeigt das Kontextmenü an der angegebenen Position an.

#### Kontextmenü für Tabellenzeilen (`showRowContextMenu`)
```python
def showRowContextMenu(self, pos: QPoint):
    row = self.tableWidget.rowAt(pos.y())
    if row < 0: return
    menu = QMenu()
    createAction = QAction('Erstelle Frachtbrief / Create Waybill', self)
    createAction.triggered.connect(lambda: self.createFrachtbrief(row))
    menu.addAction(createAction)
    menu.exec(self.tableWidget.viewport().mapToGlobal(pos))
```
- **`def showRowContextMenu(self, pos: QPoint):`**: Methode zum Anzeigen eines Kontextmenüs für die Tabellenzeilen.
- **`row = self.tableWidget.rowAt(pos.y())`**: Holt den Index der Zeile, an der das Kontextmenü angezeigt wird.
- **`if row < 0: return`**: Bricht die Methode ab, wenn

 keine gültige Zeile gefunden wurde.
- **`menu = QMenu()`**: Erstellt ein Kontextmenü.
- **`createAction = QAction('Erstelle Frachtbrief / Create Waybill', self)`**: Erstellt eine Aktion zum Erstellen eines Frachtbriefs.
- **`createAction.triggered.connect(lambda: self.createFrachtbrief(row))`**: Verbindet die Aktion mit der Methode `createFrachtbrief`.
- **`menu.addAction(createAction)`**: Fügt die Aktion zum Kontextmenü hinzu.
- **`menu.exec(self.tableWidget.viewport().mapToGlobal(pos))`**: Zeigt das Kontextmenü an der angegebenen Position an.

### Frachtbriefe anzeigen und erstellen
#### Frachtbrief erstellen (`createFrachtbrief`)
```python
def createFrachtbrief(self, row):
    data = {self.tableWidget.horizontalHeaderItem(col).text(): self.tableWidget.item(row, col).text() for col in range(self.tableWidget.columnCount())}
    template_path = 'if.html' if self.table == 'internationalefrachtbriefe' else 'nf.html'
    with open(template_path, 'r', encoding='utf-8') as file:
        html_content = file.read()
    for key, value in data.items():
        html_content = html_content.replace(f'{{{{ {key.split(" / ")[0]} }}}}', value)
    filename = f'{data["FrachtbriefID / Waybill ID"]}_{data["AusstellungsDatum / Date of Issue"]}_{data["EmpfaengerName / Recipient Name"]}.html'.replace(" ", "_")
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(html_content)
    webbrowser.open(filename)
```
- **`def createFrachtbrief(self, row):`**: Methode zum Erstellen eines Frachtbriefs.
- **`data = {self.tableWidget.horizontalHeaderItem(col).text(): self.tableWidget.item(row, col).text() for col in range(self.tableWidget.columnCount())}`**: Holt die Daten der ausgewählten Zeile aus der Tabelle.
- **`template_path = 'if.html' if self.table == 'internationalefrachtbriefe' else 'nf.html'`**: Wählt die Vorlage basierend auf dem Tabellennamen.
- **`with open(template_path, 'r', encoding='utf-8') as file:`**: Öffnet die HTML-Vorlage.
- **`html_content = file.read()`**: Liest den Inhalt der HTML-Vorlage.
- **`for key, value in data.items():`**: Ersetzt die Platzhalter in der Vorlage durch die tatsächlichen Werte.
- **`filename = f'{data["FrachtbriefID / Waybill ID"]}_{data["AusstellungsDatum / Date of Issue"]}_{data["EmpfaengerName / Recipient Name"]}.html'.replace(" ", "_")`**: Erstellt den Dateinamen für den Frachtbrief.
- **`with open(filename, 'w', encoding='utf-8') as file:`**: Speichert den Frachtbrief als HTML-Datei.
- **`file.write(html_content)`**: Schreibt den Inhalt in die HTML-Datei.
- **`webbrowser.open(filename)`**: Öffnet die HTML-Datei im Webbrowser.

### Hauptprogramm
```python
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())
```
- **`if __name__ == '__main__':`**: Überprüft, ob das Skript direkt ausgeführt wird.
- **`app = QApplication(sys.argv)`**: Erstellt eine Anwendung.
- **`mainWindow = MainWindow()`**: Erstellt eine Instanz des Hauptfensters.
- **`mainWindow.show()`**: Zeigt das Hauptfenster an.
- **`sys.exit(app.exec())`**: Startet die Anwendung und wartet, bis sie beendet wird.

### Zusammenhänge und Interaktionen
1. **Initialisierung**: Das Programm startet und erstellt ein Hauptfenster (`MainWindow`).
2. **Menüs**: Die Menüs für internationale und nationale Frachtbriefe werden erstellt und Aktionen (`Daten erfassen` und `Daten abrufen`) hinzugefügt.
3. **Formulare**: Beim Klicken auf `Daten erfassen` wird das Eingabeformular (`ErfassenForm`) angezeigt. Beim Klicken auf `Daten abrufen` wird das Suchformular (`AbrufenForm`) angezeigt.
4. **Datenbank**: Daten werden in die SQLite-Datenbank eingefügt (`submitData`) oder daraus abgerufen (`searchData`).
5. **Kontextmenüs**: Kontextmenüs für Spaltenüberschriften und Zeilen werden angezeigt und ermöglichen zusätzliche Aktionen (z.B. Anpassen der Spaltenbreite oder Erstellen eines Frachtbriefs).
6. **Frachtbriefe**: Daten werden aus der Tabelle geholt und in eine HTML-Datei eingefügt, die dann im Browser geöffnet wird (`createFrachtbrief`).

Diese detaillierte Erklärung sollte alle wesentlichen Aspekte und Zusammenhänge des Codes abdecken und helfen, zu verstehen, wie die einzelnen Teile miteinander interagieren.


