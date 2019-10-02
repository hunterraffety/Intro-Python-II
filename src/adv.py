from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
"North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
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

# Make a new player object that is currently in the 'outside' room.

p = Player("Louise", room['outside'])

# print(p.room)

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#

directions = input("Which direction would you like to go? N E S or W? ")
#ok, i struggled to get directions to update the way I wanted to even begin to detect the correct if/elif statement because I was trying to use input(type(directions)) and that was throwing me off for the first hour after finally understanding what the directions are. I am going to try and figure out if we can use the methods that are attaching the rooms up there somehow or if we have to write new ones.

while directions != "q":
    print(f"{p.room.name}: {p.room.description}")
    print(directions)
    if directions == "n":
        print("n")
    elif directions == "e":
        print(f"e")
    elif directions == "s":
        print(f"s")
    elif directions == "s":
        print(f"s")
    else:
        quit()
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
