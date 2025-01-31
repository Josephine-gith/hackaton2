class Entity:
    def __init__(self, x, y, name, car):
        self.x = x
        self.y = y
        self.name = name
        self.car = car

    def move(self, nextmove, map):
        if nextmove == "d":
            if is_empty(self.x + 1, self.y, map):
                self.x += 1
                return self.x, self.y
            else:
                return self.x + 1, self.y
        elif nextmove == "q":
            if is_empty(self.x - 1, self.y, map):
                self.x -= 1
                return self.x, self.y
            else:
                return self.x - 1, self.y
        elif nextmove == "z":
            if is_empty(self.x, self.y - 1, map):
                self.y -= 1
                return self.x, self.y
            else:
                return self.x, self.y - 1
        elif nextmove == "s":
            if is_empty(self.x, self.y + 1, map):
                self.y += 1
                return self.x, self.y
            else:
                return self.x, self.y + 1

    def __repr__(self):
        return f"{self.name} : ({self.x, self.y})"
    
class Player(Entity) : 
    def __init__(self, x, y, name):
        super().__init__(x,y,name,'@')


class Player(Entity):
    def __init__(self, x, y, name):
        super().__init__(x, y, name, "@")


def is_empty(x, y, map):
    if map[y][x] in ["-", "|", " "]:
        return False
    return True
