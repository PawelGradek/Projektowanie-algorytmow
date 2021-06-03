# konwertowanie drzewa na BST

class Wezel:
    def __init__(self, dane):
        self.dane = dane
        self.lewe = None
        self.prawe = None


def Inorder(wiercholek, inorder):
    if wiercholek is None:
        return

    Inorder(wiercholek.lewe, inorder)
    inorder.append(wiercholek.dane)
    Inorder(wiercholek.prawe, inorder)


def licz_Wierzcholki(wierzcholek):
    if wierzcholek is None:
        return 0

    return licz_Wierzcholki(wierzcholek.lewe) + licz_Wierzcholki(wierzcholek.prawe) + 1



def array_BST(arr, wierzcholek):
    if wierzcholek is None:
        return

    array_BST(arr, wierzcholek.lewe)
    wierzcholek.dane = arr[0]
    arr.pop(0)
    array_BST(arr, wierzcholek.prawe)



def zamiana_BT_na_BST(wierzcholek):
    if wierzcholek is None:
        return
    n = licz_Wierzcholki(wierzcholek)
    arr = []
    Inorder(wierzcholek, arr)
    arr.sort()

    array_BST(arr, wierzcholek)


def printInorder(wierzcholek):
    if wierzcholek:
        printInorder(wierzcholek.lewe)
        print(wierzcholek.dane, printInorder(wierzcholek.prawe))



korzen = Wezel(10)
korzen.lewe = Wezel(30)
korzen.prawe = Wezel(15)
korzen.lewe.lewe = Wezel(20)
korzen.prawe.prawe = Wezel(5)


zamiana_BT_na_BST(korzen)


print('Przejście inorder po skonwertowaniu drzewa na BST')
printInorder(korzen)

