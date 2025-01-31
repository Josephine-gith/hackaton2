from pynput import keyboard
from classes import *
import itertools

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
        amap[i][j] = map[i][j]

def discover_room(x,y,amap,map):
    x0,y0=x,y
    if map[x0-1][y]=='-':
        amap[x0-1][y]=map[x0-1][y]
        while map[x0-1][y]=='-':
            y=y+1
            amap[x0-1][y]=map[x0-1][y]
    if map[x][y0-1]=='|':
        amap[x][y0-1]=map[x][y0-1]
        while map[x][y0-1]=='|':
            x=x+1
            amap[x][y0-1]=map[x][y0-1]
    for i in range(x0,x):
        for j in range(y0,y):
            amap[i][j]=map[i][j]

def update_map(player, move, map):
    with open("josephine.txt", "r") as in_file:
        reader = [list(line) for line in in_file.readlines()]
        map[player.x][player.y] = reader[player.x][player.y]
    player.move(move, map)
    map[player.x][player.y] = "@"


# inplémentation de la map
with open("josephine.txt", "r") as in_file:
    map = in_file.readlines()
    map = [list(line) for line in map]

##déroulé du jeu

# initialisation
# name=input('Quel est ton nom ? ')
P = Player(1, 1, "rogue")
map[P.x][P.y] = "@"
amap = [([" " for j in range(len(map[0]) - 1)] + ["\n"]) for i in range(len(map))]
amap[0][0]='-'
discover_room(P.x, P.y, amap, map)
print_map(amap)


# jeu en cours
def on_press(key):
    if key == keyboard.Key.esc:
        return False
    nextmove = key.char
    if nextmove in ["z", "q", "s", "d"]:
        update_map(P, nextmove, map)
        if map[P.x][P.y]=='+' and map[P.x+1][P.y]:
            discover_room(P.x+1,P.y,amap,map)
        elif map[P.x][P.y]=='+' and map[P.x][P.y+1]:
            discover_room(P.x,P.y+1,amap,map)
        else:
            discover(P.x, P.y, amap, map)
        print_map(amap)


listener = keyboard.Listener(on_press=on_press)
listener.start()
listener.join()
