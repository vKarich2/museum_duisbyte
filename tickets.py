# tickets.py



# --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---
# Schöne Ticket-Beschriftungen wurden hier definiert.
# --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---



# Imports 
from config import CHILD_MAX_AGE, YOUTH_MAX_AGE, CATEGORIES
from utils import TicketType, MembershipType

# Gibt den lesbaren Namen der Ticket-Kategorie zurück
def get_category(age: int, ticket_type: TicketType, membership, champagne: bool, lang: str) -> str:
	
	if age <= CHILD_MAX_AGE:
		key = "child_full" if ticket_type == TicketType.FULL_DAY else "child_half"
	elif age <= YOUTH_MAX_AGE:
		key = "youth_full" if ticket_type == TicketType.FULL_DAY else "youth_half"
	else:
		suffix = "full" if ticket_type == TicketType.FULL_DAY else "half"
		if membership == MembershipType.PREMIUM:
			key = f"adult_premium_{suffix}"
		elif membership == MembershipType.BASIC:
			key = f"adult_basic_{suffix}"
		else:
			key = f"adult_none_{suffix}"

		text = CATEGORIES[lang][key]

		if champagne and membership == MembershipType.PREMIUM:
			text += CATEGORIES[lang]["champagne"]

		return text

