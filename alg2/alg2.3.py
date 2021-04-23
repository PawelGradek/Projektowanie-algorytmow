
def stworz_graf():
    dictionary = {'A': {'B': 3, 'C': 5},
                  'B': {'C': 8, 'D': 7},
                  'C': {'E': 4, 'D': 2},
                  'D': {'F': 1},
                  'E': {'F': 3, 'D': 6},
                  'F': {'D': 3}
                  }

    return dictionary


def dist(v,w):
    graf = stworz_graf()

    if ((v == w)):
        print("v jest taki sam jak koncowy_wierzcholek")
        print("Wybierz inne wierzchołki")

    final_source = v
    droga = {}
    kolejka = []

    for wierzcholek in graf:# przechodzimy po kluczach w slowniku graf
        droga[wierzcholek] = float('inf') # przypisujemy każdemu kluczowi inf
        kolejka.append(wierzcholek) # dodajemy do kolejki kolejne wierzchołki

    print(droga)
    print(kolejka)


    dystans = []
    odwiedzone = []

    while v != w:
        try:
            droga[v] = 0 # wartosc wierzcholka poczatkowego jest rowna 0
            graf_dict = graf[v]# słownik okreslajacy odleglosci wierzcholka poczatkowego od innych wierzcholkow

            najkrotsza_droga = min(graf_dict.values()) # najkrotsza droga w slowniku ktory jest wartoscia wierzcholka poczatkowego

            s = None #zmienna pomocnicza
            for k in graf[v]: # przechodzimy petla po slowniku wierzcholka poczatkowego
                if (graf[v][k] == najkrotsza_droga and (k not in odwiedzone)): # żeby nie było cykli
                    dystans.append(najkrotsza_droga)
                    odwiedzone.append(k)
                    s = k

            v = s

            if (v == w):
                print("Dotarłeś do swojego wierzchołka.")
                final_visited = ' -> '.join([str(item) for item in odwiedzone])
                print(f"Droga po wierzchołkach : {final_source} -> {final_visited}")
                print(f"Suma wag  przebytych krawedzi : {sum(dystans)}")

        except KeyError:
            print("Nie możesz dotrzeć do punktu końcowego z tego źródła, ponieważ nie ma dostępnej ścieżki.")
            break

print(stworz_graf())
dist('A', 'F')