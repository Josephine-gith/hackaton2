


Voici une version en markdown pour un TP dirigé sur l'exploration de graphes avec des algorithmes de parcours en profondeur (DFS) et en largeur (BFS). Ce TP inclut des explications, des exercices guidés et des exemples pour les étudiants.

---

# TP Dirigé : Exploration de Graphes - Parcours en Profondeur (DFS) et en Largeur (BFS)

## Objectifs

1. Comprendre les algorithmes de parcours DFS et BFS.
2. Implémenter des structures de stockage (FIFO, FILO) pour réaliser ces parcours.
3. Manipuler un graphe sous forme d'objets Python.
4. Utiliser des générateurs pour explorer les graphes.

Il y a du code à compléter partout ou il y a le mot clef `pass`

---

## Partie 1 : Introduction aux Parcours DFS et BFS

### Concepts de Base

Lorsqu'on explore un graphe depuis un sommet donné, deux stratégies principales sont utilisées :

- **DFS (Depth-First Search)** : Explore les chemins aussi loin que possible avant de revenir en arrière.
- **BFS (Breadth-First Search)** : Explore tous les voisins directs avant de passer au niveau suivant.

Prenons le graphe suivant pour illustrer ces deux stratégies :

```
    v
   / \
 v1   v2
 / \   / \
v11 v12 v21 v22
```

#### Ordre de Parcours

- DFS à partir de `v` : `v → v1 → v11 → v111 → v112 → v12 → v121 → v122 → v2 → v21 → v211 → v212 → v22 → v221 → v222`.
- BFS à partir de `v` : `v → v1 → v2 → v11 → v12 → v21 → v22 → v111 → v112 → v121 → v122 → v211 → v212 → v221 → v222`.

---

## Partie 2 : Mise en Place

### Étape 1 : Implémentation des Structures de Stockage

Nous avons besoin de deux structures :

- Une file **FIFO** (First-In-First-Out) pour BFS.
- Une pile **FILO** (First-In-Last-Out) pour DFS.

#### Implémentez les classes suivantes :

```python
from collections import deque

class Fifo:
    def __init__(self):
        self.file = deque()
    def store(self, item):
        self.file.append(item)
    def retrieve(self):
        return self.file.popleft()
    def __len__(self):
        return len(self.file)
    def __repr__(self):
        return f"{self.file}"

class Filo:
    def __init__(self):
        self.pile = deque()
    def store(self, item):
        self.pile.append(item)
    def retrieve(self):
        return self.pile.pop()
    def __len__(self):
        return len(self.pile)
    def __repr__(self):
        return f"{self.pile}"
```

#### Vérifiez leur bon fonctionnement :

```python
# Testez Fifo
fifo = Fifo()
for i in range(1, 4):
    fifo.store(i)
while fifo:
    print(f"retrieve → {fifo.retrieve()}")

# Testez Filo
filo = Filo()
for i in range(1, 4):
    filo.store(i)
while filo:
    print(f"retrieve → {filo.retrieve()}")

```

Autre méthode en créant une classe pile dont héritent Fifo et Filo, et qui contient les méthodes communes aux deux piles.

```python
class Pile:
    def __init__(self):
        self.pile=deque()
    def store(self, item):
        self.pile.append(item)
    def __len__(self):
        return len(self.pile)
    def __repr__(self):
        return f"{self.pile}"

class Fifo(Pile):
    def retrieve(self):
        return self.pile.popleft()

class Filo(Pile):
    def retrieve(self):
        return self.pile.pop()
```

```python
# Testez Fifo
fifo = Fifo()
for i in range(1, 4):
    fifo.store(i)
while fifo:
    print(f"retrieve → {fifo.retrieve()}")

# Testez Filo
filo = Filo()
for i in range(1, 4):
    filo.store(i)
while filo:
    print(f"retrieve → {filo.retrieve()}")

```

**Questions :**
1. Quelle est la différence dans l'ordre des éléments récupérés entre Fifo et Filo ?

---

### Étape 2 : Représentation d'un Graphe

Implémentez une classe `Tree` pour représenter un sommet :

```python
class Tree:
    def __init__(self, name):
        self.neighbours = set()
        self.name = name

    def add_neighbour(self, other):
        self.neighbours.add(other)

    def __len__(self):
        return len(self.neighbours)

    def __repr__(self):
        return f"Le sommet s'appelle {self.name} et a {len(self)} voisins."
```

#### Créez un graphe binaire :

```python
def tree_vertex(name, depth):
    if depth == 0:
        return Tree(name)
    elif depth > 0:
        result = Tree(name)
        result.add_neighbour(tree_vertex(name + '1', depth - 1))
        result.add_neighbour(tree_vertex(name + '2', depth - 1))
        return result

g = tree_vertex('v', 3)
```

#### Modifier le tree pour permettre les éléments suivants

```python
print(g)
print(len(g))
```


**Questions :**
1. Quelle structure est utilisée pour représenter les voisins d'un sommet ?
2. Que représente l'argument `depth` ?

---

### Étape 3 : Implémentation des Algorithmes de Parcours

Implémentez une fonction `scan` pour explorer un graphe :

```python
def scan(start, storage):
    storage.store(start)
    scanned = set()

    while storage:
        current = storage.retrieve()
        if current in scanned:
            continue
        yield current
        scanned.add(current)
        for neighbour in current.neighbours:
            storage.store(neighbour)
```

#### Testez les parcours :

```python
# DFS
for vertex in scan(g, Filo()):
    print(vertex)

# BFS
for vertex in scan(g, Fifo()):
    print(vertex)
```

**Questions :**
1. Pourquoi utilise-t-on un ensemble `scanned` ?
2. Quelle est la différence de comportement entre DFS et BFS dans cet exemple ?
3. Comment réécrire la fonction scan pour rendre le tout un peu plus object ?

```python
#Réimplémentation de Tree avec les méthodes dfs et bfs

class Tree:
    def __init__(self, name):
        self.neighbours = set()
        self.name = name

    def add_neighbour(self, other):
        self.neighbours.add(other)

    def __len__(self):
        return len(self.neighbours)

    def __repr__(self):
        return f"Le sommet s'appelle {self.name} et a {len(self)} voisins."
'''
    def bfs(self):
        for vertex in scan(g, self):
            print(vertex)'''
```

## Partie 3 : Applications des Générateurs

### Filtrage des Sommets

En utilisant `itertools`, affichez un sommet sur deux dans un parcours DFS :

```python
import itertools

df_scan = scan(g, Filo())
pass
```

**Exercice :**
1. Modifiez le code pour afficher les sommets à partir du troisième.

---

### Conclusion

Ce TP vous a permis de :

1. Implémenter des structures adaptées au DFS et BFS.
2. Manipuler un graphe et explorer ses sommets.
3. Utiliser des générateurs pour rendre l'exploration flexible.

**Question de réflexion :**
Comment pourriez-vous modifier ce code pour gérer un graphe avec des cycles ?

--- 

Vous pouvez maintenant adapter ce TP selon vos besoins spécifiques en ajoutant des exercices ou des variantes.
# hackaton2
