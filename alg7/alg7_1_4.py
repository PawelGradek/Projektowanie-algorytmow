# Lista połaczona
class ListaPolaczona:
    def __init__(self):
        self.dane = None
        self.nastepny = None



class Wezel:
    def __init__(self):
        self.dane = None
        self.lewe = None
        self.prawe = None


def sortowanie_listy_BST():
    global glowny_wierz
    n = licz_wierzcholki(glowny_wierz)
    return sortowanie_listy_BST_rekur(n)



def sortowanie_listy_BST_rekur(n):
    global glowny_wierz
    if (n <= 0):
        return None
    lewe = sortowanie_listy_BST_rekur(int(n / 2))
    korzen = nowy_wierzcholek((glowny_wierz).dane)
    korzen.lewe = lewe
    glowny_wierz = (glowny_wierz).nastepny
    korzen.prawe = sortowanie_listy_BST_rekur(n - int(n / 2) - 1)

    return korzen


def licz_wierzcholki(glowny_wierz):
    licz = 0
    zm_pomoc = glowny_wierz
    while (zm_pomoc != None):
        zm_pomoc = zm_pomoc.nastepny
        licz = licz + 1

    return licz


# funkcja do wstawienia wierzcholka na poczatek polaczonej listy
def wstaw1(glowny_wierz, nowe_dane):
    # allocate wierzcholek
    nowy_wierz = ListaPolaczona()
    nowy_wierz.dane = nowe_dane
    nowy_wierz.nastepny = (glowny_wierz)
    (glowny_wierz) = nowy_wierz

    return glowny_wierz


def wypisz_liste(wierzcholek):
    while (wierzcholek != None):
        print(wierzcholek.dane, end=" ")
        wierzcholek = wierzcholek.nastepny



def nowy_wierzcholek(dane):
    wierzcholek = Wezel()
    wierzcholek.dane = dane
    wierzcholek.lewe = None
    wierzcholek.prawe = None

    return wierzcholek



def przechodzenie_preorder(wierzcholek):
    if (wierzcholek == None):
        return
    print(wierzcholek.dane, end=" ")
    przechodzenie_preorder(wierzcholek.lewe)
    przechodzenie_preorder(wierzcholek.prawe)



glowny_wierz = None


# połaczona lista be 1.2.3.4.5.6.7
glowny_wierz = wstaw1(glowny_wierz, 7)
glowny_wierz = wstaw1(glowny_wierz, 6)
glowny_wierz = wstaw1(glowny_wierz, 5)
glowny_wierz = wstaw1(glowny_wierz, 4)
glowny_wierz = wstaw1(glowny_wierz, 3)
glowny_wierz = wstaw1(glowny_wierz, 2)
glowny_wierz = wstaw1(glowny_wierz, 1)

print("Połączona lista ")
wypisz_liste(glowny_wierz)


korzen = sortowanie_listy_BST()
print("\nPrzejscie Preorder po BST ")
przechodzenie_preorder(korzen)

