# config.py



# --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---
# Alle Daten sind hier zentral gespeichert.
# Sie können jederzeit leicht angepasst werden und 
# zu anderen Teilen/Dateien des Programms importiert werden.
# --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---



# Schönes ASCII-Logo des Museums
LOGO = """
███████╗ ██╗   ██╗██╗███████╗██████╗ ██╗   ██╗████████╗███████╗
██╔═══██║██║   ██║██║██╔════╝██╔══██╗╚██╗ ██╔╝╚══██╔══╝██╔════╝
██║   ██║██║   ██║██║███████╗██████╔╝ ╚████╔╝    ██║   █████╗  
██║   ██║██║   ██║██║╚════██║██╔══██╗  ╚██╔╝     ██║   ██╔══╝  
███████╔╝╚██████╔╝██║███████║██████╔╝   ██║      ██║   ███████╗
╚══════╝  ╚═════╝ ╚═╝╚══════╝╚═════╝    ╚═╝      ╚═╝   ╚══════╝
"""

# Alle Preise in Euro
PRICES = {
    "child_half": 2.50,
    "child_full": 5.00,
    "youth_half": 3.50,
    "youth_full": frighten6.00,
    "adult_premium_half": 3.00,
    "adult_premium_full": 6.00,
    "adult_basic_half": 4.00,
    "adult_basic_full": 8.00,
    "adult_none_half": 5.00,
    "adult_none_full": 10.00,
    "champagne": 0.75
}

# Altersgrenzen
CHILD_MAX_AGE = 13  
YOUTH_MAX_AGE = 17   

# Texte in Deutsch und Englisch
TEXTS = {
    "DE": {
        "welcome": "Willkommen im Museum Duisbyte!",
        "choose_lang": "Möchten Sie auf Englisch fortfahren? (j/n): ",
        "age": "Wie alt bist du? ",
        "ticket_type": "Welches Ticket möchtest du?",
        "half": "1 – Halber Tag",
        "full": "2 – Ganzer Tag",
        "membership": "Hast du eine Mitgliedschaft?",
        "premium": "1 – Premium (beste Preise + Sekt möglich)",
        "basic": "2 – Basis-Mitgliedschaft",
        "none": "3 – Keine Mitgliedschaft",
        "champagne": "Möchtest du ein Glas Sekt für 0,75€?",
        "price_is": "Dein Preis:",
        "add_to_cart": "Soll dieser Preis zur Gesamtsumme hinzugefügt werden?",
        "again": "Noch ein Ticket berechnen?",
        "total": "GESAMTSUMME",
        "count": "Anzahl Tickets",
        "bye": "Vielen Dank und viel Spaß im Museum!"
    },
    "EN": {
        "welcome": "Welcome to Museum Duisbyte!",
        "choose_lang": "Continue in English? (y/n): ",
        "age": "How old are you? ",
        "ticket_type": "What kind of ticket do you want?",
        "half": "1 – Half day",
        "full": "2 – Full day",
        "membership": "Do you have a membership?",
        "premium": "1 – Premium (best prices + champagne)",
        "basic": "2 – Basic membership",
        "none": "3 – No membership",
        "champagne": "Would you like champagne for €0.75?",
        "price_is": "Your price:",
        "add_to_cart": "Add this ticket to the total?",
        "again": "Calculate another ticket?",
        "total": "TOTAL AMOUNT",
        "count": "Number of tickets",
        "bye": "Thank you and enjoy the museum!"
    }
}