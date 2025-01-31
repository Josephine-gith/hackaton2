from classes import Player as pl

#fonctions utiles
def show(map):
    for line in map:
        for c in line:
            print(c)

#inplémentation de la map
with open('josephine.txt', 'r') as in_file:
    file = in_file.readlines()
    for i in range(len(file)):
        file[i] = list(file[i])

##déroulé du jeu

#initialisation
#name=input('Quel est ton nom ? ')
P = pl(1,1,'rogue')
show(file)


    #nextmove = input()
    #while nextmove != 't':
        #P.move(nextmove)



