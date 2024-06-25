import sys
import sqlite3
import webbrowser
from PyQt5.QtWidgets import (QApplication, QMainWindow, QAction, QMenu, QWidget, 
                             QVBoxLayout, QFormLayout, QLineEdit, QPushButton, 
                             QTableWidget, QTableWidgetItem, QHeaderView, QHBoxLayout, QSplitter)
from PyQt5.QtCore import Qt, QPoint

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Frachtbriefe')
        self.setGeometry(100, 100, 1200, 800)
        menubar = self.menuBar()
        self.createMenu(menubar, 'Internationaler Frachtbrief', self.erfassenInternational, self.abrufenInternational)
        self.createMenu(menubar, 'Nationaler Frachtbrief', self.erfassenNational, self.abrufenNational)

    def createMenu(self, menubar, title, erfassen, abrufen):
        menu = menubar.addMenu(title)
        erfassenAction = QAction('Daten erfassen', self)
        erfassenAction.triggered.connect(erfassen)
        menu.addAction(erfassenAction)
        abrufenAction = QAction('Daten abrufen', self)
        abrufenAction.triggered.connect(abrufen)
        menu.addAction(abrufenAction)

    def erfassenInternational(self): self.setCentralWidget(ErfassenForm('internationalefrachtbriefe'))
    def abrufenInternational(self): self.setCentralWidget(AbrufenForm('internationalefrachtbriefe'))
    def erfassenNational(self): self.setCentralWidget(ErfassenForm('nationalefrachtbriefe'))
    def abrufenNational(self): self.setCentralWidget(AbrufenForm('nationalefrachtbriefe'))

class ErfassenForm(QWidget):
    def __init__(self, table):
        super().__init__()
        self.table = table
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        formLayout = QFormLayout()
        self.fields = {field: QLineEdit() for field in [
            'AusstellungsDatum', 'Ausstellungsort', 'AbsenderName', 'AbsenderAnschrift', 'AbsenderTelefon', 
            'AbsenderEmail', 'EmpfaengerName', 'EmpfaengerAnschrift', 'EmpfaengerTelefon', 'EmpfaengerEmail', 
            'FrachtfuehrerName', 'FrachtfuehrerAnschrift', 'FrachtfuehrerTelefon', 'FrachtfuehrerEmail', 'Frachtgut', 
            'Verpackung', 'FrachtstueckeAnzahl', 'Gesamtgewicht', 'Bemerkungen', 'Abholort', 'Abholdatum', 'Lieferort', 
            'Lieferdatum', 'Transportart', 'Versicherungsdetails'
        ]}
        for field, widget in self.fields.items():
            formLayout.addRow(field, widget)
        self.submitButton = QPushButton('Speichern')
        self.submitButton.clicked.connect(self.submitData)
        layout.addLayout(formLayout)
        layout.addWidget(self.submitButton)
        self.setLayout(layout)

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

class AbrufenForm(QWidget):
    def __init__(self, table):
        super().__init__()
        self.table = table
        self.initUI()

    def initUI(self):
        layout = QHBoxLayout()
        splitter = QSplitter(Qt.Horizontal)
        searchWidget = QWidget()
        searchLayout = QFormLayout()
        self.searchFields = {field: QLineEdit() for field in [
            'FrachtbriefID', 'AusstellungsDatum', 'Ausstellungsort', 'AbsenderName', 'AbsenderAnschrift', 'AbsenderTelefon', 
            'AbsenderEmail', 'EmpfaengerName', 'EmpfaengerAnschrift', 'EmpfaengerTelefon', 'EmpfaengerEmail', 
            'FrachtfuehrerName', 'FrachtfuehrerAnschrift', 'FrachtfuehrerTelefon', 'FrachtfuehrerEmail', 'Frachtgut', 
            'Verpackung', 'FrachtstueckeAnzahl', 'Gesamtgewicht', 'Bemerkungen', 'Abholort', 'Abholdatum', 'Lieferort', 
            'Lieferdatum', 'Transportart', 'Versicherungsdetails'
        ]}
        for field, widget in self.searchFields.items():
            searchLayout.addRow(field, widget)
        self.searchButton = QPushButton('Suchen')
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

    def searchData(self):
        conn = sqlite3.connect('frachtbriefe.db')
        cursor = conn.cursor()
        conditions = [f"{field} LIKE ?" for field, widget in self.searchFields.items() if widget.text()]
        values = [f"{widget.text()}%" for widget in self.searchFields.values() if widget.text()]
        query = f"SELECT * FROM {self.table}" + (" WHERE " + " AND ".join(conditions) if conditions else "")
        cursor.execute(query, values)
        results = cursor.fetchall()
        self.tableWidget.setRowCount(len(results))
        for row_idx, row_data in enumerate(results):
            for col_idx, col_data in enumerate(row_data):
                self.tableWidget.setItem(row_idx, col_idx, QTableWidgetItem(str(col_data)))
        conn.close()

    def showHeaderContextMenu(self, pos: QPoint):
        header = self.tableWidget.horizontalHeader()
        logicalIndex = header.logicalIndexAt(pos)
        menu = QMenu()
        resizeAction = QAction('Optimale Breite', self)
        resizeAction.triggered.connect(lambda: self.tableWidget.resizeColumnToContents(logicalIndex))
        menu.addAction(resizeAction)
        menu.exec(header.mapToGlobal(pos))

    def showRowContextMenu(self, pos: QPoint):
        row = self.tableWidget.rowAt(pos.y())
        if row < 0: return
        menu = QMenu()
        createAction = QAction('Erstelle Frachtbrief', self)
        createAction.triggered.connect(lambda: self.createFrachtbrief(row))
        menu.addAction(createAction)
        menu.exec(self.tableWidget.viewport().mapToGlobal(pos))

    def createFrachtbrief(self, row):
        data = {self.tableWidget.horizontalHeaderItem(col).text(): self.tableWidget.item(row, col).text() for col in range(self.tableWidget.columnCount())}
        template_path = 'if.html' if self.table == 'internationalefrachtbriefe' else 'nf.html'
        with open(template_path, 'r', encoding='utf-8') as file:
            html_content = file.read()
        for key, value in data.items():
            html_content = html_content.replace(f'{{{{ {key} }}}}', value)
        filename = f'{data["FrachtbriefID"]}_{data["AusstellungsDatum"]}_{data["EmpfaengerName"]}.html'.replace(" ", "_")
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(html_content)
        webbrowser.open(filename)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
