from os import system
from classes import Player
import copy
import random

##Fonctions utiles 

def array_from_map(txt) :  #Construit un array a partir du fichier texte
    map = open(txt, 'r')
    indexed_x_map = map.readlines()
    return([list(line) for line in indexed_x_map])

sample_map = array_from_map('map-sample.txt')

#map = array_from_map('ines.txt')

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
map[pl.x][pl.y]=pl.car
print_map()

#jeu en cours
nextmove=None
while nextmove!='t':
    nextmove=input("next move : ")
    if nextmove in {'q','s','z','d'}:
        refresh(pl,nextmove)
    
def is_object(pl)
    if map[pl.x][pl.y] == 'G' : 
        sum = random.randint(3,30)
        pl.inventory["gold"] += sum
        not_here
    elif map[pl.x][pl.y] == 'j' : 
        pl.inventory["potion"] += 1
    elif map[pl.x][pl.y] == "&" : 
        armor = random.randint(1,5)
        pl.defense += armor
    elif map[pl.x][pl.y] == "!" : 
        sword = random.randint(1,5)
        pl.attack += sword
    elif map[pl.x][pl.y] == "f" : 
        miam = random.randint(3,10)
        pl.hunger += miam
    elif map[pl.x][pl.y] == "w" : 
        pl.thirst += 10
