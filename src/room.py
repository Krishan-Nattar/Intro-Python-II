# Implement a class to hold room information. This should have name and
# description attributes.
from colorama import Fore, Back, Style

class Room:

    def __init__(self, title, description):
        
        self.title=title
        self.description=description
        self.items = []
    

        self.n_to=None
        self.e_to=None
        self.s_to=None
        self.w_to=None
        
        
    def where_am_i(self):
        print(Fore.GREEN + f"*******************\n{self.title}\n\n\t{self.description}\n*******************")
        self.list_items()
        
    
    def list_items(self):
        if self.items ==[]:
            print(Fore.LIGHTCYAN_EX + f"You don't see any items nearby")
        else:
            if len(self.items) > 1:
                print(Fore.LIGHTCYAN_EX + "You see several items")
                for x in self.items:
                    print(Fore.LIGHTCYAN_EX + f"A {x.name}: it appears to be {x.description}")
            else:
                print(Fore.LIGHTCYAN_EX + "You spot an item...")
                for x in self.items:
                    print(Fore.LIGHTCYAN_EX + f"A {x.name}: it appears to be {x.description}")
                    # print(x.description)

#add methods to check directions?
