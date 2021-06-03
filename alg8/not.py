from collections import defaultdict
import networkx as nx
import matplotlib.pyplot as plt



class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices # Liczba wierzchołków

    def addEdge(self, u, v): # g.addEdge(5, 2)
        self.graph[u].append(v)


    def topologicalSortUtil(self, v, visited, stack):


        # Zaznacz wierzchołek jako odwiedzony
        visited[v] = True

        # Powtarzaj dla wszystkich wierzchołków sąsiadujących z tym wierzchołkiem
        for i in self.graph[v]:
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)

        # Wepchnij bieżący wierzchołek na stos, który przechowuje wynik
        if v not in stack:
            stack.append(v)


    def topologicalSort(self):
        # Zaznacz wszystkie wierzchołki jako nieodwiedzone
        visited = [False] * self.V
        stack = []
        priorytet = 4
        # Wywołaj rekursywną funkcję pomocniczą, aby zapisać topologię
        # Sortuj zaczynając od wszystkich wierzchołków jeden po drugim


        for i in range(self.V):
            if visited[i] == False:
                if i != priorytet:
                    self.topologicalSortUtil(i, visited, stack)
        self.topologicalSortUtil(priorytet, visited, stack)



        return stack[::-1]


def metoda_tworzaca_i_wyswietlajaca():
    g = Graph(6)
    g.addEdge(5, 2)
    g.addEdge(5, 0)
    g.addEdge(4, 0)
    g.addEdge(4, 1)
    g.addEdge(2, 3)
    g.addEdge(3, 1)

    g.topologicalSort()
    listaczasow = list(g.topologicalSort())
    G = nx.DiGraph()
    print(listaczasow)
    zadania_i_czas = [[0,2],[1,3],[2,6],[3,2],[4,1],[5,7]]
    krawedzie = [(5, 2), (5, 0), (4, 0), (4, 1), (2, 3), (3, 1)]

    time = 0
    lista_ostateczna = []
    for i in listaczasow:
        for j in zadania_i_czas:
            if i == j[0]:
                w1 = f'{i},{j[1]},{time}'
                time += j[1]
                lista_ostateczna.append(w1)
    print('krawedzie ', krawedzie)
    print('lista ostateczna: ', lista_ostateczna)


    lista_do_edges_from = []
    for (i1,i2) in krawedzie:
        for j in lista_ostateczna:
            if str(i1) == j[0] :
                e1 = j
                lista_do_edges_from.append(e1)
    for (i1,i2) in krawedzie:
        for j in lista_ostateczna:
            if str(i2) == j[0] :
                e1 = j
                lista_do_edges_from.append(e1)
    print('lista do edges', lista_do_edges_from)

    lista_do_edges_from_ostateczna = []
    for i in range(len(lista_do_edges_from)//2):
        lista_do_edges_from_ostateczna.append((lista_do_edges_from[i], lista_do_edges_from[i+6]))
    print(lista_do_edges_from_ostateczna)
    G.add_edges_from(lista_do_edges_from_ostateczna)

    plt.figure(figsize=(4, 4))
    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos, node_color='y')
    nx.draw_networkx_labels(G, pos)
    nx.draw_networkx_edges(G, pos, edge_color='k', arrows=True)
    plt.show()

metoda_tworzaca_i_wyswietlajaca()



