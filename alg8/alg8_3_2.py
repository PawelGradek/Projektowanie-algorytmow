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
        # Wywołaj rekursywną funkcję pomocniczą, aby zapisać topologię
        # Sortuj zaczynając od wszystkich wierzchołków jeden po drugim
        a = input('Czy chcesz sortować z priorytetem T/N: ')
        priority = None
        if a =='T':
            priority = int(input('Wpisz zadanie priorytetowe według którego chcesz sortować topologicznie: '))

        if priority != None:
            for i in range(self.V):
                if visited[i] == False:
                    if i != priority:
                        self.topologicalSortUtil(i, visited, stack)
            self.topologicalSortUtil(priority, visited, stack)

        else:
            for i in range(self.V):
                if visited[i] == False:
                    self.topologicalSortUtil(i, visited, stack)
        return stack[::-1]


def creat_and_visualizating():
    a = 6 # int(input('Podaj ilosc wierzcholkow: '))
    g = Graph(a)
    # krawedzie = []
    # zadania_i_czas = []
    # for i in range(a):
    #     a1 = int(input(f'Podaj numer {i+1} zadania : '))
    #     a2 = int(input(f'Podaj czas wykonania {i+1} zadania : '))
    #     zadania_i_czas.append([a1, a2])
    task_and_time = [[0,4], [1,1], [2,3], [3,2], [4,5], [5,20]]
    q = 6 # int(input('Podaj ilosc krawędzi pomiędzy zadaniami: '))
    # for i in range(q):
    #     b = int(input(f'Podaj pierwsze zadanie dla {i+1} pary: '))
    #     c = int(input(f'Podaj drugie zadanie dla {i+1} pary: '))
    #     g.addEdge(b, c)
    #     krawedzie.append((b, c))
    edges1 = [(5,2),(5,0),(4,0),(4,1),(2,3),(3,1)]
    for i in edges1:
        g.addEdge(i[0],i[1])


    # g.topologicalSort() # priorytet=4
    list_of_time = list(g.topologicalSort())
    G = nx.DiGraph()
    print("Przechodzenie po grafie posortowanym topologicznie: ")
    print(list_of_time)

    time = 0
    final_list = []
    for i in list_of_time:
        for j in task_and_time:
            if i == j[0]:
                w1 = f'{i},{j[1]},{time}'
                time += j[1]
                final_list.append(w1)
    print('krawedzie ', edges1)
    print('lista ostateczna: ', final_list)

    final_list_from_edges = []
    for (i1, i2) in edges1:
        for j in final_list:
            if str(i1) == j[0]:
                e1 = j
                final_list_from_edges.append(e1)
    for (i1, i2) in edges1:
        for j in final_list:
            if str(i2) == j[0]:
                e1 = j
                final_list_from_edges.append(e1)
    print('lista do edges', final_list_from_edges)

    list_to_visualization = []
    for i in range(len(final_list_from_edges) // 2):
        list_to_visualization.append((final_list_from_edges[i], final_list_from_edges[i + 6]))
    print(list_to_visualization)
    G.add_edges_from(list_to_visualization)

    plt.figure(figsize=(4, 4))
    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos, node_color='y')
    nx.draw_networkx_labels(G, pos)
    nx.draw_networkx_edges(G, pos, edge_color='k', arrows=True)
    plt.show()

creat_and_visualizating()
