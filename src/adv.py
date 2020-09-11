from room import Room
from player import Player

import os

# Declare all the rooms


room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",
                     ["item1", "item2", "item3"]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", 
                     ["item4"]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",
                     ["item5"]),

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

usr_name = input('Please enter character name: ')

player1 = Player(usr_name, room['outside'], ['basic_item0'])
cur_room = player1.cur_room
print(player1.cur_room)

while True:
    command = input('Enter a direction or type "help" for a list of commands: ').split()
    if command[0] == 'help':
        print('''
        Directions:
        "n" - north
        "s" - south
        "e" - east
        "w" - west

        Commands:
        "q" - quit game
        "i" - display player's inventory
        "drop <item>" - drops named item in current room
        "get <item>" - pick up named item from current room
        TODO
        ''')
    elif command[0] == 'q':
        print(f'Thanks for playing, {usr_name}!')
        break
    elif command[0] == 'i':
        print(f'Inventory: {", ".join(player1.items)}')
    # elif command[0] == 'get':
    #     add item (command[1]) to inventory
    #     remove item(command[1]) from cur_room item list
    # elif command[0] == 'drop':
    #     drop item from inventory
    #     add item to cur_room item list
    else:
        try:
            os.system('cls' if os.name == 'nt' else 'clear')
            if command[0] == 'n':
                player1 = Player(usr_name, player1.cur_room.n_to)
            elif command[0] == 's':
                player1 = Player(usr_name, player1.cur_room.s_to)
            elif command[0] == 'e':
                player1 = Player(usr_name, player1.cur_room.e_to)
            elif command[0] == 'w':
                player1 = Player(usr_name, player1.cur_room.w_to)
            print(player1.cur_room)
        except:
            print('Ouch!  You hit a wall!')