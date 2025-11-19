# calculator.py



# --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---
# Preisberechnungsfunktionen wurden hier definiert.
# --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---



from config import PRICES, CHILD_MAX_AGE, YOUTH_MAX_AGE
from utils import TicketType, MembershipType

# Diese Funktion berechnet den Preis basierend auf Alter, Tickettyp, Mitgliedschaft und Sektoption.
def get_price(age: int, ticket_type: TicketType, membership=None, champange=False) -> float:

	# Kinder bis 13 Jahre
	if age <= CHILD_MAX_AGE:
		key = "child_full" if ticket_type == TicketType.FULL_DAY else "child_half"

	# Jugendliche von 14 bis 17 Jahre
	elif age <= YOUTH_MAX_AGE:
		key = "youth_full" if ticket_type == TicketType.FULL_DAY else "youth_half"

	# Erwachsene ab 18 Jahre
	else:
		suffix = "full" if ticket_type == TicketType.FULL_DAY else "half"
		if membership == MembershipType.PREMIUM:
			key = f"adult_premium_{suffix}"
		elif membership == MembershipType.BASIC:
			key = f"adult_basic_{suffix}"
		else:
			key = f"adult_none_{suffix}"

	price = PRICES[key]

	# Nur Premium-Mitglieder dürfen Sekt kaufen
	if champange and membership == MembershipType.PREMIUM:
		price += PRICES["champagne"]

	return round(price, 2)