# utils.py



# --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---
# Hilfsklassen und -funktionen können hier definiert werden.
# --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---



# Imports 
from enum import IntEnum

# Tickettypen
class TicketType(IntEnum):
		HALF_DAY = 1 		# Halber Tag
		FULL_DAY = 2 		# Ganzer Tag

# Mitgliedschaftstypen (ab 18 Jahre)
class MembershipType(IntEnum):
		PREMIUM = 1			# Premium (Sekt möglich)
		BASIC = 2				# Basis-Mitgliedschaft
		NONE = 3				# Keine Mitgliedschaft