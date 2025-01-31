from classes import Player as pl


#fonctions utiles
def print_map(map): 
    print(''.join([''.join(map[k]) for k in range (len(map))]))

def update_map(player,move,map):
    with open('josephine.txt','r') as in_file:
            reader = [list(line) for line in in_file.readlines()]
            map[player.y][player.x]=reader[player.y][player.x]
    player.move(move)
    file[player.y][player.x]='@'

#inplémentation de la map
with open('josephine.txt', 'r') as in_file:
    file = in_file.readlines()
    file = [list(line) for line in file]

##déroulé du jeu

#initialisation
#name=input('Quel est ton nom ? ')
P = pl(1,1,'rogue')
file[P.y][P.x]='@'
print_map(file)

#jeu en cours
nextmove=None
while nextmove!='t':
    nextmove=input()
    if nextmove in {'q','s','z','d'}:
        update_map(P,nextmove,file)
        print_map(file)
    




