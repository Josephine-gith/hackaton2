from classes import *
from ines import *
from josephine import *
from pynput import keyboard

name = input("Quel est ton nom ?")
P = Player(1, 1, name)

while True:
    """
    objectif général :
    info = move(player)
    if info is vide :
        analyser_case (recup les objets)
    elif info is aggro :
        combat
    move(entities)
    update(map)
    display(map)"""
    
