from classes import *
from josephine import *
from pynput import keyboard

# inplémentation de la map
with open("map-sample.txt", "r") as in_file:
    map = in_file.readlines()
    map = [list(line) for line in map]
##déroulé du jeu

# initialisation
name = input("Quel est ton nom ? ")
P = Player(1, 1, name)
V = Valroy(3, 3, "valérie")
map[P.x][P.y] = "@"
map[3][3] = "V"
entities[(1, 1)] = P
entities[(3, 3)] = V

amap = [([" " for j in range(len(map[i]))] + ["\n"]) for i in range(len(map))]
discover(P.x, P.y, amap, map)
print_map(amap)
E = False


# jeu en cours
def on_press(key):
    if key == keyboard.Key.esc:
        return False
    nextmove = key.char
    if nextmove in ["z", "q", "s", "d"]:
        update_map(P, nextmove, map)
        discover(P.x, P.y, amap, map)
        if not E:
            print_map(amap)


listener = keyboard.Listener(on_press=on_press)
listener.start()
listener.join()
