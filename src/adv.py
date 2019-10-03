from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
"North of you, the cave mount beckons", "Empty"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", "Sword"),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", "Candle"),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", "Cloak"),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", "Sadness"),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

import textwrap
#
player = Player("Louise", room['outside'], None)


playerInput = ""

while playerInput != "q":
    print(player)
    print("Which direction would you like to go? North, East, South, or West?")
    userInput = input("? ")
    if userInput == "n" or "e" or "s" or "w" or "q":
        if userInput == "n":
            if hasattr(player.current_room, 'n_to'):
                player.current_room = player.current_room.n_to
            else:
                print("Can't go that direction.")
        elif userInput == "e":
            if hasattr(player.current_room, 'e_to'):
                player.current_room = player.current_room.e_to
            else:
                print("Can't go that direction.")
        elif userInput == "s":
            if hasattr(player.current_room, 's_to'):
                player.current_room = player.current_room.s_to
            else:
                print("Can't go that direction.")
        elif userInput == "w":
            if hasattr(player.current_room, 'w_to'):
                player.current_room = player.current_room.w_to
            else:
                print("Can't go that direction.")
        elif userInput == "q":
            break
        else:
            print(f"Invalid key entered.")
    else:
        break