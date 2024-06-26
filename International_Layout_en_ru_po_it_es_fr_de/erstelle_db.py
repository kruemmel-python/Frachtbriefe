import sqlite3

def create_database():
    # Verbindung zur SQLite-Datenbank herstellen (oder erstellen, falls nicht vorhanden)
    conn = sqlite3.connect('frachtbriefe.db')
    cursor = conn.cursor()

    # Tabelle für internationale Frachtbriefe erstellen
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS internationalefrachtbriefe (
        FrachtbriefID INTEGER PRIMARY KEY AUTOINCREMENT,
        AusstellungsDatum TEXT,
        Ausstellungsort TEXT,
        AbsenderName TEXT,
        AbsenderAnschrift TEXT,
        AbsenderTelefon TEXT,
        AbsenderEmail TEXT,
        EmpfaengerName TEXT,
        EmpfaengerAnschrift TEXT,
        EmpfaengerTelefon TEXT,
        EmpfaengerEmail TEXT,
        FrachtfuehrerName TEXT,
        FrachtfuehrerAnschrift TEXT,
        FrachtfuehrerTelefon TEXT,
        FrachtfuehrerEmail TEXT,
        Frachtgut TEXT,
        Verpackung TEXT,
        FrachtstueckeAnzahl INTEGER,
        Gesamtgewicht REAL,
        Bemerkungen TEXT,
        Abholort TEXT,
        Abholdatum TEXT,
        Lieferort TEXT,
        Lieferdatum TEXT,
        Transportart TEXT,
        Versicherungsdetails TEXT
    )
    ''')

    # Tabelle für nationale Frachtbriefe erstellen
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS nationalefrachtbriefe (
        FrachtbriefID INTEGER PRIMARY KEY AUTOINCREMENT,
        AusstellungsDatum TEXT,
        Ausstellungsort TEXT,
        AbsenderName TEXT,
        AbsenderAnschrift TEXT,
        AbsenderTelefon TEXT,
        AbsenderEmail TEXT,
        EmpfaengerName TEXT,
        EmpfaengerAnschrift TEXT,
        EmpfaengerTelefon TEXT,
        EmpfaengerEmail TEXT,
        FrachtfuehrerName TEXT,
        FrachtfuehrerAnschrift TEXT,
        FrachtfuehrerTelefon TEXT,
        FrachtfuehrerEmail TEXT,
        Frachtgut TEXT,
        Verpackung TEXT,
        FrachtstueckeAnzahl INTEGER,
        Gesamtgewicht REAL,
        Bemerkungen TEXT,
        Abholort TEXT,
        Abholdatum TEXT,
        Lieferort TEXT,
        Lieferdatum TEXT,
        Transportart TEXT,
        Versicherungsdetails TEXT
    )
    ''')

    # Beispiele für internationale Frachtbriefe einfügen
    cursor.execute('''
    INSERT INTO internationalefrachtbriefe (AusstellungsDatum, Ausstellungsort, AbsenderName, AbsenderAnschrift, AbsenderTelefon, AbsenderEmail, EmpfaengerName, EmpfaengerAnschrift, EmpfaengerTelefon, EmpfaengerEmail, FrachtfuehrerName, FrachtfuehrerAnschrift, FrachtfuehrerTelefon, FrachtfuehrerEmail, Frachtgut, Verpackung, FrachtstueckeAnzahl, Gesamtgewicht, Bemerkungen, Abholort, Abholdatum, Lieferort, Lieferdatum, Transportart, Versicherungsdetails)
    VALUES 
    ('2024-06-25', 'Musterstadt', 'Max Mustermann', 'Musterstraße 1, 12345 Musterstadt', '+49 123 456789', 'max@mustermann.de', 'Anna Beispiel', 'Beispielweg 2, 67890 Beispielstadt', '+49 987 654321', 'anna@beispiel.de', 'Global Transport', 'Globalplatz 4, 34567 Globalstadt', '+49 555 123456', 'contact@globaltransport.com', 'Elektronik', 'Karton', 10, 200.00, 'Keine', 'Lager 1, Lagerstraße 5, 12345 Lagerstadt', '2024-06-26', 'Hauptlager, Lieferstraße 6, 67890 Lieferstadt', '2024-06-27', 'Straßentransport', 'Keine'),
    ('2024-07-01', 'Beispielstadt', 'Fritz Beispiel', 'Beispielallee 3, 45678 Beispielhausen', '+49 321 987654', 'fritz@beispiel.de', 'Karl Muster', 'Musterweg 4, 98765 Musterhausen', '+49 654 321987', 'karl@muster.de', 'Schnell Transport', 'Schnellstraße 6, 54321 Schnellstadt', '+49 123 456789', 'info@schnelltransport.com', 'Maschinenteile', 'Holzkiste', 5, 1500.00, 'Achtung zerbrechlich', 'Lager 2, Industriering 7, 65432 Industrienstadt', '2024-07-02', 'Werk 3, Produktionsstraße 8, 87654 Werkstadt', '2024-07-03', 'Schienentransport', 'Vollversicherung')
    ''')

    # Beispiele für nationale Frachtbriefe einfügen
    cursor.execute('''
    INSERT INTO nationalefrachtbriefe (AusstellungsDatum, Ausstellungsort, AbsenderName, AbsenderAnschrift, AbsenderTelefon, AbsenderEmail, EmpfaengerName, EmpfaengerAnschrift, EmpfaengerTelefon, EmpfaengerEmail, FrachtfuehrerName, FrachtfuehrerAnschrift, FrachtfuehrerTelefon, FrachtfuehrerEmail, Frachtgut, Verpackung, FrachtstueckeAnzahl, Gesamtgewicht, Bemerkungen, Abholort, Abholdatum, Lieferort, Lieferdatum, Transportart, Versicherungsdetails)
    VALUES 
    ('2024-06-25', 'Musterstadt', 'Max Mustermann', 'Musterstraße 1, 12345 Musterstadt', '+49 123 456789', 'max@mustermann.de', 'Anna Beispiel', 'Beispielweg 2, 67890 Beispielstadt', '+49 987 654321', 'anna@beispiel.de', 'Global Transport', 'Globalplatz 4, 34567 Globalstadt', '+49 555 123456', 'contact@globaltransport.com', 'Elektronik', 'Karton', 10, 200.00, 'Keine', 'Lager 1, Lagerstraße 5, 12345 Lagerstadt', '2024-06-26', 'Hauptlager, Lieferstraße 6, 67890 Lieferstadt', '2024-06-27', 'Straßentransport', 'Keine'),
    ('2024-07-01', 'Beispielstadt', 'Fritz Beispiel', 'Beispielallee 3, 45678 Beispielhausen', '+49 321 987654', 'fritz@beispiel.de', 'Karl Muster', 'Musterweg 4, 98765 Musterhausen', '+49 654 321987', 'karl@muster.de', 'Schnell Transport', 'Schnellstraße 6, 54321 Schnellstadt', '+49 123 456789', 'info@schnelltransport.com', 'Maschinenteile', 'Holzkiste', 5, 1500.00, 'Achtung zerbrechlich', 'Lager 2, Industriering 7, 65432 Industrienstadt', '2024-07-02', 'Werk 3, Produktionsstraße 8, 87654 Werkstadt', '2024-07-03', 'Schienentransport', 'Vollversicherung')
    ''')

    # Änderungen speichern und Verbindung schließen
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_database()
