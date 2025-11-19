# ui.py


# --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---
# Benutzeroberfläche - Eingabe und Ausgabe.
# --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---


from config import LOGO, TEXTS
from utils import TicketType, MembershipType


class Interface:
    def __init__(self, lang):
        self.lang = lang
        self.t = TEXTS[lang]  # Kurzform für Texte – einfacher zu schreiben

    def show_welcome(self):
        print("\n" + "=" * 60)
        print(LOGO)
        print(self.t["welcome"])
        print("=" * 60 + "\n")

    def ask(self, question):
        return input(question).strip().lower()

    def yes_no(self, question):
        """Fragt nach Ja/Nein – akzeptiert j/n, ja/nein, y/n"""
        while True:
            answer = self.ask(question)
            if answer in ["y", "yes", "j", "ja"]:
                return True
            elif answer in ["n", "no", "nein"]:
                return False
            else:
                print("Bitte nur 'j' oder 'n' eingeben.")

    def get_age(self):
        while True:
            try:
                age_input = self.ask(self.t["age"])
                age = int(age_input)
                if 0 <= age <= 120:
                    return age
                else:
                    print("Alter muss zwischen 0 und 120 Jahren liegen.")
            except ValueError:
                print("Bitte eine gültige Zahl eingeben.")

    def get_ticket_type(self):
        print(self.t["ticket_type"])
        print(self.t["half"])
        print(self.t["full"])
        while True:
            choice = self.ask("Deine Wahl (1 oder 2): ")
            if choice == "1":
                return TicketType.HALF_DAY
            elif choice == "2":
                return TicketType.FULL_DAY
            else:
                print("Ungültige Eingabe. Bitte 1 oder 2 wählen.")

    def get_membership(self):
        print(self.t["membership"])
        print(self.t["premium"])
        print(self.t["basic"])
        print(self.t["none"])
        while True:
            choice = self.ask("Deine Wahl (1, 2 oder 3): ")
            if choice == "1":
                return MembershipType.PREMIUM
            elif choice == "2":
                return MembershipType.BASIC
            elif choice == "3":
                return MembershipType.NONE
            else:
                print("Ungültige Eingabe. Bitte 1, 2 oder 3 wählen.")

    def show_ticket(self, category, price):
        print("\n" + "—" * 50)
        print(f"KATEGORIE: {category}")
        print(f"PREIS:     {price:.2f} €")
        print("—" * 50 + "\n")

    def show_total(self, total, count):
        print("\n" + "=" * 60)
        print(f"{self.t['total']}: {total:.2f} €")
        print(f"{self.t['count']}: {count}")
        print("=" * 60 + "\n")
