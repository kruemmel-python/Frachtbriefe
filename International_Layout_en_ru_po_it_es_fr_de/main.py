import sys  # sys hilft uns, mit dem Computer zu sprechen
import sqlite3  # sqlite3 ist wie ein großes Notizbuch, in das wir Daten schreiben können
import webbrowser  # webbrowser öffnet den Internetbrowser
from PyQt5.QtWidgets import (QApplication, QMainWindow, QAction, QMenu, QWidget, QVBoxLayout, 
                             QFormLayout, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem, 
                             QHeaderView, QHBoxLayout, QSplitter)  # PyQt5 sind Bausteine, um Fenster und Buttons zu bauen
from PyQt5.QtCore import Qt, QPoint  # Qt und QPoint sind Helfer, um Dinge im Fenster anzuordnen

# FIELDS ist eine Liste von Dingen, die wir in unser Formular schreiben wollen
FIELDS = ['AusstellungsDatum', 'Ausstellungsort', 'AbsenderName', 'AbsenderAnschrift', 'AbsenderTelefon', 
          'AbsenderEmail', 'EmpfaengerName', 'EmpfaengerAnschrift', 'EmpfaengerTelefon', 'EmpfaengerEmail', 
          'FrachtfuehrerName', 'FrachtfuehrerAnschrift', 'FrachtfuehrerTelefon', 'FrachtfuehrerEmail', 'Frachtgut', 
          'Verpackung', 'FrachtstueckeAnzahl', 'Gesamtgewicht', 'Bemerkungen', 'Abholort', 'Abholdatum', 'Lieferort', 
          'Lieferdatum', 'Transportart', 'Versicherungsdetails']

# MainWindow ist das große Hauptfenster
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()  # Das ruft die Eltern-Klasse auf, um alles zu initialisieren
        self.initUI()  # Das ist unsere eigene Funktion, um das Fenster zu bauen

    def initUI(self):
        self.setWindowTitle('Frachtbriefe')  # Das ist der Titel oben im Fenster
        self.setGeometry(100, 100, 1200, 800)  # Das setzt die Größe und Position des Fensters (x, y, Breite, Höhe)
        menubar = self.menuBar()  # Das erstellt eine Menüleiste oben im Fenster
        # Hier erstellen wir zwei Menüs: eines für internationale und eines für nationale Frachtbriefe
        for title, table in [('Internationaler Frachtbrief', 'internationalefrachtbriefe'), 
                             ('Nationaler Frachtbrief', 'nationalefrachtbriefe')]:
            menu = menubar.addMenu(title)  # Fügt ein Menü zur Menüleiste hinzu
            # Wir fügen zwei Aktionen hinzu: "Daten erfassen" und "Daten abrufen"
            for action_title, method in [('Daten erfassen', self.erfassen), ('Daten abrufen', self.abrufen)]:
                action = QAction(action_title, self)  # Erstellt eine neue Aktion im Menü
                action.triggered.connect(lambda _, m=method, t=table: m(t))  # Verbindet die Aktion mit einer Funktion
                menu.addAction(action)  # Fügt die Aktion zum Menü hinzu

    def erfassen(self, table): self.setCentralWidget(ErfassenForm(table))  # Setzt das zentrale Widget auf das Erfassungsformular
    def abrufen(self, table): self.setCentralWidget(AbrufenForm(table))  # Setzt das zentrale Widget auf das Abrufformular

