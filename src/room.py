# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
		def __init__(self, name, description):
				self.name = name
				self.description = description
				
		def e_to(self, room):
				pass
		
		def __str__(self):
				s = f"{self.name}. {self.description}"
				return s