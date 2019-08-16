# Write a class to hold player information, e.g. what room they are in
# currently.
from colorama import Fore, Back, Style


class Player:

    def __init__(self, name, starting_room):
        self.name = name
        self.current_room = starting_room
        self.items = []

    def move_player(self, inp):
        if inp == "q":
            print(Fore.YELLOW + 'Thanks for playing!')
            return True
        # returning True to quit game

        else:
            possible_room = getattr(self.current_room, (f"{inp}_to"))
            # Check what room exists in the direction inputted

        if possible_room == None:
            print(Fore.RED + "There is nothing in that direction")
            self.input_instructions()
            # self.tester()
            # No room exists, continue loop

        else:
            self.current_room = possible_room
            # Assign the room that exists to the current room
    def tester(self):
        print('test')

    def input_instructions(self):

        self.current_room.where_am_i()
        user_input = input(Fore.LIGHTMAGENTA_EX +
                           "What would you like to do?\nTo move type: n,e,s,w\n"
                           +"to pick up an item type 'get <item>'\n"
                           +"to drop an item type 'drop <item>'"
                           +"Type 'q' to quit\n")
        return self.check_input(user_input)

    def check_input(self, inp):
        text = inp.split(" ")
        move_list = ['n', 'e', 's', 'w', 'q']
        action_list = ['get', 'drop']
        if inp in move_list:
            return self.move_player(inp)
        elif text[0] in action_list and len(text) > 1:
            # print('actions')
            if text[0] == 'get':
                self.get_item(text[1])
            else:
                self.drop_item(text[1])

        else:
            print(Fore.RED + "Incorrect Input. Please Try Again!")

    def get_item(self, item):
        # print(self.current_room.items['rock'])
        # if (getattr(self.current_room.items, (f"{item}"))):
        #     pass
        for obj in self.current_room.items:
            if obj.name == item:
                print(f"Picking up {item}")
                self.current_room.items.remove(obj)
                self.items.append(obj)
                return
        print("That item is not in this room")
        # if item in self.current_room.items:
        #     print(f'getting {item}')
        # else:
        #     print("That item is not here")
        #     print(self.current_room.items)

    def drop_item(self,item):
        for obj in self.items:
            if obj.name == item:
                print(f'dropping {item}')
                self.current_room.items.append(obj)
                self.items.remove(obj)
