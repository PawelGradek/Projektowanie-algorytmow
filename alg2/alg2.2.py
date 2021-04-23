import networkx as nx
import matplotlib.pyplot as plt
import random
import sys
import math


#p- liczba wierzchołków
n = 6
Vx = {}
Vy = {}
k = 0
VV = []#węzły w naszym grafie
for i in range(1, n + 1):
    a = random.randrange(0,100)
    b = random.randrange(0,100)
    if a in Vx.values() and b in Vy.values():
        k = k + 1
        if k == 100:
            print("Nie możemy uzyskać grafu po 100 nieudanych próbach")
            sys.exit(0)
        n = n + 1
    else:
        VV.append(i)
        Vx[i] = a
        Vy[i] = b

G = nx.Graph()

gpos = {}
for v in VV:
    G.add_node(v)#Dodaj pojedynczy węzeł, węzeł jest to wierzchołek
    gpos[v] = [Vx[v], Vy[v]]


odleglosci = {}
for i in VV:
    for j in VV:
        if i != j:
            dis = math.sqrt((gpos[i][0] - gpos[j][0]) ** 2 + ((gpos[i][1] - gpos[j][1]) ** 2))
            odleglosci[(i, j)] = dis

print(odleglosci)


#zad2
min_odleglosci = {}
i = 2
for i in range(2, n + 1):
    p = 0
    min_dis = 150
    for j in range(1, i):

        if odleglosci[(i, j)] < min_dis:
            min_dis = odleglosci[(i, j)]
            p = j
            print(i, ":", p)
    print('finalnie',i, ":", p)
    G.add_edge(i, p, weight=round(min_dis, 2))
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, gpos, edge_labels=labels)
    nx.draw(G, gpos, with_labels=True, node_color='yellow')
    plt.draw()
    plt.pause(1)
    plt.clf()












