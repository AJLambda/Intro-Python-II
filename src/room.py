# Implement a class to hold room information. This should have name and
# description attributes.

import colorama
colorama.init(autoreset=True)


class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def __str__(self):
        str = f"""
              \n----------------------------------------------------
              \nRoom: {self.name}
              \n   {self.description}
              \n{self._get_exits_string()}
              \n{self._get_item_string()}
              \n----------------------------------------------------
            """
        return str

    def _get_item_string(self):
        if len(self.items) > 0:
            return "Room Items: " + ", ".join([item.name for item in self.items])
        else:
            return "Room Items: None"

    def _get_exits_string(self):
        exits = []
        if self.n_to is not None:
            exits.append("n")
        if self.s_to is not None:
            exits.append("s")
        if self.e_to is not None:
            exits.append("e")
        if self.w_to is not None:
            exits.append("w")
        return "Exits: " + ", ".join(exits)
