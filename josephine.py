from classes import Player as pl


#fonctions utiles
def print_map(map) : 
    print(''.join([''.join(map[k]) for k in range (len(map))]))

#inplémentation de la map
with open('josephine.txt', 'r') as in_file:
    file = in_file.readlines()
    file = [list(line) for line in file]

##déroulé du jeu

#initialisation
#name=input('Quel est ton nom ? ')
P = pl(1,1,'rogue')
file[P.x][P.y]='@'
print_map(file)

#jeu en cours
nextmove=None
while nextmove!='t':
    nextmove=input()
    if nextmove in {'q','s','z','d'}:
        P.move(nextmove)

    




