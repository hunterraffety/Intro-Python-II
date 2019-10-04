# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, player_name, current_room):
        self.player_name = player_name
        self.current_room = current_room
        self.items = []

    def additem(self, item):
        self.items.append(item)

    def dropitem(self, item):
        self.items.remove(item)

    def __str__(self):
        return f"{self.current_room}"