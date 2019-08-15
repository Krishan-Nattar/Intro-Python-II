# Write a class to hold player information, e.g. what room they are in
# currently.
from colorama import Fore, Back, Style 

class Player:
    # user_input = ""
    

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
            # print(possible_room)
        if possible_room == None:
            print(Fore.RED + "There is nothing in that direction")
        else:
            self.current_room = possible_room

    def input_instructions(self):
    
        print(Fore.GREEN + self.current_room.where_am_i())
        user_input = input(Fore.BLUE + 
        "Where would you like to go? n, s, e, w? type q to quit.")
        return self.check_input(user_input)

    def check_input(self, inp):
        input_list = ['n', 'e', 's', 'w', 'q']
        if inp in input_list:
            return self.move_player(inp)
        else:
            print(Fore.RED + "Incorrect Input. Please Try Again!")