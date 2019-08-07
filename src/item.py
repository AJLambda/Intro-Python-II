# Create a file called item.py and add an Item class in there.
# The item should have name and description attributes.
# Hint: the name should be one word for ease in parsing later.
# This will be the base class for specialized item types to be declared later."""

import colorama
colorama.init(autoreset=True)


class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return (f"name: {self.name} description:{self.description}")

    def on_take(self):
        print(colorama.Fore.BLUE + f"\nyou have picked up {self.name}\n")

    def on_drop(self):
        print(colorama.Fore.BLUE + f"\nyou have dropped {self.name}\n")
