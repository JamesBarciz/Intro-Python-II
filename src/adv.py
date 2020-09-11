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

# breakpoint()

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
        "room" - displays available items in current room
        "inv" - display player's inventory
        "drop <item>" - drops named item in current room
        "get <item>" - pick up named item from current room
        TODO
        ''')
    elif command[0] == 'q':
        print(f'Thanks for playing, {usr_name}!')
        break
    elif command[0] == 'inv':
        if len(player1.items) == 0:
            print(f'\nYou have no items...\n')
        elif len(player1.items) == 2:
            print(f'\nInventory: {" & ".join(player1.items)}\n')
        else:
            print(f'\nInventory: {", ".join(player1.items)}\n')
    elif command[0] == 'get':
        player1.pick_up_item(command[1])
        player1.cur_room.items.remove(command[1])
    elif command[0] == 'drop':
        player1.drop_item(command[1])
        player1.cur_room.items.append(command[1])
    elif command[0] == 'room':
        if len(player1.cur_room.items) == 0:
            print('\nThere are no items in this room...\n')
        elif len(player1.cur_room.items) == 2:
            print(f'\nItems in this room: {" & ".join(player1.cur_room.items)}\n')
        else:
            print(f'\nItems in this room: {", ".join(player1.cur_room.items)}\n')
    else:
        try:
            os.system('cls' if os.name == 'nt' else 'clear')
            if command[0] == 'n':
                player1 = Player(usr_name, player1.cur_room.n_to, player1.items)
            elif command[0] == 's':
                player1 = Player(usr_name, player1.cur_room.s_to, player1.items)
            elif command[0] == 'e':
                player1 = Player(usr_name, player1.cur_room.e_to, player1.items)
            elif command[0] == 'w':
                player1 = Player(usr_name, player1.cur_room.w_to, player1.items)
            print(player1.cur_room)
        except:
            print('Ouch!  You hit a wall!')
