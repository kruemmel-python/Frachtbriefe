import sqlite3
from faker import Faker
from datetime import datetime, timedelta

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

    # Faker-Objekt erstellen
    fake = Faker()

    # Liste der Länder mit echten Städten
    countries_with_cities = {
        'Deutschland': ['Berlin', 'Hamburg', 'München', 'Köln', 'Frankfurt'],
        'England': ['London', 'Manchester', 'Birmingham', 'Leeds', 'Glasgow'],
        'Russland': ['Moskau', 'Sankt Petersburg', 'Nowosibirsk', 'Jekaterinburg', 'Nischni Nowgorod'],
        'Polen': ['Warschau', 'Krakau', 'Łódź', 'Wrocław', 'Poznań'],
        'Italien': ['Rom', 'Mailand', 'Neapel', 'Turin', 'Palermo'],
        'Frankreich': ['Paris', 'Marseille', 'Lyon', 'Toulouse', 'Nizza'],
        'Spanien': ['Madrid', 'Barcelona', 'Valencia', 'Sevilla', 'Zaragoza']
    }

    # Beispieldatensätze generieren und einfügen
    for country, cities in countries_with_cities.items():
        data_entries = []
        for _ in range(1120):
            ausstellungs_datum = fake.date_between(start_date='-1y', end_date='today')
            abholdatum = ausstellungs_datum + timedelta(days=1)
            lieferdatum = abholdatum + timedelta(days=1)
            stadt = fake.random_element(elements=cities)
            data_entries.append((
                ausstellungs_datum.strftime('%Y-%m-%d'),
                f"{country}, {stadt}",
                fake.name(),
                f"{country}, {fake.street_address()}, {stadt}",
                fake.phone_number(),
                fake.email(),
                fake.name(),
                f"{country}, {fake.street_address()}, {stadt}",
                fake.phone_number(),
                fake.email(),
                fake.company(),
                f"{country}, {fake.street_address()}, {stadt}",
                fake.phone_number(),
                fake.email(),
                fake.bs(),
                fake.word(),
                fake.random_int(min=1, max=100),
                fake.random_number(digits=5),
                fake.sentence(),
                f"{country}, {fake.street_address()}, {stadt}",
                abholdatum.strftime('%Y-%m-%d'),
                f"{country}, {fake.street_address()}, {stadt}",
                lieferdatum.strftime('%Y-%m-%d'),
                fake.random_element(elements=('Straßentransport', 'Schienentransport', 'Lufttransport', 'Seetransport')),
                fake.catch_phrase()
            ))

        insert_query = '''
        INSERT INTO {} (AusstellungsDatum, Ausstellungsort, AbsenderName, AbsenderAnschrift, AbsenderTelefon, AbsenderEmail, EmpfaengerName, EmpfaengerAnschrift, EmpfaengerTelefon, EmpfaengerEmail, FrachtfuehrerName, FrachtfuehrerAnschrift, FrachtfuehrerTelefon, FrachtfuehrerEmail, Frachtgut, Verpackung, FrachtstueckeAnzahl, Gesamtgewicht, Bemerkungen, Abholort, Abholdatum, Lieferort, Lieferdatum, Transportart, Versicherungsdetails)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        '''
        cursor.executemany(insert_query.format('internationalefrachtbriefe'), data_entries)
        cursor.executemany(insert_query.format('nationalefrachtbriefe'), data_entries)

    # Änderungen speichern und Verbindung schließen
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_database()
