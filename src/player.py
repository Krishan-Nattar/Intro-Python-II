# Write a class to hold player information, e.g. what room they are in
# currently.
from colorama import Fore, Back, Style 

class Player:
    def __init__(self, name, starting_room):
        self.name=name
        self.current_room=starting_room

    def move_player(self, inp):
        if inp == "q":
            print(Fore.YELLOW + 'Thanks for playing!')
            return True 
        # returning True to quit value
        
        else:
            possible_room = getattr(self.current_room, (f"{inp}_to"))
            print(possible_room)
        if possible_room == None:
            print(Fore.RED + "There is nothing in that direction")
        else:
            self.current_room = possible_room