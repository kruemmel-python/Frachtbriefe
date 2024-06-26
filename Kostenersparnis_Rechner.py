import tkinter as tk
from tkinter import ttk

def calculate_total_costs():
    try:
        # Eingabewerte abrufen und validieren
        national_deliveries = int(national_entries.get())
        international_deliveries = int(international_entries.get())
        cost_per_100_national = float(cost_national.get())
        cost_per_100_international = float(cost_international.get())
        needed_sheets = int(needed_sheets_entry.get())
        sheets_per_package = int(sheets_per_package_entry.get())
        package_price = float(package_price_entry.get())
        printing_cost_per_sheet = float(printing_cost_entry.get())
        
        # Preis pro Blatt berechnen
        cost_per_sheet = package_price / sheets_per_package
        
        # Kosten berechnen
        total_cost_national = (national_deliveries / 100) * cost_per_100_national
        total_cost_international = (international_deliveries / 100) * cost_per_100_international
        total_sheet_costs = needed_sheets * (cost_per_sheet + printing_cost_per_sheet)
        
        total_cost = total_cost_national + total_cost_international + total_sheet_costs
        
        # Ergebnislabel aktualisieren
        result_var.set(f"Gesamtkosten National: {total_cost_national:.2f}€\n"
                       f"Gesamtkosten International: {total_cost_international:.2f}€\n"
                       f"Gesamtkosten Blätter: {total_sheet_costs:.2f}€\n"
                       f"Gesamtkosten insgesamt: {total_cost:.2f}€")
    except ValueError:
        result_var.set("Bitte geben Sie gültige Zahlen ein.")

# Hauptfenster erstellen
root = tk.Tk()
root.title("Kostenrechner-Einsparungsrechner")

# Eingabefelder und Labels erstellen und platzieren
tk.Label(root, text="Monatliche nationale Lieferungen:").grid(row=0, column=0, padx=10, pady=5)
national_entries = tk.Entry(root)
national_entries.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Monatliche internationale Lieferungen:").grid(row=1, column=0, padx=10, pady=5)
international_entries = tk.Entry(root)
international_entries.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Kosten pro 100 Vorlagen nationale Lieferungen:").grid(row=2, column=0, padx=10, pady=5)
cost_national = tk.Entry(root)
cost_national.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Kosten pro 100 Vorlagen internationale Lieferungen:").grid(row=3, column=0, padx=10, pady=5)
cost_international = tk.Entry(root)
cost_international.grid(row=3, column=1, padx=10, pady=5)

tk.Label(root, text="Benötigte Blätter:").grid(row=4, column=0, padx=10, pady=5)
needed_sheets_entry = tk.Entry(root)
needed_sheets_entry.grid(row=4, column=1, padx=10, pady=5)

tk.Label(root, text="Blattmenge pro Paket:").grid(row=5, column=0, padx=10, pady=5)
sheets_per_package_entry = tk.Entry(root)
sheets_per_package_entry.grid(row=5, column=1, padx=10, pady=5)

tk.Label(root, text="Preis pro Paket:").grid(row=6, column=0, padx=10, pady=5)
package_price_entry = tk.Entry(root)
package_price_entry.grid(row=6, column=1, padx=10, pady=5)

tk.Label(root, text="Druckkosten pro Blatt:").grid(row=7, column=0, padx=10, pady=5)
printing_cost_entry = tk.Entry(root)
printing_cost_entry.grid(row=7, column=1, padx=10, pady=5)

# Schaltfläche zum Auslösen der Berechnung erstellen
calculate_button = ttk.Button(root, text="Berechnen", command=calculate_total_costs)
calculate_button.grid(row=8, column=0, columnspan=2, pady=10)

# Label zur Anzeige der Ergebnisse erstellen
result_var = tk.StringVar()
result_label = tk.Label(root, textvariable=result_var, justify=tk.LEFT)
result_label.grid(row=9, column=0, columnspan=2, padx=10, pady=10)

# Hauptschleife ausführen
root.mainloop()
