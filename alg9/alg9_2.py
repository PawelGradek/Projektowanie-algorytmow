from collections import namedtuple, deque
from pprint import pprint as pp

inf = float('inf')
Edge = namedtuple('Krawedz', ['start', 'stop', 'koszt'])


class Graf():
    def __init__(self, krawedzie):
        self.krawedzie = [Edge(*krawedz) for krawedz in krawedzie]

        self.wierzcholki = {e.start for e in self.krawedzie} | {e.stop for e in self.krawedzie}

    def dijkstra(self, poczatek, koniec):
        assert poczatek in self.wierzcholki
        dystans = {vertex: inf for vertex in self.wierzcholki}
        poprzedni = {vertex: None for vertex in self.wierzcholki}
        dystans[poczatek] = 0
        q = self.wierzcholki.copy()
        sasiedzi = {wierzcholek: set() for wierzcholek in self.wierzcholki}
        for start, stop, koszt in self.krawedzie:
            sasiedzi[start].add((stop, koszt))
        # pp(neighbours)

        while q:
            # pp(q)
            u = min(q, key=lambda wierzcholek: dystans[wierzcholek])
            q.remove(u)
            if dystans[u] == inf or u == koniec:
                break
            for v, koszt in sasiedzi[u]:
                alt = dystans[u] + koszt
                if alt < dystans[v]:  # Relax (u,v,wypadly_teraz_i_w_pieciu_poprz)
                    dystans[v] = alt
                    poprzedni[v] = u
        # pp(previous)

        s, u = deque(), koniec
        while poprzedni[u]:
            s.appendleft(u)
            u = poprzedni[u]
        s.appendleft(u)
        return s


'''
        ciag, u = [], koniec
        while previous[u]:
            ciag.append(u)
            u = previous[u]
        ciag.append(u)
        ciag = ciag[::-1]
        return ciag'''


graph = Graf([("wypadly_teraz_i_w_pieciu_poprz", "nie_padly_w_5_loso", 7), ("wypadly_teraz_i_w_pieciu_poprz", "wypadly_teraz_ale_nie_w_poprz_pieciu", 9), ("wypadly_teraz_i_w_pieciu_poprz", "f", 8), ("nie_padly_w_5_loso", "wypadly_teraz_i_w_pieciu_poprz", 7), ("wypadly_teraz_ale_nie_w_poprz_pieciu", "wypadly_teraz_i_w_pieciu_poprz", 9), ("f", "wypadly_teraz_i_w_pieciu_poprz", 8),
              ("nie_padly_w_5_loso", "wypadly_teraz_ale_nie_w_poprz_pieciu", 10), ("nie_padly_w_5_loso", "d", 15), ("wypadly_teraz_ale_nie_w_poprz_pieciu", "nie_padly_w_5_loso", 11), ("d", "nie_padly_w_5_loso", 15),
              ("wypadly_teraz_ale_nie_w_poprz_pieciu", "d", 11), ("wypadly_teraz_ale_nie_w_poprz_pieciu", "f", 2), ("d", "wypadly_teraz_ale_nie_w_poprz_pieciu", 11), ("f", "wypadly_teraz_ale_nie_w_poprz_pieciu", 2),
              ("d", "e", 6), ("e", "d", 6),
              ("e", "f", 9), ("f", "e", 9)])


sciezka = graph.dijkstra("e", "wypadly_teraz_ale_nie_w_poprz_pieciu")
pp(sciezka)
red_edges = []
for i in range(len(sciezka) - 1):
    red_edges.append((f'{sciezka[i]}', f'{sciezka[i + 1]}'))
print(red_edges)
import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()
plt.figure(figsize=(6, 6))
G.add_edge("wypadly_teraz_i_w_pieciu_poprz", "nie_padly_w_5_loso", weight=7)
G.add_edge("wypadly_teraz_i_w_pieciu_poprz", "wypadly_teraz_ale_nie_w_poprz_pieciu", weight=9)
G.add_edge("wypadly_teraz_i_w_pieciu_poprz", "f", weight=8)

G.add_edge("nie_padly_w_5_loso", "wypadly_teraz_i_w_pieciu_poprz", weight=7)
G.add_edge("wypadly_teraz_ale_nie_w_poprz_pieciu", "wypadly_teraz_i_w_pieciu_poprz", weight=9)
G.add_edge("f", "wypadly_teraz_i_w_pieciu_poprz", weight=8)

G.add_edge("nie_padly_w_5_loso", "wypadly_teraz_ale_nie_w_poprz_pieciu", weight=10)
G.add_edge("nie_padly_w_5_loso", "d", weight=15)

G.add_edge("wypadly_teraz_ale_nie_w_poprz_pieciu", "nie_padly_w_5_loso", weight=10)
G.add_edge("d", "nie_padly_w_5_loso", weight=15)

G.add_edge("d", "wypadly_teraz_ale_nie_w_poprz_pieciu", weight=11)
G.add_edge("f", "wypadly_teraz_ale_nie_w_poprz_pieciu", weight=2)

G.add_edge("d", "e", weight=6)
G.add_edge("e", "d", weight=6)

G.add_edge("e", "f", weight=9)
G.add_edge("f", "e", weight=9)



edge_labels = dict([((u, v), d['weight']) for u, v, d in G.edges(data=True)])
print(edge_labels)

edge_colors = ['black' if not edge in red_edges else 'red' for edge in G.edges()]
print(edge_colors)
pos = nx.spring_layout(G)
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
nx.draw(G, pos, node_size=1000, edge_color=edge_colors)
nx.draw_networkx_labels(G, pos)
plt.show()
