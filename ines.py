from os import system

def array_from_map(txt) :
    map = open(txt, 'r')
    indexed_x_map = map.readlines()
    return([list(line) for line in indexed_x_map])

sample_map = array_from_map('map-sample.txt')

map = array_from_map('ines.txt')

def clear():
    _ = system('clear')

def print_map() : 
    print(''.join([''.join(map[k]) for k in range (len(map))]))
    
def not_here(Player) : 
    map[Player.x][Player.y] = sample_map[Player.x][Player.y]

def here(Player)
    map[Player.x][Player.y] = Player.car

