### Einleitung
Ein Programm, das dir hilft, Frachtbriefe zu verwalten. Ein Frachtbrief ist ein Dokument, das
Informationen über eine Sendung enthält, z.B. wer der Absender und der Empfänger sind, was 
versendet wird und wie es verpackt ist. Dein Programm ermöglicht es, diese Informationen einzugeben,
zu speichern und wieder abzurufen. 

### Der Code

#### Importe und Bibliotheken
- **`import sys`**: Das wird benötigt, um das Programm zu starten und zu beenden. [Python sys documentation](https://docs.python.org/3/library/sys.html)
- **`import sqlite3`**: Damit kannst du eine Datenbank nutzen, um die Frachtbriefinformationen zu speichern. [Python sqlite3 documentation](https://docs.python.org/3/library/sqlite3.html)
- **`import webbrowser`**: Damit kannst du HTML-Dateien in deinem Standard-Webbrowser öffnen. [Python webbrowser documentation](https://docs.python.org/3/library/webbrowser.html)
- **`from PyQt5.QtWidgets import ...`**: Das sind Werkzeuge, um die Benutzeroberfläche (die Fenster und Buttons) deines Programms zu erstellen. [PyQt5 documentation](https://www.riverbankcomputing.com/static/Docs/PyQt5/)
- **`from PyQt5.QtCore import Qt, QPoint`**: Zusätzliche Werkzeuge für die Benutzeroberfläche. [PyQt5 QtCore documentation](https://www.riverbankcomputing.com/static/Docs/PyQt5/api/qtcore/qtcore.html)

#### Die Hauptklasse (`MainWindow`)
- **`class MainWindow(QMainWindow):`**: Das ist die Hauptklasse deines Programms. Sie erstellt das Hauptfenster. [QMainWindow documentation](https://www.riverbankcomputing.com/static/Docs/PyQt5/api/qtwidgets/qmainwindow.html)
- **`def __init__(self):`**: Das ist der Konstruktor der Klasse. Er wird aufgerufen, wenn du eine neue Instanz von `MainWindow` erstellst. [Python __init__ method](https://docs.python.org/3/reference/datamodel.html#object.__init__)
- **`self.initUI()`**: Diese Methode richtet die Benutzeroberfläche ein.

#### Benutzeroberfläche einrichten (`initUI`)
- **`self.setWindowTitle('Frachtbriefe / Waybills')`**: Legt den Titel des Fensters fest. [QWidget setWindowTitle](https://www.riverbankcomputing.com/static/Docs/PyQt5/api/qtwidgets/qwidget.html#PyQt5.QtWidgets.QWidget.setWindowTitle)
- **`self.setGeometry(100, 100, 1200, 800)`**: Setzt die Position und Größe des Fensters. [QWidget setGeometry](https://www.riverbankcomputing.com/static/Docs/PyQt5/api/qtwidgets/qwidget.html#PyQt5.QtWidgets.QWidget.setGeometry)
- **`menubar = self.menuBar()`**: Erstellt eine Menüleiste. [QMainWindow menuBar](https://www.riverbankcomputing.com/static/Docs/PyQt5/api/qtwidgets/qmainwindow.html#PyQt5.QtWidgets.QMainWindow.menuBar)
- **`self.createMenu(...)`**: Fügt Menüs für internationale und nationale Frachtbriefe hinzu.

#### Menüs erstellen (`createMenu`)
- **`def createMenu(self, menubar, title, erfassen, abrufen):`**: Diese Methode erstellt ein Menü.
- **`menu.addAction(erfassenAction)`**: Fügt eine Aktion hinzu, um Daten einzugeben. [QMenu addAction](https://www.riverbankcomputing.com/static/Docs/PyQt5/api/qtwidgets/qmenu.html#PyQt5.QtWidgets.QMenu.addAction)
- **`menu.addAction(abrufenAction)`**: Fügt eine Aktion hinzu, um Daten abzurufen. [QMenu addAction](https://www.riverbankcomputing.com/static/Docs/PyQt5/api/qtwidgets/qmenu.html#PyQt5.QtWidgets.QMenu.addAction)

#### Daten eingeben und abrufen
- **`ErfassenForm` und `AbrufenForm`**: Diese Klassen erstellen Formulare, um Daten einzugeben und abzurufen.
- **`self.fields`**: Ein Wörterbuch, das die Felder des Formulars definiert, z.B. "AbsenderName / Sender Name".
- **`submitData`**: Diese Methode speichert die eingegebenen Daten in der Datenbank.
- **`searchData`**: Diese Methode sucht nach Daten in der Datenbank.

#### Frachtbriefe anzeigen und erstellen
- **`createFrachtbrief`**: Diese Methode erstellt einen Frachtbrief und öffnet ihn im Browser.
- **`showHeaderContextMenu` und `showRowContextMenu`**: Diese Methoden zeigen Kontextmenüs an, wenn du mit der rechten Maustaste auf Tabellenüberschriften oder -zeilen klickst.

#### Einfache Erklärung der Schlüsselkonzepte
- **`self`**: Bezieht sich auf das aktuelle Objekt der Klasse. Es wird verwendet, um auf Variablen und Methoden des Objekts zuzugreifen. [Python self documentation](https://docs.python.org/3/tutorial/classes.html#class-and-instance-variables)
- **`row`**: Eine Zeile in der Tabelle, die Daten anzeigt. Jede Zeile stellt einen Datensatz (einen Frachtbrief) dar.

### Zusammenfassung
Du hast ein Programm geschrieben, das dir hilft, Frachtbriefe zu verwalten. Du kannst Daten eingeben, speichern, suchen und anzeigen. Die Benutzeroberfläche ist mit PyQt5 erstellt, und die Daten werden in einer SQLite-Datenbank gespeichert. Das Programm kann auch HTML-Dateien erstellen, die den Frachtbrief darstellen, und diese im Browser öffnen.

---

Die Zusammenhänge zwischen den einzelnen Codezeilen, Funktionen und Definitionen im Detail erklärt:

### Importe und Bibliotheken
```python
import sys  # https://docs.python.org/3/library/sys.html
import sqlite3  # https://docs.python.org/3/library/sqlite3.html
import webbrowser  # https://docs.python.org/3/library/webbrowser.html
from PyQt5.QtWidgets import (QApplication, QMainWindow, QAction, QMenu, QWidget,
                             QVBoxLayout, QFormLayout, QLineEdit, QPushButton,
                             QTableWidget, QTableWidgetItem, QHeaderView, QHBoxLayout, QSplitter)  # https://www.riverbankcomputing.com/static/Docs/PyQt5/
from PyQt5.QtCore import Qt, QPoint  # https://www.riverbankcomputing.com/static/Docs/PyQt5/api/qtcore/qtcore.html
```
- **`import sys`**: Ermöglicht den Zugriff auf Systemfunktionen wie das Beenden des Programms.
- **`import sqlite3`**: Ermöglicht die Verwendung einer SQLite-Datenbank zur Speicherung der Frachtbriefdaten.
- **`import webbrowser`**: Ermöglicht das Öffnen von HTML-Dateien im Webbrowser.
- **`from PyQt5.QtWidgets import ...`**: Importiert verschiedene Widgets und Layouts aus der PyQt5-Bibliothek, um die Benutzeroberfläche zu erstellen.
- **`from PyQt5.QtCore import Qt, QPoint`**: Importiert grundlegende Qt-Funktionen und -Typen.

### Die Hauptklasse (`MainWindow`)
```python
class MainWindow(QMainWindow):  # https://www.riverbankcomputing.com/static/Docs/PyQt5/api/qtwidgets/qmainwindow.html
    def __init__(self):  # https://docs.python.org/3/reference/datamodel.html#object.__init__
        super().__init__()  # https://docs.python.org/3/library/functions.html#super
        self.initUI()
```
- **`class MainWindow(QMainWindow):`**: Definiert eine Klasse namens `MainWindow`, die von `QMainWindow` erbt. `QMainWindow` ist ein Standard-Fenstertyp in PyQt5.
- **`def __init__(self):`**: Konstruktor der Klasse, wird aufgerufen, wenn eine Instanz von `MainWindow` erstellt wird.
- **`super().__init__()`**: Ruft den Konstruktor der Basisklasse `QMainWindow` auf, um sicherzustellen, dass alle Initialisierungen der Basisklasse durchgeführt werden.
- **`self.initUI()`**: Ruft die Methode `initUI` auf, um die Benutzeroberfläche einzurichten.

### Benutzeroberfläche einrichten (`initUI`)
```python
def initUI(self):  # https://docs.python.org/3/tutorial/classes.html#method-objects
    self.setWindowTitle('Frachtbriefe / Waybills')  # https://www.riverbankcomputing.com/static/Docs/PyQt5/api/qtwidgets/qwidget.html#PyQt5.QtWidgets.QWidget.setWindowTitle
    self.setGeometry(100, 100, 1200, 800)  # https://www.riverbankcomputing.com/static/Docs/PyQt5/api/qtwidgets/qwidget.html#PyQt5.QtWidgets.QWidget.setGeometry
    menubar = self.menuBar()  # https://www.riverbankcomputing.com/static/Docs/PyQt5/api/qtwidgets

/qmainwindow.html#PyQt5.QtWidgets.QMainWindow.menuBar
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
def createMenu(self, menubar, title, erfassen, abrufen):  # https://docs.python.org/3/tutorial/classes.html#method-objects
    menu = menubar.addMenu(title)  # https://www.riverbankcomputing.com/static/Docs/PyQt5/api/qtwidgets/qmenubar.html#PyQt5.QtWidgets.QMenuBar.addMenu
    erfassenAction = QAction('Daten erfassen / Enter Data', self)  # https://www.riverbankcomputing.com/static/Docs/PyQt5/api/qtwidgets/qaction.html
    erfassenAction.triggered.connect(erfassen)  # https://www.riverbankcomputing.com/static/Docs/PyQt5/api/qtcore/qobject.html#PyQt5.QtCore.QObject.connect
    menu.addAction(erfassenAction)  # https://www.riverbankcomputing.com/static/Docs/PyQt5/api/qtwidgets/qmenu.html#PyQt5.QtWidgets.QMenu.addAction
    abrufenAction = QAction('Daten abrufen / Retrieve Data', self)  # https://www.riverbankcomputing.com/static/Docs/PyQt5/api/qtwidgets/qaction.html
    abrufenAction.triggered.connect(abrufen)  # https://www.riverbankcomputing.com/static/Docs/PyQt5/api/qtcore/qobject.html#PyQt5.QtCore.QObject.connect
    menu.addAction(abrufenAction)  # https://www.riverbankcomputing.com/static/Docs/PyQt5/api/qtwidgets/qmenu.html#PyQt5.QtWidgets.QMenu.addAction
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
class ErfassenForm(QWidget):  # https://www.riverbankcomputing.com/static/Docs/PyQt5/api/qtwidgets/qwidget.html
    def __init__(self, table):  # https://docs.python.org/3/reference/datamodel.html#object.__init__
        super().__init__()  # https://docs.python.org/3/library/functions.html#super
        self.table = table
        self.initUI()
```
- **`class ErfassenForm(QWidget):`**: Definiert eine Klasse `ErfassenForm`, die von `QWidget` erbt. `QWidget` ist ein Basiskomponentenklasse für alle GUI-Elemente in PyQt5.
- **`def __init__(self, table):`**: Konstruktor der Klasse `ErfassenForm`.
- **`self.table = table`**: Speichert den Namen der Tabelle, in der die Daten gespeichert werden sollen.
- **`self.initUI()`**: Initialisiert die Benutzeroberfläche des Formulars.

```python
def initUI(self):  # https://docs.python.org/3/tutorial/classes.html#method-objects
    layout = QVBoxLayout()  # https://www.riverbankcomputing.com/static/Docs/PyQt5/api/qtwidgets/qvboxlayout.html
    formLayout = QFormLayout()  # https://www.riverbankcomputing.com/static/Docs/PyQt5/api/qtwidgets/qformlayout.html
    self.fields = {
        'AusstellungsDatum / Date of Issue': QLineEdit(),  # https://www.riverbankcomputing.com/static/Docs/PyQt5/api/qtwidgets/qlineedit.html
        'Ausstellungsort / Place of Issue': QLineEdit(),  # https://www.riverbankcomputing.com/static/Docs/PyQt5/api/qtwidgets/qlineedit.html
        ...
    }
    for field, widget in self.fields.items():  # https://docs.python.org/3/tutorial/controlflow.html#for-statements
        formLayout.addRow(field, widget)  # https://www.riverbankcomputing.com/static/Docs/PyQt5/api/qtwidgets/qformlayout.html#PyQt5.QtWidgets.QFormLayout.addRow
    self.submitButton = QPushButton('Speichern / Save')  # https://www.riverbankcomputing.com/static/Docs/PyQt5/api/qtwidgets/qpushbutton.html
    self.submitButton.clicked.connect(self.submitData)  # https://www.riverbankcomputing.com/static/Docs/PyQt5/api/qtcore/qobject.html#PyQt5.QtCore.QObject.connect
    layout.addLayout(formLayout)  # https://www.riverbankcomputing.com/static/Docs/PyQt5/api/qtwidgets/qboxlayout.html#PyQt5.QtWidgets.QBoxLayout.addLayout
    layout.addWidget(self.submitButton)  # https://www.riverbankcomputing.com/static/Docs/PyQt5/api/qtwidgets/qboxlayout.html#PyQt5.QtWidgets.QBoxLayout.addWidget
    self.setLayout(layout)  # https://www.riverbankcomputing.com/static/Docs/PyQt5/api/qtwidgets/qwidget.html#PyQt5.QtWidgets.QWidget.setLayout
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
class AbrufenForm(QWidget):  # https://www.riverbankcomputing.com/static/Docs/PyQt5/api/qtwidgets/qwidget.html
    def __init__(self, table):  # https://docs.python.org/3/reference/datamodel.html#object.__init__
        super().__init__()  # https://docs.python.org/3/library/functions.html#super
        self.table = table
        self.initUI()
```
- **`class AbrufenForm(QWidget):`**: Definiert eine Klasse `AbrufenForm`, die von `QWidget` erbt.
- **`def __init__(self, table):`**: Konstruktor der Klasse `AbrufenForm`.
- **`self.table = table`**: Speichert den Namen der Tabelle, aus der die Daten abgerufen werden sollen.
- **`self.initUI()`**: Initialisiert die Benutzeroberfläche des Formulars.

```python
def initUI(self):  # https://docs.python.org/3/tutorial/classes.html#method-objects
    layout = QHBoxLayout()  # https://www.riverbankcomputing.com/static/Docs/PyQt5/api/qtwidgets/qhboxlayout.html
    splitter = QSplitter(Qt.Horizontal)  # https://www.riverbankcomputing.com

/static/Docs/PyQt5/api/qtwidgets/qsplitter.html
    searchWidget = QWidget()  # https://www.riverbankcomputing.com/static/Docs/PyQt5/api/qtwidgets/qwidget.html
    searchLayout = QFormLayout()  # https://www.riverbankcomputing.com/static/Docs/PyQt5/api/qtwidgets/qformlayout.html
    self.searchFields = {
        'FrachtbriefID / Waybill ID': QLineEdit(),  # https://www.riverbankcomputing.com/static/Docs/PyQt5/api/qtwidgets/qlineedit.html
        'AusstellungsDatum / Date of Issue': QLineEdit(),  # https://www.riverbankcomputing.com/static/Docs/PyQt5/api/qtwidgets/qlineedit.html
        ...
    }
    for field, widget in self.searchFields.items():  # https://docs.python.org/3/tutorial/controlflow.html#for-statements
        searchLayout.addRow(field, widget)  # https://www.riverbankcomputing.com/static/Docs/PyQt5/api/qtwidgets/qformlayout.html#PyQt5.QtWidgets.QFormLayout.addRow
    self.searchButton = QPushButton('Suchen / Search')  # https://www.riverbankcomputing.com/static/Docs/PyQt5/api/qtwidgets/qpushbutton.html
    self.searchButton.clicked.connect(self.searchData)  # https://www.riverbankcomputing.com/static/Docs/PyQt5/api/qtcore/qobject.html#PyQt5.QtCore.QObject.connect
    searchLayout.addWidget(self.searchButton)  # https://www.riverbankcomputing.com/static/Docs/PyQt5/api/qtwidgets/qboxlayout.html#PyQt5.QtWidgets.QBoxLayout.addWidget
    searchWidget.setLayout(searchLayout)  # https://www.riverbankcomputing.com/static/Docs/PyQt5/api/qtwidgets/qwidget.html#PyQt5.QtWidgets.QWidget.setLayout
    splitter.addWidget(searchWidget)  # https://www.riverbankcomputing.com/static/Docs/PyQt5/api/qtwidgets/qsplitter.html#PyQt5.QtWidgets.QSplitter.addWidget
    self.tableWidget = QTableWidget()  # https://www.riverbankcomputing.com/static/Docs/PyQt5/api/qtwidgets/qtablewidget.html
    self.tableWidget.setColumnCount(len(self.searchFields))  # https://www.riverbankcomputing.com/static/Docs/PyQt5/api/qtwidgets/qtablewidget.html#PyQt5.QtWidgets.QTableWidget.setColumnCount
    self.tableWidget.setHorizontalHeaderLabels(self.searchFields.keys())  # https://www.riverbankcomputing.com/static/Docs/PyQt5/api/qtwidgets/qtablewidget.html#PyQt5.QtWidgets.QTableWidget.setHorizontalHeaderLabels
    self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)  # https://www.riverbankcomputing.com/static/Docs/PyQt5/api/qtwidgets/qheaderview.html#PyQt5.QtWidgets.QHeaderView.setSectionResizeMode
    self.tableWidget.horizontalHeader().setContextMenuPolicy(Qt.CustomContextMenu)  # https://www.riverbankcomputing.com/static/Docs/PyQt5/api/qtwidgets/qheaderview.html#PyQt5.QtWidgets.QHeaderView.setContextMenuPolicy
    self.tableWidget.horizontalHeader().customContextMenuRequested.connect(self.showHeaderContextMenu)  # https://www.riverbankcomputing.com/static/Docs/PyQt5/api/qtcore/qobject.html#PyQt5.QtCore.QObject.connect
    self.tableWidget.setContextMenuPolicy(Qt.CustomContextMenu)  # https://www.riverbankcomputing.com/static/Docs/PyQt5/api/qtwidgets/qwidget.html#PyQt5.QtWidgets.QWidget.setContextMenuPolicy
    self.tableWidget.customContextMenuRequested.connect(self.showRowContextMenu)  # https://www.riverbankcomputing.com/static/Docs/PyQt5/api/qtcore/qobject.html#PyQt5.QtCore.QObject.connect
    splitter.addWidget(self.tableWidget)  # https://www.riverbankcomputing.com/static/Docs/PyQt5/api/qtwidgets/qsplitter.html#PyQt5.QtWidgets.QSplitter.addWidget
    layout.addWidget(splitter)  # https://www.riverbankcomputing.com/static/Docs/PyQt5/api/qtwidgets/qboxlayout.html#PyQt5.QtWidgets.QBoxLayout.addWidget
    self.setLayout(layout)  # https://www.riverbankcomputing.com/static/Docs/PyQt5/api/qtwidgets/qwidget.html#PyQt5.QtWidgets.QWidget.setLayout
```
- **`def initUI(self):`**: Methode zur Initialisierung der Benutzeroberfläche des Formulars.
- **`layout = QHBoxLayout()`**: Erstellt ein horizontales Layout.
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
def submitData(self):  # https://docs.python.org/3/tutorial/classes.html#method-objects
    conn = sqlite3.connect('frachtbriefe.db')  # https://docs.python.org/3/library/sqlite3.html#sqlite3.connect
    cursor = conn.cursor()  # https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.cursor
    columns = ', '.join(self.fields.keys())  # https://docs.python.org/3/library/stdtypes.html#str.join
    placeholders = ', '.join('?' * len(self.fields))  # https://docs.python.org/3/library/stdtypes.html#str.join
    query = f'INSERT INTO {self.table} ({columns}) VALUES ({placeholders})'  # https://docs.python.org/3/reference/lexical_analysis.html#f-strings
    values = [widget.text() for widget in self.fields.values()]  # https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
    cursor.execute(query, values)  # https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor.execute
    conn.commit()  # https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.commit
    conn.close()  # https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.close
```
- **`def submitData(self):`**: Methode zum Speichern der eingegebenen Daten in der Datenbank.
- **`conn = sqlite3.connect('frachtbriefe.db')`**: Stellt eine Verbindung zur SQLite-Datenbank her.
- **`cursor = conn.cursor()`**: Erstellt einen Cursor zum Ausführen von SQL-Befehlen.
- **`columns = ', '.join(self.fields.keys())`**: Erstellt eine durch Kommas getrennte Liste der Spaltennamen.
- **`placeholders =

 ', '.join('?' * len(self.fields))`**: Erstellt Platzhalter für die Werte.
- **`query = f'INSERT INTO {self.table} ({columns}) VALUES ({placeholders})'`**: Erstellt die SQL-Abfrage zum Einfügen der Daten.
- **`values = [widget.text() for widget in self.fields.values()]`**: Erstellt eine Liste der eingegebenen Werte.
- **`cursor.execute(query, values)`**: Führt die SQL-Abfrage aus und fügt die Daten in die Tabelle ein.
- **`conn.commit()`**: Speichert die Änderungen in der Datenbank.
- **`conn.close()`**: Schließt die Datenbankverbindung.

#### Daten suchen (`searchData`)
```python
def searchData(self):  # https://docs.python.org/3/tutorial/classes.html#method-objects
    conn = sqlite3.connect('frachtbriefe.db')  # https://docs.python.org/3/library/sqlite3.html#sqlite3.connect
    cursor = conn.cursor()  # https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.cursor
    conditions = [f"{field.split(' / ')[0]} LIKE ?" for field, widget in self.searchFields.items() if widget.text()]  # https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
    values = [f"{widget.text()}%" for widget in self.searchFields.values() if widget.text()]  # https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
    query = f"SELECT * FROM {self.table}" + (" WHERE " + " AND ".join(conditions) if conditions else "")  # https://docs.python.org/3/reference/lexical_analysis.html#f-strings
    cursor.execute(query, values)  # https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor.execute
    results = cursor.fetchall()  # https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor.fetchall
    self.tableWidget.setRowCount(len(results))  # https://www.riverbankcomputing.com/static/Docs/PyQt5/api/qtwidgets/qtablewidget.html#PyQt5.QtWidgets.QTableWidget.setRowCount
    for row_idx, row_data in enumerate(results):  # https://docs.python.org/3/library/functions.html#enumerate
        for col_idx, col_data in enumerate(row_data):  # https://docs.python.org/3/library/functions.html#enumerate
            self.tableWidget.setItem(row_idx, col_idx, QTableWidgetItem(str(col_data)))  # https://www.riverbankcomputing.com/static/Docs/PyQt5/api/qtwidgets/qtablewidget.html#PyQt5.QtWidgets.QTableWidget.setItem
    conn.close()  # https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.close
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
def showHeaderContextMenu(self, pos: QPoint):  # https://docs.python.org/3/tutorial/classes.html#method-objects
    header = self.tableWidget.horizontalHeader()  # https://www.riverbankcomputing.com/static/Docs/PyQt5/api/qtwidgets/qtablewidget.html#PyQt5.QtWidgets.QTableWidget.horizontalHeader
    logicalIndex = header.logicalIndexAt(pos)  # https://www.riverbankcomputing.com/static/Docs/PyQt5/api/qtwidgets/qheaderview.html#PyQt5.QtWidgets.QHeaderView.logicalIndexAt
    menu = QMenu()  # https://www.riverbankcomputing.com/static/Docs/PyQt5/api/qtwidgets/qmenu.html
    resizeAction = QAction('Optimale Breite / Optimal Width', self)  # https://www.riverbankcomputing.com/static/Docs/PyQt5/api/qtwidgets/qaction.html
    resizeAction.triggered.connect(lambda: self.tableWidget.resizeColumnToContents(logicalIndex))  # https://www.riverbankcomputing.com/static/Docs/PyQt5/api/qtcore/qobject.html#PyQt5.QtCore.QObject.connect
    menu.addAction(resizeAction)  # https://www.riverbankcomputing.com/static/Docs/PyQt5/api/qtwidgets/qmenu.html#PyQt5.QtWidgets.QMenu.addAction
    menu.exec(header.mapToGlobal(pos))  # https://www.riverbankcomputing.com/static/Docs/PyQt5/api/qtwidgets/qwidget.html#PyQt5.QtWidgets.QWidget.mapToGlobal
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
def showRowContextMenu(self, pos: QPoint):  # https://docs.python.org/3/tutorial/classes.html#method-objects
    row = self.tableWidget.rowAt(pos.y())  # https://www.riverbankcomputing.com/static/Docs/PyQt5/api/qtwidgets/qtablewidget.html#PyQt5.QtWidgets.QTableWidget.rowAt
    if row < 0: return
    menu = QMenu()  # https://www.riverbankcomputing.com/static/Docs/PyQt5/api/qtwidgets/qmenu.html
    createAction = QAction('Erstelle Frachtbrief / Create Waybill', self)  # https://www.riverbankcomputing.com/static/Docs/PyQt5/api/qtwidgets/qaction.html
    createAction.triggered.connect(lambda: self.createFrachtbrief(row))  # https://www.riverbankcomputing.com/static/Docs/PyQt5/api/qtcore/qobject.html#PyQt5.QtCore.QObject.connect
    menu.addAction(createAction)  # https://www.riverbankcomputing.com/static/Docs/PyQt5/api/qtwidgets/qmenu.html#PyQt5.QtWidgets.QMenu.addAction
    menu.exec(self.tableWidget.viewport().mapToGlobal(pos))  # https://www.riverbankcomputing.com/static/Docs/PyQt5/api/qtwidgets/qwidget.html#PyQt5.QtWidgets.QWidget.mapToGlobal
```
- **`def showRowContextMenu(self, pos: QPoint):`**: Methode zum Anzeigen eines Kontextmenüs für die Tabellenzeilen.
- **`row = self.tableWidget.rowAt(pos.y())`**: Holt den Index der Zeile, an der das Kontextmenü angezeigt wird.
- **`if row < 0: return`**: Bricht die Methode ab, wenn keine gültige Zeile gefunden wurde.
- **`menu = QMenu()`**: Erstellt ein Kontextmenü.
- **`createAction = QAction('Erstelle Frachtbrief / Create Waybill', self)`**: Erstellt eine Aktion zum Erstellen eines F

rachtbriefs.
- **`createAction.triggered.connect(lambda: self.createFrachtbrief(row))`**: Verbindet die Aktion mit der Methode `createFrachtbrief`.
- **`menu.addAction(createAction)`**: Fügt die Aktion zum Kontextmenü hinzu.
- **`menu.exec(self.tableWidget.viewport().mapToGlobal(pos))`**: Zeigt das Kontextmenü an der angegebenen Position an.

### Frachtbriefe anzeigen und erstellen
#### Frachtbrief erstellen (`createFrachtbrief`)
```python
def createFrachtbrief(self, row):  # https://docs.python.org/3/tutorial/classes.html#method-objects
    data = {self.tableWidget.horizontalHeaderItem(col).text(): self.tableWidget.item(row, col).text() for col in range(self.tableWidget.columnCount())}  # https://docs.python.org/3/tutorial/datastructures.html#dictionaries
    template_path = 'if.html' if self.table == 'internationalefrachtbriefe' else 'nf.html'  # https://docs.python.org/3/reference/lexical_analysis.html#if
    with open(template_path, 'r', encoding='utf-8') as file:  # https://docs.python.org/3/library/functions.html#open
        html_content = file.read()  # https://docs.python.org/3/library/io.html#io.TextIOBase.read
    for key, value in data.items():  # https://docs.python.org/3/tutorial/controlflow.html#for-statements
        html_content = html_content.replace(f'{{{{ {key.split(" / ")[0]} }}}}', value)  # https://docs.python.org/3/library/stdtypes.html#str.replace
    filename = f'{data["FrachtbriefID / Waybill ID"]}_{data["AusstellungsDatum / Date of Issue"]}_{data["EmpfaengerName / Recipient Name"]}.html'.replace(" ", "_")  # https://docs.python.org/3/reference/lexical_analysis.html#f-strings
    with open(filename, 'w', encoding='utf-8') as file:  # https://docs.python.org/3/library/functions.html#open
        file.write(html_content)  # https://docs.python.org/3/library/io.html#io.TextIOBase.write
    webbrowser.open(filename)  # https://docs.python.org/3/library/webbrowser.html#webbrowser.open
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
if __name__ == '__main__':  # https://docs.python.org/3/reference/datamodel.html#module.__name__
    app = QApplication(sys.argv)  # https://www.riverbankcomputing.com/static/Docs/PyQt5/api/qtwidgets/qapplication.html
    mainWindow = MainWindow()  # https://docs.python.org/3/reference/compound_stmts.html#class
    mainWindow.show()  # https://www.riverbankcomputing.com/static/Docs/PyQt5/api/qtwidgets/qwidget.html#PyQt5.QtWidgets.QWidget.show
    sys.exit(app.exec())  # https://docs.python.org/3/library/sys.html#sys.exit
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
