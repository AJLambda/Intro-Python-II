from room import Room
from player import Player
from item import Item

import colorama
colorama.init(autoreset=True)


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


# Create items

torch = Item("torch", "A flaming torch")
key = Item("key", "I can get inside with this")
book = Item("book", "A large spellbook")
eyeglasses = Item("eyeglasses", "I can see better with these")
telescope = Item("telescope", "Useful for stargazing")
rope = Item("rope", "I can hang myself with this")
shovel = Item("shovel", "A small shovel")
compass = Item("compass", "N.E.S.W")
chest = Item("chest", "Chest appears empty :(")
dust = Item("dust", "Just dust.")


# Link items to rooms

room['outside'].items.append(torch)
room['outside'].items.append(key)
room['foyer'].items.append(book)
room['foyer'].items.append(eyeglasses)
room['overlook'].items.append(telescope)
room['overlook'].items.append(rope)
room['narrow'].items.append(shovel)
room['narrow'].items.append(compass)
room['treasure'].items.append(chest)
room['treasure'].items.append(dust)


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


p = Player("Austin", room['outside'])

current_room = p.room
print(current_room)


valid_directions = ["n", "s", "e", "w"]

while True:

    print(colorama.Style.BRIGHT + colorama.Fore.GREEN +
          "type [h] for help")
    cmd = input(">>").lower()
    action = cmd.split(" ")

    if len(action) == 1:
        if cmd in valid_directions:
            p.travel(cmd)
        elif cmd == "i":
            p.print_inventory()
        elif cmd == "h":
            p.print_help()
        elif cmd == "q":
            print("Fare thee well!")
            exit()
        else:
            print(colorama.Fore.RED + "\nI did not recognize that command\n")

    elif len(action) == 2:
        # Picking up items in room
        if action[0] == "get" or action[0] == "take":
            for item in p.room.items:
                if item.name == action[1]:
                    p.get_item(item)
                    print(item.on_take())

        # Dropping items in room
        if action[0] == "drop" or action[0] == "remove":
            for item in p.items:
                if item.name == action[1]:
                    p.drop_item(item)
                    print(item.on_drop())
