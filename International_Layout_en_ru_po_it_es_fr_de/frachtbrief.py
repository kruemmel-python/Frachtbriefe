import sys
import sqlite3
import webbrowser
from PyQt5.QtWidgets import (QApplication, QMainWindow, QAction, QMenu, QWidget,
                             QVBoxLayout, QFormLayout, QLineEdit, QPushButton,
                             QTableWidget, QTableWidgetItem, QHeaderView, QHBoxLayout, QSplitter, QScrollArea)
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QFont


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Frachtbriefe / Waybills')
        self.setGeometry(100, 100, 1200, 800)
        self.setStyleSheet("background-color: #2e2e2e; color: #ffffff;")

        menubar = self.menuBar()
        menubar.setStyleSheet("background-color: #1e1e1e; color: #ffffff;")
        self.createMenu(menubar, 'Internationaler Frachtbrief / International Waybill', self.erfassenInternational, self.abrufenInternational)
        self.createMenu(menubar, 'Nationaler Frachtbrief / National Waybill', self.erfassenNational, self.abrufenNational)

    def createMenu(self, menubar, title, erfassen, abrufen):
        menu = menubar.addMenu(title)
        menu.setStyleSheet("background-color: #1e1e1e; color: #ffffff;")
        erfassenAction = QAction('Daten erfassen / Enter Data', self)
        erfassenAction.triggered.connect(erfassen)
        menu.addAction(erfassenAction)
        abrufenAction = QAction('Daten abrufen / Retrieve Data', self)
        abrufenAction.triggered.connect(abrufen)
        menu.addAction(abrufenAction)

    def erfassenInternational(self): 
        self.setCentralWidget(ErfassenForm('internationalefrachtbriefe'))

    def abrufenInternational(self): 
        self.setCentralWidget(AbrufenForm('internationalefrachtbriefe'))

    def erfassenNational(self): 
        self.setCentralWidget(ErfassenForm('nationalefrachtbriefe'))

    def abrufenNational(self): 
        self.setCentralWidget(AbrufenForm('nationalefrachtbriefe'))


class ErfassenForm(QWidget):
    def __init__(self, table):
        super().__init__()
        self.table = table
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        formLayout = QFormLayout()
        self.fields = {
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
        font.setPointSize(12)
        
        for field, widget in self.fields.items():
            widget.setFont(font)
            widget.setStyleSheet("padding: 10px; border: 1px solid #444; border-radius: 5px; color: #ffffff; background-color: #333;")
            formLayout.addRow(field, widget)

        self.submitButton = QPushButton('Speichern / Save')
        self.submitButton.setFont(font)
        self.submitButton.setStyleSheet("background-color: #007BFF; color: white; padding: 10px; border-radius: 5px;")
        self.submitButton.clicked.connect(self.submitData)

        layout.addLayout(formLayout)
        layout.addWidget(self.submitButton)

        scrollArea = QScrollArea()
        scrollArea.setWidgetResizable(True)
        container = QWidget()
        container.setLayout(layout)
        scrollArea.setWidget(container)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(scrollArea)
        self.setLayout(mainLayout)

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
        self.searchFields = {
            'FrachtbriefID / Waybill ID': QLineEdit(),
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
        font.setPointSize(12)

        for field, widget in self.searchFields.items():
            widget.setFont(font)
            widget.setStyleSheet("padding: 10px; border: 1px solid #444; border-radius: 5px; color: #ffffff; background-color: #333;")
            searchLayout.addRow(field, widget)

        self.searchButton = QPushButton('Suchen / Search')
        self.searchButton.setFont(font)
        self.searchButton.setStyleSheet("background-color: #007BFF; color: white; padding: 10px; border-radius: 5px;")
        self.searchButton.clicked.connect(self.searchData)

        searchLayout.addWidget(self.searchButton)

        scrollArea = QScrollArea()
        scrollArea.setWidgetResizable(True)
        searchContainer = QWidget()
        searchContainer.setLayout(searchLayout)
        scrollArea.setWidget(searchContainer)

        splitter.addWidget(scrollArea)

        self.tableWidget = QTableWidget()
        self.tableWidget.setStyleSheet("background-color: #444; color: #ffffff; gridline-color: #ccc;")
        self.tableWidget.setColumnCount(len(self.searchFields))
        self.tableWidget.setHorizontalHeaderLabels(self.searchFields.keys())
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)
        self.tableWidget.horizontalHeader().setContextMenuPolicy(Qt.CustomContextMenu)
        self.tableWidget.horizontalHeader().customContextMenuRequested.connect(self.showHeaderContextMenu)
        self.tableWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tableWidget.customContextMenuRequested.connect(self.showRowContextMenu)

        # Make header green
        self.tableWidget.setStyleSheet(
            """
            QHeaderView::section {background-color: #00ff00; color: black;}
            QTableWidget {background-color: #444; color: #ffffff; gridline-color: #ccc;}
            """
        )

        splitter.addWidget(self.tableWidget)
        layout.addWidget(splitter)
        self.setLayout(layout)

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

    def showHeaderContextMenu(self, pos: QPoint):
        header = self.tableWidget.horizontalHeader()
        logicalIndex = header.logicalIndexAt(pos)
        menu = QMenu()
        resizeAction = QAction('Optimale Breite / Optimal Width', self)
        resizeAction.triggered.connect(lambda: self.tableWidget.resizeColumnToContents(logicalIndex))
        menu.addAction(resizeAction)
        menu.exec(header.mapToGlobal(pos))

    def showRowContextMenu(self, pos: QPoint):
        row = self.tableWidget.rowAt(pos.y())
        if row < 0: return
        menu = QMenu()
        
        createSubMenu = QMenu('Erstelle Frachtbrief / Create Waybill', self)
        self.addLanguageActions(createSubMenu, row)
        
        menu.addMenu(createSubMenu)
        menu.exec(self.tableWidget.viewport().mapToGlobal(pos))
    
    def addLanguageActions(self, menu, row):
        languages = {
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
            action.triggered.connect(lambda _, c=code: self.createFrachtbrief(row, c))
            menu.addAction(action)

    def createFrachtbrief(self, row, language_code):
        data = {self.tableWidget.horizontalHeaderItem(col).text(): self.tableWidget.item(row, col).text() for col in range(self.tableWidget.columnCount())}
        
        if self.table == 'internationalefrachtbriefe':
            template_path = f'if_{language_code}_frachtbrief.html'
        else:
            template_path = f'nf_{language_code}_frachtbrief.html'
        
        with open(template_path, 'r', encoding='utf-8') as file:
            html_content = file.read()
        
        for key, value in data.items():
            html_content = html_content.replace(f'{{{{ {key.split(" / ")[0]} }}}}', value)
        
        filename = f'{data["FrachtbriefID / Waybill ID"]}_{data["AusstellungsDatum / Date of Issue"]}_{data["EmpfaengerName / Recipient Name"]}.html'.replace(" ", "_")
        
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(html_content)
        
        webbrowser.open(filename)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())
