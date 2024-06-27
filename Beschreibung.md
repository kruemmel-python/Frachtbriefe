
# Frachtbriefe Verwaltung

## Einleitung
Ein Programm, das dir hilft, Frachtbriefe zu verwalten. Ein Frachtbrief ist ein Dokument, das
Informationen über eine Sendung enthält, z.B. wer der Absender und der Empfänger sind, was 
versendet wird und wie es verpackt ist. Dein Programm ermöglicht es, diese Informationen einzugeben,
zu speichern und wieder abzurufen. 

## Der Code

### Importe und Bibliotheken
- **`import sys`**: Das wird benötigt, um das Programm zu starten und zu beenden. ([Python sys module](https://docs.python.org/3/library/sys.html))
- **`import sqlite3`**: Damit kannst du eine Datenbank nutzen, um die Frachtbriefinformationen zu speichern. ([Python sqlite3 module](https://docs.python.org/3/library/sqlite3.html))
- **`import webbrowser`**: Damit kannst du HTML-Dateien in deinem Standard-Webbrowser öffnen. ([Python webbrowser module](https://docs.python.org/3/library/webbrowser.html))
- **`from PyQt5.QtWidgets import ...`**: Das sind Werkzeuge, um die Benutzeroberfläche (die Fenster und Buttons) deines Programms zu erstellen. ([PyQt5 QtWidgets module](https://doc.qt.io/qtforpython-5/PySide2/QtWidgets/index.html))
- **`from PyQt5.QtCore import Qt, QPoint`**: Zusätzliche Werkzeuge für die Benutzeroberfläche. ([PyQt5 QtCore module](https://doc.qt.io/qtforpython-5/PySide2/QtCore/index.html))

### Die Hauptklasse (`MainWindow`)
- **`class MainWindow(QMainWindow):`**: Das ist die Hauptklasse deines Programms. Sie erstellt das Hauptfenster. ([QMainWindow](https://doc.qt.io/qtforpython-5/PySide2/QtWidgets/QMainWindow.html))
- **`def __init__(self):`**: Das ist der Konstruktor der Klasse. Er wird aufgerufen, wenn du eine neue Instanz von `MainWindow` erstellst. ([__init__ method](https://docs.python.org/3/tutorial/classes.html#class-and-instance-variables))
- **`self.initUI()`**: Diese Methode richtet die Benutzeroberfläche ein.

### Benutzeroberfläche einrichten (`initUI`)
- **`self.setWindowTitle('Frachtbriefe / Waybills')`**: Legt den Titel des Fensters fest. ([setWindowTitle](https://doc.qt.io/qtforpython-5/PySide2/QtWidgets/QWidget.html#PySide2.QtWidgets.PySide2.QtWidgets.QWidget.setWindowTitle))
- **`self.setGeometry(100, 100, 1200, 800)`**: Setzt die Position und Größe des Fensters. ([setGeometry](https://doc.qt.io/qtforpython-5/PySide2/QtWidgets/QWidget.html#PySide2.QtWidgets.PySide2.QtWidgets.QWidget.setGeometry))
- **`menubar = self.menuBar()`**: Erstellt eine Menüleiste. ([menuBar](https://doc.qt.io/qtforpython-5/PySide2/QtWidgets/QMainWindow.html#PySide2.QtWidgets.PySide2.QtWidgets.QMainWindow.menuBar))
- **`self.createMenu(...)`**: Fügt Menüs für internationale und nationale Frachtbriefe hinzu.

### Menüs erstellen (`createMenu`)
- **`def createMenu(self, menubar, title, erfassen, abrufen):`**: Diese Methode erstellt ein Menü.
- **`menu.addAction(erfassenAction)`**: Fügt eine Aktion hinzu, um Daten einzugeben. ([addAction](https://doc.qt.io/qtforpython-5/PySide2/QtWidgets/QMenu.html#PySide2.QtWidgets.PySide2.QtWidgets.QMenu.addAction))
- **`menu.addAction(abrufenAction)`**: Fügt eine Aktion hinzu, um Daten abzurufen.

### Daten eingeben und abrufen
- **`ErfassenForm` und `AbrufenForm`**: Diese Klassen erstellen Formulare, um Daten einzugeben und abzurufen.
- **`self.fields`**: Ein Wörterbuch, das die Felder des Formulars definiert, z.B. "AbsenderName / Sender Name".
- **`submitData`**: Diese Methode speichert die eingegebenen Daten in der Datenbank.
- **`searchData`**: Diese Methode sucht nach Daten in der Datenbank.

### Frachtbriefe anzeigen und erstellen
- **`createFrachtbrief`**: Diese Methode erstellt einen Frachtbrief und öffnet ihn im Browser.
- **`showHeaderContextMenu` und `showRowContextMenu`**: Diese Methoden zeigen Kontextmenüs an, wenn du mit der rechten Maustaste auf Tabellenüberschriften oder -zeilen klickst.

### Einfache Erklärung der Schlüsselkonzepte
- **`self`**: Bezieht sich auf das aktuelle Objekt der Klasse. Es wird verwendet, um auf Variablen und Methoden des Objekts zuzugreifen. ([self](https://docs.python.org/3/tutorial/classes.html#class-and-instance-variables))
- **`row`**: Eine Zeile in der Tabelle, die Daten anzeigt. Jede Zeile stellt einen Datensatz (einen Frachtbrief) dar.

## Zusammenfassung
Du hast ein Programm geschrieben, das dir hilft, Frachtbriefe zu verwalten. Du kannst Daten eingeben, speichern, suchen und 
anzeigen. Die Benutzeroberfläche ist mit PyQt5 erstellt, und die Daten werden in einer SQLite-Datenbank gespeichert. Das 
Programm kann auch HTML-Dateien erstellen, die den Frachtbrief darstellen, und diese im Browser öffnen.

---

## Die Zusammenhänge zwischen den einzelnen Codezeilen, Funktionen und Definitionen im Detail erklärt:

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
- **`import sys`**: Ermöglicht den Zugriff auf Systemfunktionen wie das Beenden des Programms. ([Python sys module](https://docs.python.org/3/library/sys.html))
- **`import sqlite3`**: Ermöglicht die Verwendung einer SQLite-Datenbank zur Speicherung der Frachtbriefdaten. ([Python sqlite3 module](https://docs.python.org/3/library/sqlite3.html))
- **`import webbrowser`**: Ermöglicht das Öffnen von HTML-Dateien im Webbrowser. ([Python webbrowser module](https://docs.python.org/3/library/webbrowser.html))
- **`from PyQt5.QtWidgets import ...`**: Importiert verschiedene Widgets und Layouts aus der PyQt5-Bibliothek, um die Benutzeroberfläche zu erstellen. ([PyQt5 QtWidgets module](https://doc.qt.io/qtforpython-5/PySide2/QtWidgets/index.html))
- **`from PyQt5.QtCore import Qt, QPoint`**: Importiert grundlegende Qt-Funktionen und -Typen. ([PyQt5 QtCore module](https://doc.qt.io/qtforpython-5/PySide2/QtCore/index.html))

### Die Hauptklasse (`MainWindow`)
```python
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
```
- **`class MainWindow(QMainWindow):`**: Definiert eine Klasse namens `MainWindow`, die von `QMainWindow` erbt. `QMainWindow` ist ein Standard-Fenstertyp in PyQt5. ([QMainWindow](https://doc.qt.io/qtforpython-5/PySide2/QtWidgets/QMainWindow.html))
- **`def __init__(self):`**: Konstruktor der Klasse, wird aufgerufen, wenn eine Instanz von `MainWindow` erstellt wird. ([__init__ method](https://docs.python.org/3/tutorial/classes.html#class-and-instance-variables))
- **`super().__init__()`**: Ruft den Konstruktor der Basisklasse `QMainWindow` auf, um sicherzustellen, dass alle Initialisierungen der Basisklasse durchgeführt werden. ([super()](https://docs.python.org/3/library/functions.html#super))
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
- **`self.setWindowTitle('Frachtbriefe / Waybills')`**
