# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
	def __init__(self, room_name, room_description, items):
		self.room_name = room_name
		self.room_description = room_description
		self.items = items

	def __str__(self):
		return f"{self.room_name}. {self.room_description}. {self.items}"
