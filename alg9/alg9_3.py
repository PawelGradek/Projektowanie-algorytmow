from math import inf
from itertools import product


def floyd_warshall(n, krawedz):
    rn = range(n)
    dystans = [[inf] * n for i in rn]
    nxt = [[0] * n for i in rn]
    for i in rn:
        dystans[i][i] = 0
    for u, v, w in krawedz:
        dystans[u - 1][v - 1] = w
        nxt[u - 1][v - 1] = v - 1
    for k, i, j in product(rn, repeat=3):
        sum_ik_kj = dystans[i][k] + dystans[k][j]
        if dystans[i][j] > sum_ik_kj:
            dystans[i][j] = sum_ik_kj
            nxt[i][j] = nxt[i][k]
    s = []
    for i, j in product(rn, repeat=2):
        if i != j:
            sciezka = [i]
            while sciezka[-1] != j:
                sciezka.append(nxt[sciezka[-1]][j])
            l = [i + 1, j + 1], dystans[i][j],      [p + 1 for p in sciezka]
            s.append(l)

    return s

lista_floyda = floyd_warshall(4, [[1, 3, -2], [2, 1, 4], [2, 3, 3], [3, 4, 2], [4, 2, -1]
                                  # [3, 1, -2], [1, 2, 4], [3, 2, 3], [4, 3, 2], [2, 4, -1]
                                  ])

# wybór wierzchołków

start = 2
stop = 3

sciezka1 = "p"
sciezka2 = "k"
dlugosc1 = 'l1'
dlugosc2 = 'l2'
for i in lista_floyda:
    print(i)
print()
for i in lista_floyda:
    if i[0] == [start, stop]:
        grupa1 = i
        sciezka1 = i[2]
        dlugosc1= i[1]


sciezka_wlasciwa = sciezka1

print('Wlasciwa sciezka to ta:  ',sciezka_wlasciwa)
red_edges = []
for i in range(len(sciezka_wlasciwa)-1):
    red_edges.append((int(sciezka_wlasciwa[i]),int(sciezka_wlasciwa[i+1])))
print(red_edges)

import networkx as nx
import matplotlib.pyplot as plt

krawedzie = [-2, 4, 3, 2, -1]
VV = [1, 2, 3, 4, 5]
WW = [(1, 3), (2, 1), (2, 3), (3, 4), (4, 2)]
Vx = {1:0, 2:1, 3:2, 4:3}
Vy = {1:0, 2:1, 3:-0.5, 4: 0}

g = nx.DiGraph()
gpos = {}

for v in VV[:-1]:
    g.add_node(v)
    gpos[v] = [Vx[v], Vy[v]]
for v1 in range(len(VV)):
    for v2 in range(len(VV)):
        if (VV[v1], VV[v2]) in WW:
            g.add_weighted_edges_from([(VV[v1], VV[v2], krawedzie[v1])])

edge_labels = dict([((u, v,), d['weight'])for u, v, d in g.edges(data=True)])

edge_colors = ['black' if not edge in red_edges else 'red' for edge in g.edges()]



nx.draw(g, gpos, with_labels=True, node_color='yellow', node_size=1000, edge_color=edge_colors)
labels = nx.get_edge_attributes(g, 'weight')
nx.draw_networkx_edge_labels(g, gpos, edge_labels=labels)
plt.show()