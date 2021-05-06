import alg5_0
import random
random.seed(157268)

robot = alg5_0.Robot()

a = int(input("Podaj ilosc elementow tablicy: "))
wektor1 = robot.opis_M_robotow(a)
print(wektor1)


tablica_do_sortowania = []
for i in range(len(wektor1)):
    tablica_do_sortowania.append(wektor1[i][4])
print(tablica_do_sortowania)


def wypisz_liste(tab):  # tworzymy metode do wypiswania zawartosci naszej tablicy
    for el in tab:
        print(el, end=" | ")


def lista_min_max(tab): #tworzymy funkcje znajdujaca najwiekszy i najmniejszy element
    min = tab[0] #tworzymy zmienne pomocnicze
    max = tab[0]
    for el in tab:
        if el > max: # a nastepnie sprawdzamy czy sa one wieksz, lub mniejsze od iterowanej wartosci
            max = el
        if el < min:
            min = el
    array = []
    array.append(min) #na koniec wrzucamy je w tablice
    array.append(max)
    return array



def sortowanie_przez_zliczanie(tab, n):# n - ilosc elementow tanlicy
    minmax = lista_min_max(tab) #pobieramy skrajne elementy tablicy
    min = minmax[0]
    max = minmax[1]
    countersSize = max - min + 1 # liczymy potrzebna ilosc elementow
    counters = [0] * countersSize #i od razu tworzymy tablice licznikow
    print("\nStworzono tablice licznikow: ")
    for x in range(countersSize):
        print(x + min, "=0", end=" | ")

    for x in range(n):
        counters[tab[x] - min] += 1 # zliczamy ilosc elementow
    print("\nZliczono ilosc elementow: ")
    for x in range(countersSize):
        print(x+min, "=", counters[x], end=" | ")

    lastIndex = 0
    for x in range(countersSize): # a nastepnie wstawiamy je kolejno w wyjsciowa tablice
        y = lastIndex
        while y < counters[x] + lastIndex:
            tab[y] = x + min
            y += 1
        lastIndex = y




print("\nOto twoja tablica:")
wypisz_liste(tablica_do_sortowania)
sortowanie_przez_zliczanie(tablica_do_sortowania, a)
print("\nOto twoja tablica po sortowaniu:")
wypisz_liste(tablica_do_sortowania)
print('\n',tablica_do_sortowania)

wektor1_posortowany = []
tabu = []
for i in tablica_do_sortowania:
    for j in range(len(wektor1)):
        if i == wektor1[j][4] and wektor1[j] not in tabu:
            wektor1_posortowany.append(wektor1[j])
            tabu.append(wektor1[j])

print('\n',wektor1_posortowany)
