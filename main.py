# main.py


# --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---
# Startpunkt des Programms.
# --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---


# Imports
from ui import Interface
from calculator import get_price
from tickets import get_category

# Hauptfunktion des Programms.
# Führt die Benutzerinteraktion und Preisberechnung durch.
def main():
    # --- Sprachauswahl ---
    print("DEUTSCH / ENGLISH")
    answer = input("Möchten Sie auf Englisch fortfahren? (j/n): ").strip().lower()
    lang = "EN" if answer in ["j", "ja", "y", "yes"] else "DE"

    # Interface starten
    ui = Interface(lang)
    ui.show_welcome()

    total_price = 0.0
    quantity_of_tickets = 0

    # --- Hauptschleife für Ticketberechnung ---
    while True:
        print("\n" + "═" * 50)
        print("NEUES TICKET")
        print("═" * 50)

        age = ui.get_age()
        ticket_type = ui.get_ticket_type()

        membership = None
        champagne = False

        # Nur Erwachsene haben Mitgliedschaft und können Sekt bestellen
        if age > 17:
            membership = ui.get_membership()
            if membership == 1:  # Premium = 1
                champagne = ui.yes_no(ui.t["champagne"])

        # Preis berechnen und Kategorie ermitteln
        price = get_price(age, ticket_type, membership, champagne)
        category = get_category(age, ticket_type, membership, champagne, lang)

        # Ticket anzeigen
        ui.show_ticket(category, price)

        # Zur Gesamtsumme hinzufügen?
        if ui.yes_no(ui.t["add_to_cart"]):
            total_price += price
            quantity_of_tickets += 1

        # Noch ein Ticket?
        if not ui.yes_no(ui.t["again"]):
            break

    # --- Abschluss ---
    if quantity_of_tickets > 0:
        ui.show_total(total_price, quantity_of_tickets)

    print("\n" + ui.t["bye"])


# Programm starten
if __name__ == "__main__":
    main()
