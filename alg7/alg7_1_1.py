import sys

class Wezel:
    def __init__(self, dane):
        self.dane = dane
        self.lewe = None
        self.prawe = None


def sprawdz_czy_tree_to_bst(wierzcholek, min, max):
    if wierzcholek == None:
        return 1

    if wierzcholek.dane < min:
        return 0
    if wierzcholek.dane > max:
        return 0

    return sprawdz_czy_tree_to_bst(wierzcholek.prawe, wierzcholek.dane, max) and sprawdz_czy_tree_to_bst(wierzcholek.lewe, min, wierzcholek.dane)

korzen = Wezel(6)
korzen.lewe = Wezel(3)
korzen.prawe = Wezel(9)
korzen.lewe.lewe = Wezel(1)
korzen.lewe.prawe = Wezel(5)
korzen.prawe.lewe = Wezel(7)
korzen.prawe.prawe = Wezel(11)

mini = -sys.maxsize - 1
maxi = sys.maxsize

if (sprawdz_czy_tree_to_bst(korzen, mini, maxi)):
    print('To drzewo to BST')
else:
    print('To drzewo nie jest BST')
