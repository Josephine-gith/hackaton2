from classes import *
from ines import clear


# fonctions utiles
def print_map(map):
    print("".join(["".join(map[k]) for k in range(len(map))]))


def discover(player, amap, file):
    x = player.x
    y = player.y
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
        amap[i][j] = file[i][j]


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
discover(P, amap, map)
print_map(amap)


# jeu en cours
nextmove = None
while nextmove != "t":
    nextmove = input()
    if nextmove in {"q", "s", "z", "d"}:
        update_map(P, nextmove, map)
        discover(P, amap, map)
        clear()
        print_map(amap)

