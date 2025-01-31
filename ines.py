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
    
def not_here(luigi) : 
    map[luigi.x][luigi.y] = sample_map[pl.x][pl.y]

def here(luigi) :
    map[luigi.x][luigi.y] = pl.car

def refresh(luigi,nextmove) : 

    #on update la map
    not_here(luigi)
    luigi.move(nextmove)
    here(luigi)

    #on refresh la carte avec les updates
    clear()
    print_map()


    


