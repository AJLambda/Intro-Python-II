# Write a class to hold player information, e.g. what room they are in
# currently.

import colorama
colorama.init(autoreset=True)


class Player:
    def __init__(self, name, room):
        self.name = name
        self.room = room
        self.items = []

    def travel(self, direction):
        # Check if there's a valid room in the direction
        if getattr(self.room, f"{direction}_to") is not None:
            # If so, update room to new room and print description
            self.room = getattr(self.room, f"{direction}_to")
            print(self.room)
        else:
            # Else print an error message
            print(colorama.Fore.RED + "\n" +
                  "Sorry! There's no room here.", "\n")

    def _get_item_string(self):
        if len(self.items) > 0:
            return ", ".join([item.name for item in self.items])
        else:
            return ""

    def print_inventory(self):
        if len(self.items) > 0:
            print(colorama.Fore.YELLOW + "\nYou are carrying: " +
                  ", ".join([item.name for item in self.items]) + "\n")
        else:
            print(colorama.Fore.YELLOW + "\nYou are carrying: Nothing\n")

    def get_item(self, item):
        # if item in self.room.items:
        self.items.append(item)
        self.room.items.remove(item)
        item.on_take()

        # else:
        #print(colorama.Fore.RED + "\nItem not found in room\n")

    def drop_item(self, item):
        # item in self.room.items:
        self.items.remove(item)
        self.room.items.append(item)
        item.on_drop()

        # else:
        #print(colorama.Fore.RED + "\nItem not found in room\n")
