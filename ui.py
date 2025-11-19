# ui.py



# --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---
# Benutzeroberfläche - Eingabe und Ausgabe.
# --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---



from config import LOGO, TEXTS
from utils import TicketType, MembershipType

class Interface:

	def __init__(self, lang):
		self.lang = lang
		self.texts = TEXTS[lang]

	def show_welcome(self):
		print("\n" + "=" * 60)
		print(LOGO)
		print(selt.texts["welcome"])
		print("=" * 60 + "\n" )

	def ask(self, question):
		return input(question).strip().lower()
	
	def yes_no(self, question):
		while True:
			answer = self.ask(question)
			if answer in ["y", "yes", "j", "ja"]:
				return True
			elif answer in ["n", "no", "nein"]:
				return False
			else:
				print(self.texts["invalid_input"])
			print("Bitte j/n oder y/n eingeben.")

	def get_age(self):
		while True:
			try:
				age = int(self.ask(self.texts["age"]))
				if 0 <= age <= 120:
					return age
				else:
					print(self.texts["invalid_age"])
				print("Bitte ein gülltiges Alter eingeben (0 - 120).")
			except:
				print("Bitte eine Zahl eingeben.")
				
	def get_ticket_type(self):
		print(self.texts["ticket_type"])
		print(self.texts["half"])
		print(self.texts["full"])
		while True:
			choice = self.ask(">>> ")
			if choice == "1":
				return TicketType.HALF_DAY
			elif choice == "2":
				return TicketType.FULL_DAY
			else:
				print(self.texts["invalid_input"])
			print("Bitte 1 oder 2 eingeben.")

	def get_membership(self):
		print(self.texts["membership"])
		print(self.texts["premium"])
		print(self.texts["basic"])
		print(self.texts["none"])
		while True:
			choice = self.ask(">>> ")
			if choice == "1":
				return MembershipType.PREMIUM
			elif choice == "2":
				return MembershipType.BASIC
			elif choice == "3":
				return MembershipType.NONE
			else:
				print(self.texts["invalid_input"])
			print("Bitte 1, 2 oder 3 eingeben.")

	def show_ticket(self, category: str, price: float):
		print("\n" + "-" * 40)
		print(f"{category}")
		print(f"Preis: {price:.2f} €")
    print("—" * 40)

	def show_total(self, total: float, count: int):
		print("\n" + "=" * 60)
		print(f"{self.texts['total']}: {total:.2f} €")
		print(f"{self.texts['count']}: {count}")
		print("=" * 60 + "\n")