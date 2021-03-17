import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
# w networkx węzły mogą być dowolne hashable obiekt np łańcuch tekstowy, obraz
G.add_edge('A', 'B', weight=4)#dodaj pojedyńczą krawędź
G.add_edge('B', 'D', weight=2)
G.add_edge('A', 'C', weight=3)
G.add_edge('C', 'D', weight=4)

pos = nx.spring_layout(G)#Pozycjonuj węzły za pomocą algorytmu kierowanego siłą Fruchtermana-Reingolda
#pos ( słownik ) - Słownik z węzłami jako kluczami i pozycjami jako wartościami. Pozycje powinny być sekwencjami o długości 2
nx.draw_networkx_nodes(G, pos, node_size = 500)#Narysuj węzły wykresu G  500 -to rozmiar wierzchołków
nx.draw_networkx_labels(G, pos)#Narysuj etykiety węzłów na wykresie G np. napisz A,B,C,D
nx.draw_networkx_edges(G, pos)#Narysuj krawędzie wykresu G
plt.show()


import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

G = nx.Graph()
VV = [1, 2, 3, 4, 5]#węzły w naszym grafie
WW = [(1, 2), (2, 3), (3, 4), (4, 5), (1, 3), (3, 5)]
Vx = {1:0, 2:1, 3:2, 4:3, 5:4}
Vy = {1:0, 2:1, 3:0, 4:-1, 5:0}

g = nx.Graph()
gpos = {}# słownik w którym będziemy mieli tuple składające się z [Vx[v], Vy[v]], gpos ( słownik ) - Słownik z węzłami jako kluczami i pozycjami
# jako wartościami. Pozycje powinny być sekwencjami o długości 2

for v in VV:
    g.add_node(v)#Dodaj pojedynczy węzeł, węzeł jest to wierzchołek
    gpos[v] = [Vx[v], Vy[v]]

for v1 in VV:
    for v2 in VV:
        if (v1, v2) in WW:
            label = str(np.sqrt((Vx[v1] - Vx[v2])**2 + (Vy[v1] - Vy[v2])**2))
            g.add_weighted_edges_from([(v1, v2, label)])# dodaj krawędzie z wagami

nx.draw(g, gpos, with_labels=True, node_color='yellow')#Narysuj wykres G za pomocą Matplotlib,
# with_labels ( bool, optional (default = True ) ) - Ustaw na True, aby rysować etykiety na węzłach node color - kolor węzłów
labels = nx.get_edge_attributes(g, 'weight')#Uzyskaj atrybuty krawędzi z wykresu
nx.draw_networkx_edge_labels(g, gpos, edge_labels=labels)#Narysuj etykiety krawędzi, edge_labels ( Dictionary ) - Etykiety krawędziw słowniku z kluczem
# za pomocą dwóch krotek etykiet tekstowych (domyślnie = Brak). Rysowane są tylko etykiety kluczy w słowniku
plt.show()


#Napisz program wyświetlający graf pełny o parametrach: liczba wierzchołków zadana parametrycznie (jako
#stała w programie), wierzchołki rozmieszczone na okręgu, w równych odstępach, etykiety wierzchołkow są
#kolejnymi liczbami naturalnymi.


# to ma być graf pełny
import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

# n- liczba wierzchołków
n = 6

while n > 0:
    for i in range(1, n):
        G.add_edge(i, n, weight=2)
    n = n - 1


a = nx.draw_circular(G, with_labels = True, node_color='blue')
#nx.circular_layout(G)
plt.show()




#Napisz program losujący graf o parametrycznie zadanej liczbie wierzchołków. Wierzchołki są rozmieszczone
#w losowych punktach (całego obszaru grafu) ale tak, żeby na siebie nie zachodziły. Wierzchołki dodawaj
#do grafu pojedynczo, jeśli wylosowany wierzchołek zachodzi na inny, to wylosuj nową pozycję dodawanego
#(powtarzaj tyle razy, aż nie będzie kolizji). Przerwij działanie programu, jeśli nie udało się wygenerować
#grafu po 100 nieudanych próbach dodania wierzchołka.

import networkx as nx
import matplotlib.pyplot as plt
import random
import sys


#n- liczba wierzchołków
n = 10
Vx = {}
Vy = {}
k = 0
VV = []#węzły w naszym grafie
for i in range(1, n + 1):
    VV.append(i)
    a = random.randrange(-30,30)
    b = random.randrange(-30,30)
    if a in Vx.values() and b in Vy.values():
        k = k + 1
        if k == 100:
            print("Nie możemy uzyskać grafu po 100 nieudanych próbach")
            sys.exit(0)
    else:
        Vx[i] = a
        Vy[i] = b

g = nx.Graph()
gpos = {}

for v in VV:
    g.add_node(v)#Dodaj pojedynczy węzeł, węzeł jest to wierzchołek
    gpos[v] = [Vx[v], Vy[v]]

nx.draw(g, gpos, with_labels=True, node_color='yellow')#Narysuj wykres G za pomocą Matplotlib,
plt.show()