# ErfassenForm ist das Formular, um Daten zu erfassen (also einzugeben)
class ErfassenForm(QWidget):
    def __init__(self, table):
        super().__init__()  # Ruft die Eltern-Klasse auf, um alles zu initialisieren
        self.table = table  # Speichert den Tabellennamen
        self.initUI()  # Das ist unsere eigene Funktion, um das Formular zu bauen

    def initUI(self):
        layout = QVBoxLayout()  # Das ist ein Layout, bei dem die Elemente untereinander angeordnet werden
        formLayout = QFormLayout()  # Das ist ein Layout für Formulare, wo wir Beschriftungen und Eingabefelder haben
        self.fields = {field: QLineEdit() for field in FIELDS}  # Erstellt Eingabefelder für jedes Feld in FIELDS
        for field, widget in self.fields.items():
            formLayout.addRow(field, widget)  # Fügt jedes Eingabefeld zum Formular-Layout hinzu
        self.submitButton = QPushButton('Speichern')  # Ein Knopf zum Speichern der Daten
        self.submitButton.clicked.connect(self.submitData)  # Verbindet den Knopf mit der Funktion submitData
        layout.addLayout(formLayout)  # Fügt das Formular-Layout zum Hauptlayout hinzu
        layout.addWidget(self.submitButton)  # Fügt den Knopf zum Hauptlayout hinzu
        self.setLayout(layout)  # Setzt das Hauptlayout für das Widget

    def submitData(self):
        conn = sqlite3.connect('frachtbriefe.db')  # Verbindet sich mit der Datenbank
        cursor = conn.cursor()  # Das ist wie ein Stift, um in die Datenbank zu schreiben
        columns = ', '.join(self.fields.keys())  # Macht eine Liste der Spaltennamen, getrennt durch Kommas
        placeholders = ', '.join('?' * len(self.fields))  # Macht Platzhalter für die Werte
        query = f'INSERT INTO {self.table} ({columns}) VALUES ({placeholders})'  # Das ist unser SQL-Befehl zum Einfügen der Daten
        values = [widget.text() for widget in self.fields.values()]  # Holt die Werte aus den Eingabefeldern
        cursor.execute(query, values)  # Führt den SQL-Befehl aus und fügt die Daten ein
        conn.commit()  # Speichert die Änderungen in der Datenbank
        conn.close()  # Schließt die Verbindung zur Datenbank

