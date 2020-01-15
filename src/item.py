from colorama import Fore, Back, Style

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    def on_take(self):
        print(Fore.YELLOW + f"You have picked up {self.name}")
        # pass
    def on_drop(self):
        print(Fore.YELLOW + f"You have dropped {self.name}")
        # pass