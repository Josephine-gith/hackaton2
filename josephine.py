from classes import Player as pl

name=input('Quel est ton nom ?')
P = pl(1,1,name)

with open('map-sample.txt') as reader:
    for line in reader:
        print(line, end="")

nextmove = input("\n")
P.move(nextmove)


