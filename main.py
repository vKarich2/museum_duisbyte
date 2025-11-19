# main.py



# --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---
# Startpunkt des Programms.
# --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---



from calculator import get_price
from tickets import get_category

def main():
	
	# Spache wählen
	print("DEUTCH / ENGLISH")
	answer = input("Möchten Sie auf Englisch fortfahren? (j/n): ").strip().lower()
	lang = "EN" if answer in ["j", "ja", "y", "yes"] else "DE"

	while True:

		print("\n--- Neues Ticket berechnen ---")