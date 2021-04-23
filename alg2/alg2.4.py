import networkx as nx
import matplotlib.pyplot as plt



class Graph:
    def __init__(self, edges, N):
        #tworzymy macierz z tyloma wierszami ile jest wierzcholkow
        self.sasiadujacy = [[] for _ in range(N)]

        # dodac krawedzie do nieskierowanego wykresu
        for (v1, v2) in edges:
            self.sasiadujacy[v1].append(v2)
            self.sasiadujacy[v2].append(v1)



def usl(graph):
    # sledz kolor przypisany do kazdego wierzcholka
    result = {}
    # przypisz kolor do wierzcholka jeden po drugim
    for u in range(N):
        # sprawdz kolor sasiednich wierzcholkow i zapisz je w zestawie
        # tworzymy zmienna w ktorej mamy wypisane wierzcholki czyli  klucze ze slownika result dla elementow ktore maja krawedz z tym wierzcholkiem
        przypisane = set([result.get(i) for i in graph.sasiadujacy[u] if i in result])# set- słownik z samymi kluczami, get - uzyskaj wartosc klucza i

        # sprawdz pierwszy wolny kolor
        color = 1
        for c in przypisane:
            #jezeli w zmiennej przypisane mamy wierzcholek 1 to wybieramy nastepny kolor
            if color != c:
                break
            color = color + 1

        # przypisz wierzchołkowi u pierwszy wolny kolor
        result[u] = color

    for v in range(N):
        print("Kolor przypisany do wierzchołka", v, "to", colors[result[v]])




colors = ["", "zielony", "niebieski","czerwony", "czarny","brązowy","żółty", "pomarańczowy", "biały"]
edges = [(0, 1), (0, 4), (0, 5), (4, 5), (1, 4), (1, 3), (2, 3), (2, 4)]
N = 6
# zbuduj wykres z podanych krawedzi
graph = Graph(edges, N)

usl(graph)

graph = nx.Graph()
for i in range(N):
    graph.add_node(i)

graph.add_edges_from(edges)


nx.draw(graph, with_labels=True, node_color='yellow')
plt.show()