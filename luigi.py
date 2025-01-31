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
amap = [([" " for j in range(len(map[i]))] + ["\n"]) for i in range(len(map))]
discover(P.x, P.y, amap, map)
print_map(amap)


# jeu en cours
def on_press(key):
    if key == keyboard.Key.esc:
        return False
    nextmove = key.char
    if nextmove in ["z", "q", "s", "d"]:
        update_map(P, nextmove, map)
        discover(P.x, P.y, amap, map)
        print_map(amap)


"""listener = keyboard.Listener(on_press=on_press)
listener.start()
listener.join()"""


class Monster(Entity):
    def __init__(self, x, y, name, char):
        super().__init__(x, y, name, char)

    def nextmove(self, player):
        delta_x = abs(self.x - player.x)
        delta_y = abs(self.y - player.y)
        if delta_x > delta_y:
            if self.x - player.x > 0:
                return "up"
            return "down"
        else:
            if self.y - player.y > 0:
                return "right"
            return "left"