# AbrufenForm ist das Formular, um Daten abzurufen (also anzuzeigen)
class AbrufenForm(QWidget):
    def __init__(self, table):
        super().__init__()  # Ruft die Eltern-Klasse auf, um alles zu initialisieren
        self.table = table  # Speichert den Tabellennamen
        self.initUI()  # Das ist unsere eigene Funktion, um das Formular zu bauen

    def initUI(self):
        layout = QHBoxLayout()  # Ein Layout, bei dem die Elemente nebeneinander angeordnet werden
        splitter = QSplitter(Qt.Horizontal)  # Ein Splitter, der zwei Widgets nebeneinander anordnet
        searchWidget = QWidget()  # Das Widget für die Suchfelder
        searchLayout = QFormLayout()  # Ein Formular-Layout für die Suchfelder
        self.searchFields = {field: QLineEdit() for field in ['FrachtbriefID'] + FIELDS}  # Erstellt Suchfelder für jedes Feld
        for field, widget in self.searchFields.items():
            searchLayout.addRow(field, widget)  # Fügt jedes Suchfeld zum Formular-Layout hinzu
        self.searchButton = QPushButton('Suchen')  # Ein Knopf zum Suchen der Daten
        self.searchButton.clicked.connect(self.searchData)  # Verbindet den Knopf mit der Funktion searchData
        searchLayout.addWidget(self.searchButton)  # Fügt den Knopf zum Formular-Layout hinzu
        searchWidget.setLayout(searchLayout)  # Setzt das Formular-Layout für das Widget
        splitter.addWidget(searchWidget)  # Fügt das Such-Widget zum Splitter hinzu
        self.tableWidget = QTableWidget()  # Ein Tabellen-Widget zur Anzeige der Suchergebnisse
        self.tableWidget.setColumnCount(len(self.searchFields))  # Setzt die Anzahl der Spalten in der Tabelle
        self.tableWidget.setHorizontalHeaderLabels(self.searchFields.keys())  # Setzt die Überschriften für die Spalten
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)  # Erlaubt das Ändern der Spaltenbreite
        self.tableWidget.horizontalHeader().setContextMenuPolicy(Qt.CustomContextMenu)  # Erlaubt ein Kontextmenü für die Spaltenüberschriften
        self.tableWidget.horizontalHeader().customContextMenuRequested.connect(self.showHeaderContextMenu)  # Verbindet das Kontextmenü mit der Funktion showHeaderContextMenu
        self.tableWidget.setContextMenuPolicy(Qt.CustomContextMenu)  # Erlaubt ein Kontextmenü für die Tabellenzeilen
        self.tableWidget.customContextMenuRequested.connect(self.showRowContextMenu)  # Verbindet das Kontextmenü mit der Funktion showRowContextMenu
        splitter.addWidget(self.tableWidget)  # Fügt das Tabellen-Widget zum Splitter hinzu
        layout.addWidget(splitter)  # Fügt den Splitter zum Hauptlayout hinzu
        self.setLayout(layout)  # Setzt das Hauptlayout für das Widget

    def searchData(self):
        conn = sqlite3.connect('frachtbriefe.db')  # Verbindet sich mit der Datenbank
        cursor = conn.cursor()  # Das ist wie ein Stift, um in die Datenbank zu schreiben
        conditions = [f"{field} LIKE ?" for field, widget in self.searchFields.items() if widget.text()]  # Erstellt die Bedingungen für die SQL-Abfrage
        values = [f"{widget.text()}%" for widget in self.searchFields.values() if widget.text()]  # Holt die Werte aus den Suchfeldern
        query = f"SELECT * FROM {self.table}" + (" WHERE " + " AND ".join(conditions) if conditions else "")  # Das ist unser SQL-Befehl zum Abrufen der Daten
        cursor.execute(query, values)  # Führt den SQL-Befehl aus und holt die Daten
        results = cursor.fetchall()  # Holt alle Ergebnisse der Abfrage
        self.tableWidget.setRowCount(len(results))  # Setzt die Anzahl der Zeilen in der Tabelle
        for row_idx, row_data in enumerate(results):
            for col_idx, col_data in enumerate(row_data):
                self.tableWidget.setItem(row_idx, col_idx, QTableWidgetItem(str(col_data)))  # Fügt die Daten in die Tabelle ein
        conn.close()  # Schließt die Verbindung zur Datenbank

    def showHeaderContextMenu(self, pos: QPoint):
        header = self.tableWidget.horizontalHeader()  # Holt die Spaltenüberschrift
        logicalIndex = header.logicalIndexAt(pos)  # Holt den Index der Spalte
        menu = QMenu()  # Erstellt ein Kontextmenü
        resizeAction = QAction('Optimale Breite', self)  # Erstellt eine Aktion zum Anpassen der Spaltenbreite
        resizeAction.triggered.connect(lambda: self.tableWidget.resizeColumnToContents(logicalIndex))  # Verbindet die Aktion mit der Funktion resizeColumnToContents
        menu.addAction(resizeAction)  # Fügt die Aktion zum Menü hinzu
        menu.exec(header.mapToGlobal(pos))  # Zeigt das Menü an der richtigen Stelle an

    def showRowContextMenu(self, pos: QPoint):
        row = self.tableWidget.rowAt(pos.y())  # Holt den Index der Zeile
        if row < 0: return  # Wenn keine Zeile angeklickt wurde, nichts tun
        menu = QMenu()  # Erstellt ein Kontextmenü
        createAction = QAction('Erstelle Frachtbrief', self)  # Erstellt eine Aktion zum Erstellen eines Frachtbriefs
        createAction.triggered.connect(lambda: self.createFrachtbrief(row))  # Verbindet die Aktion mit der Funktion createFrachtbrief
        menu.addAction(createAction)  # Fügt die Aktion zum Menü hinzu
        menu.exec(self.tableWidget.viewport().mapToGlobal(pos))  # Zeigt das Menü an der richtigen Stelle an

    def createFrachtbrief(self, row):
        data = {self.tableWidget.horizontalHeaderItem(col).text(): self.tableWidget.item(row, col).text() for col in range(self.tableWidget.columnCount())}  # Holt die Daten aus der Zeile
        template_path = 'if.html' if self.table == 'internationalefrachtbriefe' else 'nf.html'  # Wählt die richtige Vorlage
        with open(template_path, 'r', encoding='utf-8') as file:  # Öffnet die Vorlage
            html_content = file.read()  # Liest den Inhalt der Vorlage
        for key, value in data.items():
            html_content = html_content.replace(f'{{{{ {key} }}}}', value)  # Ersetzt die Platzhalter durch die Daten
        filename = f'{data["FrachtbriefID"]}_{data["AusstellungsDatum"]}_{data["EmpfaengerName"]}.html'.replace(" ", "_")  # Erstellt den Dateinamen
        with open(filename, 'w', encoding='utf-8') as file:  # Schreibt den Inhalt in die neue Datei
            file.write(html_content)  # Speichert die Datei
        webbrowser.open(filename)  # Öffnet die Datei im Webbrowser

if __name__ == '__main__':
    app = QApplication(sys.argv)  # Das startet unsere Anwendung
    mainWindow = MainWindow()  # Das erstellt das Hauptfenster
    mainWindow.show()  # Das zeigt das Hauptfenster an
    sys.exit(app.exec_())  # Das sorgt dafür, dass das Programm läuft, bis wir es schließen
