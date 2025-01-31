# classes
class Player:
    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        self.name = name
        self.car = '@'

    def move(self, nextmove):
        if nextmove == "d":
            self.x += 1
        elif nextmove == "q":
            self.x -= 1
        elif nextmove == "z":
            self.y -= 1
        elif nextmove == "s":
            self.y += 1
    
    def __repr__(self):
        return f"{self.name} : ({self.x, self.y})"


def discover(player, amap, file):
    x=player.x
    y=player.y
    for i,j in {(x-1,y-1),(x-1,y),(x-1,y+1),(x,y-1),(x,y),(x,y+1),(x+1,y-1),(x+1,y),(x+1,y+1)}:
        amap[j][i]=file[j][i]

def update_map(player,move,map):
    with open('josephine.txt','r') as in_file:
            reader = [list(line) for line in in_file.readlines()]
            map[player.y][player.x]=reader[player.y][player.x]
    player.move(move)
    file[player.y][player.x]='@'
# fonctions utiles
def print_map(map):
    print("".join(["".join(map[k]) for k in range(len(map))]))


def update_map(player, move, map):
    with open("josephine.txt", "r") as in_file:
        reader = [list(line) for line in in_file.readlines()]
        map[player.y][player.x] = reader[player.y][player.x]
    player.move(move, map)
    file[player.y][player.x] = "@"


# inplémentation de la map
with open("josephine.txt", "r") as in_file:
    file = in_file.readlines()
    file = [list(line) for line in file]

##déroulé du jeu

#initialisation
#name=input('Quel est ton nom ? ')
P = Player(1,1,'rogue')
file[P.y][P.x]='@'
amap = [([' ' for j in range(len(file[0])-1)]+['\n']) for i in range(len(file))]
discover(P, amap, file)
print_map(amap)


#jeu en cours
nextmove=None
while nextmove!='t':
    nextmove=input()
    if nextmove in {'q','s','z','d'}:
        update_map(P,nextmove,file)
        discover(P,amap,file)
        print_map(amap)
