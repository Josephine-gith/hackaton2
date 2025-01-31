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
    pl.move(nextmove,map)
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
    


    


