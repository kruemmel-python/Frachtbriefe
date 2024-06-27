# Importiere notwendige Module und Klassen
import sys  
# Ermöglicht den Zugriff auf einige Variablen und Funktionen, die vom Interpreter verwaltet werden. 
[sys-Dokumentation](https://docs.python.org/3/library/sys.html)
import sqlite3 
# Bietet eine Schnittstelle zur SQLite-Datenbank, um Datenbankoperationen durchzuführen. 
[sqlite3-Dokumentation](https://docs.python.org/3/library/sqlite3.html)
import webbrowser  
# Ermöglicht die Steuerung von Webbrowsern zum Öffnen von Webseiten. 
[webbrowser-Dokumentation](https://docs.python.org/3/library/webbrowser.html)
from PyQt5.QtWidgets import (QApplication, QMainWindow, QAction, QMenu, QWidget,
                             QVBoxLayout, QFormLayout, QLineEdit, QPushButton,
                             QTableWidget, QTableWidgetItem, QHeaderView, QHBoxLayout, 
                             QSplitter, QScrollArea, QLabel) 
# Importiert notwendige PyQt5-Komponenten für die Erstellung der GUI. 
[PyQt5-Dokumentation](https://www.riverbankcomputing.com/software/pyqt/intro)
from PyQt5.QtCore import Qt, QPoint 
# Importiert grundlegende PyQt5-Funktionalitäten und Typen. 
[QtCore-Dokumentation](https://doc.qt.io/qt-5/qtcore-module.html)
from PyQt5.QtGui import QFont, QPixmap  
# Importiert GUI-spezifische Funktionen wie Schriftarten und Bilder. 
[QtGui-Dokumentation](https://doc.qt.io/qt-5/qtgui-module.html)

# Definiere die Hauptfensterklasse, die von QMainWindow erbt

    class MainWindow(QMainWindow):
      def __init__(self):
          super().__init__() 
        
  # Initialisiert die Elternklasse QMainWindow. 
        
  [super()-Dokumentation](https://docs.python.org/3/library/functions.html#super)
        
        self.initUI()  
 # Ruft die Methode zur Initialisierung der Benutzeroberfläche auf

def initUI(self):
        self.setWindowTitle('Frachtbriefe / Waybills')  
        
        # Setzt den Fenstertitel.
 [setWindowTitle-Dokumentation](https://doc.qt.io/qt-5/qwidget.html#setWindowTitle)
 
        self.setGeometry(100, 100, 1200, 800) 
        # Setzt die Position und Größe des Fensters. 
  [setGeometry-Dokumentation](https://doc.qt.io/qt-5/qwidget.html#setGeometry)
  
        self.setStyleSheet("background-color: #2e2e2e; color: #ffffff;")  
 # Setzt das Stylesheet für das Fenster.
[setStyleSheet-Dokumentation](https://doc.qt.io/qt-5/stylesheet.html)

# Erstelle ein zentrales Widget, das das Logo und andere Inhalte enthält
        self.centralWidget = QWidget(self)  
  # Erzeugt ein zentrales Widget.
 [QWidget-Dokumentation](https://doc.qt.io/qt-5/qwidget.html)
 
        self.setCentralWidget(self.centralWidget)  
        # Setzt das zentrale Widget. 
 [setCentralWidget-Dokumentation](https://doc.qt.io/qt-5/qmainwindow.html#setCentralWidget)

        self.layout = QVBoxLayout(self.centralWidget)  
  # Verwendet ein vertikales Layout für das zentrale Widget. 
   [QVBoxLayout-Dokumentation](https://doc.qt.io/qt-5/qvboxlayout.html)
        
  # Füge das Logo mit fester Größe 640x480 hinzu
        self.logoLabel = QLabel(self)         
  # Erzeugt ein QLabel-Widget.  
  
        [QLabel-Dokumentation](https://doc.qt.io/qt-5/qlabel.html)
        self.logoLabel.setFixedSize(640, 480)  
  # Setzt die feste Größe für das Logo. 
  [setFixedSize-Dokumentation](https://doc.qt.io/qt-5/qwidget.html#setFixedSize)
  
        self.logoLabel.setPixmap(QPixmap("logo.jpg").scaled(640, 480, Qt.KeepAspectRatio, Qt.SmoothTransformation))  
  # Setzt das Bild für das QLabel und skaliert es. 
   [QPixmap-Dokumentation](https://doc.qt.io/qt-5/qpixmap.html)
   
        self.logoLabel.setAlignment(Qt.AlignCenter)  
  # Zentriert das Bild im QLabel. 
  [setAlignment-Dokumentation](https://doc.qt.io/qt-5/qlabel.html#setAlignment)
  
        self.layout.addWidget(self.logoLabel, alignment=Qt.AlignCenter)  
 # Fügt das QLabel zum Layout hinzu.
 [addWidget-Dokumentation](https://doc.qt.io/qt-5/qlayout.html#addWidget)

 # Erstelle die Menüleiste und setze ihren Stil
        menubar = self.menuBar()  
  # Erzeugt die Menüleiste. 
  [menuBar-Dokumentation](https://doc.qt.io/qt-5/qmainwindow.html#menuBar)
  
        menubar.setStyleSheet("background-color: #1e1e1e; color: #ffffff;") 
  # Setzt das Stylesheet für die Menüleiste. 
   [setStyleSheet-Dokumentation](https://doc.qt.io/qt-5/stylesheet.html)
       
  # Füge Menüs zur Menüleiste hinzu
        self.createMenu(menubar, 'Internationaler Frachtbrief / International Waybill', self.erfassenInternational, self.abrufenInternational)  
  # Erstellt ein Menü für internationale Frachtbriefe.
  [createMenu-Dokumentation](https://doc.qt.io/qt-5/qmenu.html)
    
      self.createMenu(menubar, 'Nationaler Frachtbrief / National Waybill', self.erfassenNational, self.abrufenNational)  
   # Erstellt ein Menü für nationale Frachtbriefe.

    def createMenu(self, menubar, title, erfassen, abrufen):
        menu = menubar.addMenu(title)  
  # Fügt der Menüleiste ein Menü hinzu. 
  [addMenu-Dokumentation](https://doc.qt.io/qt-5/qmenubar.html#addMenu)
       
        menu.setStyleSheet("background-color: #1e1e1e; color: #ffffff;")  
  # Setzt das Stylesheet für das Menü. 
   [setStyleSheet-Dokumentation](https://doc.qt.io/qt-5/stylesheet.html)
   
        erfassenAction = QAction('Daten erfassen / Enter Data', self)  
  # Erstellt eine Aktion zum Erfassen von Daten.
  [QAction-Dokumentation](https://doc.qt.io/qt-5/qaction.html)
  
        erfassenAction.triggered.connect(erfassen)  
  # Verbindet die Aktion mit der entsprechenden Methode. 
  [triggered-Dokumentation](https://doc.qt.io/qt-5/qaction.html#triggered)
  
        menu.addAction(erfassenAction)  
   # Fügt die Aktion zum Menü hinzu. 
   [addAction-Dokumentation](https://doc.qt.io/qt-5/qmenu.html#addAction)
   
        abrufenAction = QAction('Daten abrufen / Retrieve Data', self)  
   # Erstellt eine Aktion zum Abrufen von Daten.
   
        abrufenAction.triggered.connect(abrufen)  
  # Verbindet die Aktion mit der entsprechenden Methode.
  
        menu.addAction(abrufenAction)  
  # Fügt die Aktion zum Menü hinzu.

    def erfassenInternational(self): 
        self.setCentralWidget(ErfassenForm('internationalefrachtbriefe'))  
  # Setzt das zentrale Widget auf das Formular zum Erfassen von internationalen Frachtbriefen. 
  [setCentralWidget-Dokumentation](https://doc.qt.io/qt-5/qmainwindow.html#setCentralWidget)

    def abrufenInternational(self): 
        self.setCentralWidget(AbrufenForm('internationalefrachtbriefe'))  
   # Setzt das zentrale Widget auf das Formular zum Abrufen von internationalen Frachtbriefen.

    def erfassenNational(self): 
        self.setCentralWidget(ErfassenForm('nationalefrachtbriefe'))  
   # Setzt das zentrale Widget auf das Formular zum Erfassen von nationalen Frachtbriefen.

    def abrufenNational(self): 
        self.setCentralWidget(AbrufenForm('nationalefrachtbriefe'))  
    # Setzt das zentrale Widget auf das Formular zum Abrufen von nationalen Frachtbriefen.

    def clearCentralWidget(self):
  # Löscht das zentrale Widget, bevor ein neues gesetzt wird
        if self.centralWidget:
            layout = self.centralWidget.layout()  
   # Holt das Layout des zentralen Widgets. 
   [layout-Dokumentation](https://doc.qt.io/qt-5/qwidget.html#layout)
   
            if layout:
                while layout.count():
                    child = layout.takeAt(0)  
  # Nimmt das erste Widget aus dem Layout. 
  [takeAt-Dokumentation](https://doc.qt.io/qt-5/qlayout.html#takeAt)
  
                    if child.widget():
                        child.widget().deleteLater()  
   # Löscht das Widget später. 
   [deleteLater-Dokumentation](https://doc.qt.io/qt-5/qobject.html#deleteLater)
   
            QWidget().setLayout(self.centralWidget.layout())  
   # Setzt das Layout des zentralen Widgets auf ein neues leeres Layout.


# Definiere die Klasse für das Daten-Eingabeformular
    class ErfassenForm(QWidget):
        def __init__(self, table):
            super().__init__() 
  # Initialisiert die Elternklasse QWidget.
  
            self.table = table 
  # Setzt den Tabellennamen.
  
            self.initUI()  
  # Ruft die Methode zur Initialisierung der Benutzeroberfläche auf

    def initUI(self):
        layout = QVBoxLayout()  
   # Erzeugt ein vertikales Layout.
   
        formLayout = QFormLayout()  
  # Erzeugt ein Formular-Layout. 
  [QFormLayout-Dokumentation](https://doc.qt.io/qt-5/qformlayout.html)
  
        self.fields = {  
  # Erstellt ein Wörterbuch für die Eingabefelder.
            'AusstellungsDatum / Date of Issue': QLineEdit(),  
   # Erstellt ein Eingabefeld. 
            [QLineEdit-Dokumentation](https://doc.qt.io/qt-5/qlineedit.html)
            'Ausstellungsort / Place of Issue': QLineEdit(),
            'AbsenderName / Sender Name': QLineEdit(),
            'AbsenderAnschrift / Sender Address': QLineEdit(),
            'AbsenderTelefon / Sender Phone': QLineEdit(),
            'AbsenderEmail / Sender Email': QLineEdit(),
            'EmpfaengerName / Recipient Name': QLineEdit(),
            'EmpfaengerAnschrift / Recipient Address': QLineEdit(),
            'EmpfaengerTelefon / Recipient Phone': QLineEdit(),
            'EmpfaengerEmail / Recipient Email': QLineEdit(),
            'FrachtfuehrerName / Carrier Name': QLineEdit(),
            'FrachtfuehrerAnschrift / Carrier Address': QLineEdit(),
            'FrachtfuehrerTelefon / Carrier Phone': QLineEdit(),
            'FrachtfuehrerEmail / Carrier Email': QLineEdit(),
            'Frachtgut / Goods': QLineEdit(),
            'Verpackung / Packaging': QLineEdit(),
            'FrachtstueckeAnzahl / Number of Packages': QLineEdit(),
            'Gesamtgewicht / Total Weight': QLineEdit(),
            'Bemerkungen / Remarks': QLineEdit(),
            'Abholort / Pickup Location': QLineEdit(),
            'Abholdatum / Pickup Date': QLineEdit(),
            'Lieferort / Delivery Location': QLineEdit(),
            'Lieferdatum / Delivery Date': QLineEdit(),
            'Transportart / Mode of Transport': QLineEdit(),
            'Versicherungsdetails / Insurance Details': QLineEdit()
        }

        font = QFont()  
  # Erstellt eine Schriftart. 
  [QFont-Dokumentation](https://doc.qt.io/qt-5/qfont.html)
  
        font.setPointSize(12) 
  # Setzt die Schriftgröße. 
  [setPointSize-Dokumentation](https://doc.qt.io/qt-5/qfont.html#setPointSize)
        
        for field, widget in self.fields.items():
            widget.setFont(font)  
   # Setzt die Schriftart für das Eingabefeld.
   
            widget.setStyleSheet("padding: 10px; border: 1px solid #444; border-radius: 5px; color: #ffffff; background-color: #333;")  
   # Setzt das Stylesheet für das Eingabefeld.
   
            formLayout.addRow(field, widget)  
   # Fügt das Eingabefeld dem Formular-Layout hinzu. 
   [addRow-Dokumentation](https://doc.qt.io/qt-5/qformlayout.html#addRow)

        self.submitButton = QPushButton('Speichern / Save') 
   # Erstellt einen Speichern-Button. 
   [QPushButton-Dokumentation](https://doc.qt.io/qt-5/qpushbutton.html)
   
        self.submitButton.setFont(font)  
   # Setzt die Schriftart für den Button.
   
        self.submitButton.setStyleSheet("background-color: #007BFF; color: white; padding: 10px; border-radius: 5px;")  
   # Setzt das Stylesheet für den Button
   
        self.submitButton.clicked.connect(self.submitData)  
   # Verbindet den Button mit der Methode zum Speichern der Daten. 
   [clicked-Dokumentation](https://doc.qt.io/qt-5/qabstractbutton.html#clicked)

        layout.addLayout(formLayout)  
   # Fügt das Formular-Layout dem Hauptlayout hinzu.
   
        layout.addWidget(self.submitButton)  
   # Fügt den Button dem Hauptlayout hinzu.

        scrollArea = QScrollArea() 
   # Erstellt ein Scrollbereich-Widget. 
   [QScrollArea-Dokumentation](https://doc.qt.io/qt-5/qscrollarea.html)
   
        scrollArea.setWidgetResizable(True)  
  # Ermöglicht die Größenanpassung des Widgets im Scrollbereich. 
  [setWidgetResizable-Dokumentation](https://doc.qt.io/qt-5/qscrollarea.html#setWidgetResizable)
  
        container = QWidget()  
   # Erstellt ein Container-Widget. 
   [QWidget-Dokumentation](https://doc.qt.io/qt-5/qwidget.html)
   
        container.setLayout(layout)  
 # Setzt das Layout des Container-Widgets. 
 [setLayout-Dokumentation](https://doc.qt.io/qt-5/qwidget.html#setLayout)
 
        scrollArea.setWidget(container)  
 # Setzt das Container-Widget in den Scrollbereich. 
 [setWidget-Dokumentation](https://doc.qt.io/qt-5/qscrollarea.html#setWidget)

        mainLayout = QVBoxLayout()  
 # Erstellt ein Hauptlayout.
 [QVBoxLayout-Dokumentation](https://doc.qt.io/qt-5/qvboxlayout.html)
 
        mainLayout.addWidget(scrollArea) 
  # Fügt den Scrollbereich dem Hauptlayout hinzu. 
  [addWidget-Dokumentation](https://doc.qt.io/qt-5/qlayout.html#addWidget)
  
        self.setLayout(mainLayout) 
  # Setzt das Hauptlayout für das Eingabeformular-Widget.

    def submitData(self):
        conn = sqlite3.connect('frachtbriefe.db') 
   # Stellt eine Verbindung zur SQLite-Datenbank her.
   [sqlite3.connect-Dokumentation](https://docs.python.org/3/library/sqlite3.html#sqlite3.connect)
   
        cursor = conn.cursor()  
   # Erstellt einen Cursor für die Datenbankoperationen. 
   [cursor-Dokumentation](https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor)
   
        columns = ', '.join(self.fields.keys())  
   # Bereitet die Spaltennamen für die SQL-Abfrage vor.
   
        placeholders = ', '.join('?' * len(self.fields))  
   # Erstellt Platzhalter für die Werte in der SQL-Abfrage.
   
        query = f'INSERT INTO {self.table} ({columns}) VALUES ({placeholders})'  
   # Erstellt die SQL-Abfrage zum Einfügen von Daten.
   
        [SQL INSERT INTO-Dokumentation](https://www.w3schools.com/sql/sql_insert.asp)
        values = [widget.text() for widget in self.fields.values()] 
   # Holt die Werte aus den Eingabefeldern.
   
        cursor.execute(query, values)  
   # Führt die SQL-Abfrage aus. 
   [execute-Dokumentation](https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor.execute)
   
        conn.commit()  
   # Bestätigt die Transaktion. 
   [commit-Dokumentation](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.commit)
   
        conn.close()  
   # Schließt die Datenbankverbindung. 
   [close-Dokumentation](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.close)

# Definiere die Klasse für das Daten-Abfrageformular
    class AbrufenForm(QWidget):
      def __init__(self, table):
      
          super().__init__()  
# Initialisiert die Elternklasse QWidget.

        self.table = table  
  # Setzt den Tabellennamen.
  
        self.initUI()  
 # Ruft die Methode zur Initialisierung der Benutzeroberfläche auf

    def initUI(self):
        layout = QHBoxLayout()  
   # Erzeugt ein horizontales Layout.
   
        splitter = QSplitter(Qt.Horizontal)  
   # Erstellt einen Splitter für die horizontale Aufteilung. 
   [QSplitter-Dokumentation](https://doc.qt.io/qt-5/qsplitter.html)
   
        searchWidget = QWidget()  
   # Erstellt ein Widget für die Suchfelder.
   
        searchLayout = QFormLayout()  
   # Erstellt ein Formular-Layout für die Suchfelder.
   [QFormLayout-Dokumentation](https://doc.qt.io/qt-5/qformlayout.html)
   
        self.searchFields = {  
   # Erstellt ein Wörterbuch für die Suchfelder.
   
            'FrachtbriefID / Waybill ID': QLineEdit(),  
   # Erstellt ein Eingabefeld für die Suche.
   
            [QLineEdit-Dokumentation](https://doc.qt.io/qt-5/qlineedit.html)
            'AusstellungsDatum / Date of Issue': QLineEdit(),
            'Ausstellungsort / Place of Issue': QLineEdit(),
            'AbsenderName / Sender Name': QLineEdit(),
            'AbsenderAnschrift / Sender Address': QLineEdit(),
            'AbsenderTelefon / Sender Phone': QLineEdit(),
            'AbsenderEmail / Sender Email': QLineEdit(),
            'EmpfaengerName / Recipient Name': QLineEdit(),
            'EmpfaengerAnschrift / Recipient Address': QLineEdit(),
            'EmpfaengerTelefon / Recipient Phone': QLineEdit(),
            'EmpfaengerEmail / Recipient Email': QLineEdit(),
            'FrachtfuehrerName / Carrier Name': QLineEdit(),
            'FrachtfuehrerAnschrift / Carrier Address': QLineEdit(),
            'FrachtfuehrerTelefon / Carrier Phone': QLineEdit(),
            'FrachtfuehrerEmail / Carrier Email': QLineEdit(),
            'Frachtgut / Goods': QLineEdit(),
            'Verpackung / Packaging': QLineEdit(),
            'FrachtstueckeAnzahl / Number of Packages': QLineEdit(),
            'Gesamtgewicht / Total Weight': QLineEdit(),
            'Bemerkungen / Remarks': QLineEdit(),
            'Abholort / Pickup Location': QLineEdit(),
            'Abholdatum / Pickup Date': QLineEdit(),
            'Lieferort / Delivery Location': QLineEdit(),
            'Lieferdatum / Delivery Date': QLineEdit(),
            'Transportart / Mode of Transport': QLineEdit(),
            'Versicherungsdetails / Insurance Details': QLineEdit()
        }

        font = QFont() 
 # Erstellt eine Schriftart.
 
        font.setPointSize(12) 
  # Setzt die Schriftgröße.

        for field, widget in self.searchFields.items():
            widget.setFont(font)  
   # Setzt die Schriftart für das Suchfeld.
   
            widget.setStyleSheet("padding: 10px; border: 1px solid #444; border-radius: 5px; color: #ffffff; background-color: #333;")  
  # Setzt das Stylesheet für das Suchfeld.
  
            searchLayout.addRow(field, widget)  
  # Fügt das Suchfeld dem Formular-Layout hinzu.

        self.searchButton = QPushButton('Suchen / Search')  
 # Erstellt einen Such-Button.
 
        self.searchButton.setFont(font)  
 # Setzt die Schriftart für den Button.
 
        self.searchButton.setStyleSheet("background-color: #007BFF; color: white; padding: 10px; border-radius: 5px;")  
  # Setzt das Stylesheet für den Button.
  
        self.searchButton.clicked.connect(self.searchData)  
 # Verbindet den Button mit der Methode zum Suchen von Daten.

        searchLayout.addWidget(self.searchButton)  
 # Fügt den Such-Button dem Formular-Layout hinzu.

        scrollArea = QScrollArea()  
 # Erstellt ein Scrollbereich-Widget.
 
        scrollArea.setWidgetResizable(True)  
 # Ermöglicht die Größenanpassung des Widgets im Scrollbereich.
 
        searchContainer = QWidget()  
 # Erstellt ein Container-Widget.
 
        searchContainer.setLayout(searchLayout)  
 # Setzt das Layout des Container-Widgets.
 
        scrollArea.setWidget(searchContainer)  
 # Setzt das Container-Widget in den Scrollbereich.

        splitter.addWidget(scrollArea)  
 # Fügt den Scrollbereich dem Splitter hinzu.

        self.tableWidget = QTableWidget()  
 # Erstellt ein Tabellen-Widget.
 
        self.tableWidget.setStyleSheet("background-color: #444; color: #ffffff; gridline-color: #ccc;")  
 # Setzt das Stylesheet für das Tabellen-Widget.
 
        self.tableWidget.setColumnCount(len(self.searchFields))  
 # Setzt die Anzahl der Spalten in der Tabelle.
 [setColumnCount-Dokumentation](https://doc.qt.io/qt-5/qtablewidget.html#setColumnCount)
 
        self.tableWidget.setHorizontalHeaderLabels(self.searchFields.keys()) 
        # Setzt die Überschriften der Spalten. 
        [setHorizontalHeaderLabels-Dokumentation](https://doc.qt.io/qt-5/qtablewidget.html#setHorizontalHeaderLabels)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)  
        # Ermöglicht die interaktive Größenanpassung der Spalten. 
        [setSectionResizeMode-Dokumentation](https://doc.qt.io/qt-5/qheaderview.html#setSectionResizeMode)
        self.tableWidget.horizontalHeader().setContextMenuPolicy(Qt.CustomContextMenu)  
        # Setzt die Richtlinie für das Kontextmenü der Kopfzeile. 
        [setContextMenuPolicy-Dokumentation](https://doc.qt.io/qt-5/qwidget.html#setContextMenuPolicy)
        self.tableWidget.horizontalHeader().customContextMenuRequested.connect(self.showHeaderContextMenu)  
        # Verbindet das Signal für das benutzerdefinierte Kontextmenü mit der entsprechenden Methode. 
        [customContextMenuRequested-Dokumentation](https://doc.qt.io/qt-5/qwidget.html#customContextMenuRequested)
        self.tableWidget.setContextMenuPolicy(Qt.CustomContextMenu)  
        # Setzt die Richtlinie für das Kontextmenü der Tabelle.
        self.tableWidget.customContextMenuRequested.connect(self.showRowContextMenu) 
        # Verbindet das Signal für das benutzerdefinierte Kontextmenü mit der entsprechenden Methode.

        # Setzt den Stil für die Kopfzeile der Tabelle
        self.tableWidget.setStyleSheet(
            """
            QHeaderView::section {background-color: #00ff00; color: black;}
            QTableWidget {background-color: #444; color: #ffffff; gridline-color: #ccc;}
            """
        )

        splitter.addWidget(self.tableWidget)  
        # Fügt das Tabellen-Widget dem Splitter hinzu.
        splitter.setSizes([300, 900])  
        # Setzt die anfänglichen Größen der Splitter-Bereiche.
        [setSizes-Dokumentation](https://doc.qt.io/qt-5/qsplitter.html#setSizes)
        layout.addWidget(splitter) 
        # Fügt den Splitter dem Hauptlayout hinzu.
        self.setLayout(layout)  
        # Setzt das Hauptlayout für das Abfrageformular-Widget.

    def searchData(self):
        conn = sqlite3.connect('frachtbriefe.db')  
        # Stellt eine Verbindung zur SQLite-Datenbank her.
        cursor = conn.cursor()  
        # Erstellt einen Cursor für die Datenbankoperationen.
        conditions = [f"{field.split(' / ')[0]} LIKE ?" for field, widget in self.searchFields.items() if widget.text()] 
        # Erstellt die Bedingungen für die SQL-Abfrage.
        values = [f"{widget.text()}%" for widget in self.searchFields.values() if widget.text()]  
        # Holt die Werte aus den Suchfeldern.
        query = f"SELECT * FROM {self.table}" + (" WHERE " + " AND ".join(conditions) if conditions else "")  
        # Erstellt die SQL-Abfrage zum Suchen von Daten.
        cursor.execute(query, values) 
        # Führt die SQL-Abfrage aus.
        results = cursor.fetchall() 
        # Holt alle Ergebnisse der Abfrage. 
        [fetchall-Dokumentation](https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor.fetchall)
        self.tableWidget.setRowCount(len(results))  
        # Setzt die Anzahl der Zeilen in der Tabelle. 
        [setRowCount-Dokumentation](https://doc.qt.io/qt-5/qtablewidget.html#setRowCount)
        for row_idx, row_data in enumerate(results):
            for col_idx, col_data in enumerate(row_data):
                self.tableWidget.setItem(row_idx, col_idx, QTableWidgetItem(str(col_data))) 
                # Fügt die Daten in die Tabelle ein. 
                [setItem-Dokumentation](https://doc.qt.io/qt-5/qtablewidget.html#setItem)
        conn.close()  # Schließt die Datenbankverbindung.

    def showHeaderContextMenu(self, pos: QPoint):
        header = self.tableWidget.horizontalHeader() 
        # Holt die horizontale Kopfzeile der Tabelle. 
        [horizontalHeader-Dokumentation](https://doc.qt.io/qt-5/qtablewidget.html#horizontalHeader)
        logicalIndex = header.logicalIndexAt(pos) 
        # Holt den logischen Index der Kopfzeile an der angegebenen Position.
        [logicalIndexAt-Dokumentation](https://doc.qt.io/qt-5/qheaderview.html#logicalIndexAt)
        menu = QMenu()  
        # Erstellt ein Kontextmenü. 
        [QMenu-Dokumentation](https://doc.qt.io/qt-5/qmenu.html)
        resizeAction = QAction('Optimale Breite / Optimal Width', self)  
        # Erstellt eine Aktion zum Anpassen der Spaltenbreite. 
        [QAction-Dokumentation](https://doc.qt.io/qt-5/qaction.html)
        resizeAction.triggered.connect(lambda: self.tableWidget.resizeColumnToContents(logicalIndex)) 
        # Verbindet die Aktion mit der Methode zum Anpassen der Spaltenbreite. 
        [resizeColumnToContents-Dokumentation](https://doc.qt.io/qt-5/qtableview.html#resizeColumnToContents)
        menu.addAction(resizeAction) 
        # Fügt die Aktion zum Menü hinzu.
        menu.exec(header.mapToGlobal(pos))  
        # Zeigt das Menü an der angegebenen Position an. 
        [exec-Dokumentation](https://doc.qt.io/qt-5/qmenu.html#exec)

    def showRowContextMenu(self, pos: QPoint):
        row = self.tableWidget.rowAt(pos.y())  
        # Holt die Zeile an der angegebenen Position. 
        [rowAt-Dokumentation](https://doc.qt.io/qt-5/qtablewidget.html#rowAt)
        if row < 0: return 
        # Wenn keine Zeile vorhanden ist, nichts tun.
        menu = QMenu() 
        # Erstellt ein Kontextmenü.
        
        createSubMenu = QMenu('Erstelle Frachtbrief / Create Waybill', self)  
        # Erstellt ein Untermenü zum Erstellen von Frachtbriefen.
        self.addLanguageActions(createSubMenu, row)  
        # Fügt Sprachoptionen zum Untermenü hinzu.
        
        menu.addMenu(createSubMenu)  
        # Fügt das Untermenü zum Kontextmenü hinzu.
        menu.exec(self.tableWidget.viewport().mapToGlobal(pos))  
        # Zeigt das Menü an der angegebenen Position an.

    def addLanguageActions(self, menu, row):
        languages = {  # Definiert die verfügbaren Sprachen.
            'Deutsch': 'de', 
            'Englisch': 'en', 
            'Russisch': 'ru', 
            'Polnisch': 'po', 
            'Italienisch': 'it', 
            'Französisch': 'fr', 
            'Spanisch': 'sp'
        }
        for language, code in languages.items():
            action = QAction(language, self)  
            # Erstellt eine Aktion für jede Sprache.
            action.triggered.connect(lambda _, c=code: self.createFrachtbrief(row, c))  
            # Verbindet die Aktion mit der Methode zum Erstellen eines Frachtbriefs. 
            [triggered-Dokumentation](https://doc.qt.io/qt-5/qaction.html#triggered)
            menu.addAction(action) 
            # Fügt die Aktion zum Menü hinzu.

    def createFrachtbrief(self, row, language_code):
        data = {self.tableWidget.horizontalHeaderItem(col).text(): self.tableWidget.item(row, col).text() for col in range(self.tableWidget.columnCount())}  
        # Holt die Daten aus der ausgewählten Zeile. 
        [horizontalHeaderItem-Dokumentation](https://doc.qt.io/qt-5/qtablewidget.html#horizontalHeaderItem)

        if self.table == 'internationalefrachtbriefe':
            template_path = f'if_{language_code}_frachtbrief.html' 
            # Setzt den Pfad zur internationalen Frachtbriefvorlage.
        else:
            template_path = f'nf_{language_code}_frachtbrief.html'  
            # Setzt den Pfad zur nationalen Frachtbriefvorlage.

        with open(template_path, 'r', encoding='utf-8') as file:  
        # Öffnet die HTML-Vorlage. 
        [open-Dokumentation](https://docs.python.org/3/library/functions.html#open)
            html_content = file.read()  
            # Liest den Inhalt der HTML-Vorlage. 
            [read-Dokumentation](https://docs.python.org/3/library/io.html#io.TextIOBase.read)

        for key, value in data.items():
            html_content = html_content.replace(f'{{{{ {key.split(" / ")[0]} }}}}', value)  
            # Ersetzt Platzhalter im HTML-Inhalt durch die Daten. 
            [replace-Dokumentation](https://docs.python.org/3/library/stdtypes.html#str.replace)

        filename = f'{data["FrachtbriefID / Waybill ID"]}_{data["AusstellungsDatum / Date of Issue"]}_{data["EmpfaengerName / Recipient Name"]}.html'.replace(" ", "_")  
        # Erzeugt den Dateinamen für den Frachtbrief. 
        [replace-Dokumentation](https://docs.python.org/3/library/stdtypes.html#str.replace)

        with open(filename, 'w', encoding='utf-8') as file: 
        # Öffnet die Datei zum Schreiben. 
        [open-Dokumentation](https://docs.python.org/3/library/functions.html#open)
            file.write(html_content)  
            # Schreibt den HTML-Inhalt in die Datei. 
            [write-Dokumentation](https://docs.python.org/3/library/io.html#io.TextIOBase.write)

        webbrowser.open(filename)  
        # Öffnet die HTML-Datei im Webbrowser. 
        [open-Dokumentation](https://docs.python.org/3/library/webbrowser.html#webbrowser.open)

# Überprüft, ob das Skript direkt ausgeführt wird
if __name__ == '__main__':
    app = QApplication(sys.argv)  
    # Erstellt die Anwendung. 
    [QApplication-Dokumentation](https://doc.qt.io/qt-5/qapplication.html)
    mainWindow = MainWindow()  
    # Erstellt das Hauptfenster. 
    mainWindow.show()  
    # Zeigt das Hauptfenster an. 
    [show-Dokumentation](https://doc.qt.io/qt-5/qwidget.html#show)
    sys.exit(app.exec())  
    # Startet die Haupt-Ereignisschleife und wartet, bis sie beendet ist. 
    [sys.exit-Dokumentation](https://docs.python.org/3/library/sys.html#sys.exit)
