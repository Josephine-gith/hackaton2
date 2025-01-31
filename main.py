from classes import *
from ines import *
from josephine import *
from pynput import keyboard

name = input("Quel est ton nom ?")
P = Player(1, 1, name)

while True:
    """
    objectif général :
    move(player)
    analyser_case (recup les objets)
    if combat :
        combat
    else :
        move(entities)
    update(map)
    display(map)"""
