from os import system
from classes import Player
import copy

##Fonctions utiles 

def array_from_map(txt) :  #Construit un array a partir du fichier texte
    map = open(txt, 'r')
    indexed_x_map = map.readlines()
    return([list(line) for line in indexed_x_map])

sample_map = array_from_map('map-sample.txt')

map = array_from_map('ines.txt')

def clear():
    _ = system('clear')

def print_map() : 
    print(''.join([''.join(map[k]) for k in range (len(map))]))
    
def not_here(pl) : 
    map[pl.x][pl.y] = sample_map[pl.x][pl.y]

def here(pl) :
    map[pl.x][pl.y] = pl.car

def refresh(pl,nextmove) : 

    #on update la map
    not_here(pl)
    pl.move(nextmove)
    here(pl)

    #on refresh la carte avec les updates
    clear()
    print_map()


#initialisation
#name=input('Quel est ton nom ? ')
pl = Player(1,1,'rogue')
map = copy.deepcopy(sample_map)
map[pl.y][pl.x]='@'
print_map()

#jeu en cours
nextmove=None
while nextmove!='t':
    nextmove=input("next move : ")
    if nextmove in {'q','s','z','d'}:
        refresh(pl,nextmove)

class Entity():
    def __init__(self, x, y, name, car):
        self.x = x
        self.y = y
        self.name = name
        self.car = car

    def move(self, nextmove):
        if nextmove == "d":
            if is_empty(self.x+1,self.y):
                self.x += 1
                return self.x, self.y
            else:
                return self.x+1, self.y
        elif nextmove == "q":
            if is_empty(self.x-1,self.y):
                self.x -= 1
                return self.x,self.y
            else:
                return self.x-1, self.y
        elif nextmove == "z":
            if is_empty(self.x,self.y-1):
                self.y -= 1
                return self.x,self.y
            else:
                return self.x, self.y-1
        elif nextmove == "s":
            if is_empty(self.x,self.y-1):
                self.y += 1
                return self.x,self.y
            else:
                return self.x, self.y+1
    
    def __repr__(self):
        return f"{self.name} : ({self.x, self.y})"
    
class Player(Entity) : 
    def __init__(self, x, y, name):
        super().__init__(x,y,name,'@')


    


