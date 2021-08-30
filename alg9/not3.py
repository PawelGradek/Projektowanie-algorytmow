import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

krawedzie = [-2, 4, 3, 2, -1]
VV = [1, 2, 3, 4, 5]
WW = [(1, 3), (2, 1), (2, 3), (3, 4), (4, 2)]
Vx = {1:0, 2:1, 3:2, 4:3}
Vy = {1:0, 2:1, 3:0, 4: 0}

g = nx.Graph()
gpos = {}

for v in VV[:-1]:
    g.add_node(v)
    gpos[v] = [Vx[v], Vy[v]]
for v1 in VV:
    for v2 in VV:
        if (v1, v2) in WW:
            g.add_weighted_edges_from([(v1, v2, krawedzie[v1])])

nx.draw(g, gpos, with_labels=True, node_color='yellow')
labels = nx.get_edge_attributes(g, 'weight')
nx.draw_networkx_edge_labels(g, gpos, edge_labels=labels)
plt.show()