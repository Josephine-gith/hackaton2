class Player:
    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        self.name = name
        self.car = '@'

    def move(self, nextmove):
        if nextmove == "d":
            self.x += 1
        elif nextmove == "q":
            self.x -= 1
        elif nextmove == "z":
            self.y -= 1
        elif nextmove == "s":
            self.y += 1
    
    def __repr__(self):
        return f"{self.name} : ({self.x, self.y})"