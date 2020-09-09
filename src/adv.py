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

# Make a new player object that is currently in the 'outside' room.
new_player = Player("Frodo", room["outside"])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
directions = {"n": "n_to", "e": "e_to", "s": "s_to", "w": "w_to"}

while True:
    current_room = new_player.current_room
    print(f"\nCurrent Room: {current_room.name}")
    print(f"Room Description: {current_room.description}\n")
    user_input = input("Which direction would you like to go? Select n/e/s/w: ")

    if user_input == "q":
        print("Thanks for playing! Hope to see you soon!\n")
        break
    elif user_input not in directions:
        print("Invalid selection. Please select a valid direction")
    else:
        if hasattr(current_room, directions[user_input]):
            new_player.current_room = current_room.moveRooms(user_input)
        else:
            print("\n***You cannot go that way. Choose a different direction***")