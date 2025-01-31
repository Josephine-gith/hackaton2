from ines import is_object, not_here
import random

class Entity:
    def __init__(self, x, y, name, car, life):
        self.x = x
        self.y = y
        self.name = name
        self.car = car
        self.life = life
    
    def move(self, nextmove, map):
        if nextmove == "s" or nextmove == "down":
            if is_empty(self.x + 1, self.y, map):
                self.x += 1
                is_object(self)
                return self.x, self.y
            else:
                return self.x + 1, self.y
        elif nextmove == "z" or nextmove == "up":
            if is_empty(self.x - 1, self.y, map):
                self.x -= 1
                is_object(self)
                return self.x, self.y
            else:
                return self.x - 1, self.y
        elif nextmove == "q" or nextmove == "left":
            if is_empty(self.x, self.y - 1, map):
                self.y -= 1
                is_object(self)
                return self.x, self.y
            else:
                return self.x, self.y - 1
        elif nextmove == "d" or nextmove == "right":
            if is_empty(self.x, self.y + 1, map):
                self.y += 1
                is_object(self)
                return self.x, self.y
            else:
                self.y += 1
                is_entity(self)
                self.y -= 1
                return self.x, self.y + 1

    def __repr__(self):
        return f"{self.name} : ({self.x, self.y})"


class Player(Entity):
    def __init__(self, x, y, name):
        super().__init__(x, y, name, "@", 16)
        self.level = 1
        self.hits = 15
        self.defense = 5
        self.attack = 0 
        self.hunger = 100 # chaque 100 pas font perdre 1 point de faim
        self.thirst = 100 # chaque 20 pas font perdre un point de soif
        self.inventory = {"gold" : 0 ,
                          "potions" : 0 
                          } # inventory est un dictionnaire key = objet, value = combien on en a

class Monster(Entity):
    def __init__(self, x, y, name, char,life):
        super().__init__(x, y, name, char,)

class Valroy(Monster) : 
    def __init__(self, x, y, name):
        super().__init__(x, y, name, 'V',300)

class Lionel(Monster) : 
    def __init__(self, x, y, name):
        super().__init__(x, y, name, 'L',300)

class Fontane(Monster) : 
    def __init__(self, x, y, name):
        super().__init__(x, y, name, 'F',500)

def is_object(pl) : 
    
    if type(pl)!=Player : 
        return
    else : 
        if map[pl.x][pl.y] == 'G' : 
            sum = random.randint(3,30)
            pl.inventory["gold"] += sum
            not_here(pl) # ici enleve l'objet du sol
        elif map[pl.x][pl.y] == 'j' : 
            pl.inventory["potion"] += 1
            not_here(pl)
        elif map[pl.x][pl.y] == "&" : 
            armor = random.randint(1,5)
            pl.defense += armor
            not_here(pl)
        elif map[pl.x][pl.y] == "!" : 
            sword = random.randint(1,5)
            pl.attack += sword
            not_here(pl)
        elif map[pl.x][pl.y] == "f" : 
            miam = random.randint(3,10)
            pl.hunger += miam
            not_here(pl)
        elif map[pl.x][pl.y] == "w" : 
            pl.thirst += 10
            not_here(pl)

monsters = {} # dictionnaire ; key = coordinates ; value = instance de monstre (peut s'appeler pedro par exemple)

def is_entity(pl) :
    if type(pl)!=Player : 
        return
    else : 
        if (pl.x,pl.y) in monsters : 
            damage = random.randint(20)
            monsters[(pl.x,pl.y)].life -=1
            if 
            

def is_empty(x, y, map):
    if map[x][y] in ["-", "|", " "]:
        print(map[x][y])
        return False
    return True
