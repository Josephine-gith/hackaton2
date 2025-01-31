from pynput import keyboard
from classes import *


# fonctions utiles
def print_map(map):
    print("".join(["".join(map[k]) for k in range(len(map))]))


def discover(x, y, amap, map):
    for i, j in {
        (x - 1, y - 1),
        (x - 1, y),
        (x - 1, y + 1),
        (x, y - 1),
        (x, y),
        (x, y + 1),
        (x + 1, y - 1),
        (x + 1, y),
        (x + 1, y + 1),
    }:
        if i < len(map):
            if j < len(map[i]):
                if amap[i][j] != map[i][j]:
                    amap[i][j] = map[i][j]
                    if map[i][j] == ".":
                        discover(i, j, amap, map)


def update_map(player, move, map):
    global E
    with open("map-sample.txt", "r") as in_file:
        reader = [list(line) for line in in_file.readlines()]
        map[player.x][player.y] = reader[player.x][player.y]
    player.move(move, map)
    for entity in entities:
        if type(entity) == Monster:
            entities[entity].move(entities[entity].nextmove(player), map)

    if map[player.x][player.y] == "=":
        map[player.x][player.y] = "@"
        print_map(map)
        print(f"BRAVOOO {P.name} !")
        E = True
    else:
        map[player.x][player.y] = "@"


# inplémentation de la map
with open("map-sample.txt", "r") as in_file:
    map = in_file.readlines()
    map = [list(line) for line in map]

##déroulé du jeu
"""
# initialisation
name = input("Quel est ton nom ? ")
P = Player(1, 1, name)
V = Valroy(7, 5, "prout")
map[P.x][P.y] = "@"
amap = [([" " for j in range(len(map[i]))] + ["\n"]) for i in range(len(map))]
discover(P.x, P.y, amap, map)
print_map(amap)
E = False
"""

# jeu en cours
"""def on_press(key):
    if key == keyboard.Key.esc:
        return False

    nextmove = key.char
    if nextmove in ["z", "q", "s", "d"]:
        update_map(P, nextmove, map)
        discover(P.x, P.y, amap, map)
        if not E:
            print_map(amap)"""


"""listener = keyboard.Listener(on_press=on_press)
listener.start()
listener.join()"""
