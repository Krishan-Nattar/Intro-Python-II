from room import Room
from player import Player
from item import Item
from colorama import Fore, Back, Style

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

 'river': Room("Riverfront", """You've come up to the edge of a river. It's too deep to cross. The sound of drums wafts through the air."""),

 'jungleentrance': Room("Jungle Entrance", """The trees are thick and dark between their trunks. Lush foliage surrounds you."""),

 'home': Room("Home", """Your childhood home. Your baby pictures adorn the walls."""),
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
room['treasure'].n_to = room['river']
room['river'].s_to = room['treasure']
room['river'].e_to = room['jungleentrance']
room['jungleentrance'].w_to = room['river']
room['jungleentrance'].n_to = room['home']
room['home'].s_to = room['jungleentrance']

rock = Item("rock", "a small grey stone. Nothing special")
coin = Item("coin", "a silver dollar. The symbols on it are faded, but you can make out the image of a ship.")
key = Item("key", "a rusty key. I wonder what this opens?")
parchment = Item("parchment", "a piece of paper. The writing on it is in a language you've never seen.")
banana = Item("banana", "a small yellow fruit. A great source of potassium.")

room['foyer'].items.append(rock)
room['overlook'].items.append(key)
room['overlook'].items.append(banana)
room['narrow'].items.append(parchment)
room['treasure'].items.append(coin)

player = Player("Krishan", room["outside"])

# Main Controller

while True:

    quit = player.input_instructions()

    if quit == True:
        break
