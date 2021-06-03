import random
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

# wizualizacja drzewa

import random

class Robot():
    def __init__(self):
        self.identyfikator = ''.join(random.sample('abcdefghijklmnoprstuwyz0123456789', 5))
        self.typ = random.choice(['AUV', 'AFV', 'AGV'])
        self.masa = str(random.randint(50, 2000))
        self.zasieg = str(random.randint(1, 100))
        self.rozdzielczosc = str(random.randint(1, 30))


    def opis_robota(self):
        identyfikator = ''.join(random.sample('abcdefghijklmnoprstuwyz0123456789', 5))
        typ = random.choice(['AUV', 'AFV', 'AGV'])
        masa = int(random.randint(50, 2000))
        zasieg = int(random.randint(1, 100))
        rozdzielczosc = int(random.randint(1, 30))

        return [identyfikator, typ, masa, zasieg, rozdzielczosc]

    def opis_M_robotow(self, M):
        wektor_robotow = []
        for m in range(M):
            wektor_robotow.append(self.opis_robota())
        return wektor_robotow

random.seed(15726)


robot = Robot()
wektor1 = robot.opis_M_robotow(10)
print(wektor1)

a = int(input('Podaj parametr robota 2, 3, 4: '))
wektor_pomocniczy = []
for i in range(len(wektor1)):
    wektor_pomocniczy.append(wektor1[i][a])
print(wektor_pomocniczy)


############################
class Wezel():
    def __init__(self, x):
        self.dane = x
        self.lewe = None
        self.prawe = None


def generuj_drzewo_z_wlas_listy(wektor):
    if len(wektor) == 0:
        return None
    korzen = Wezel(random.choice(wektor))
    index = wektor.index(korzen.dane)
    korzen.lewe = generuj_drzewo_z_wlas_listy(wektor[:index])
    korzen.prawe = generuj_drzewo_z_wlas_listy(wektor[index + 1:])
    return korzen

def generuj_drzewo(wektor_pomocniczy, isBST = False):

    lista_wierz = wektor_pomocniczy
    n = len(lista_wierz)

    wlas_lista = []
    for _ in range(n-1):
        a = random.choice(lista_wierz)
        wlas_lista.append(a)
        lista_wierz.remove(a)
    if isBST:
        wlas_lista.sort()
    else:
        random.shuffle(wlas_lista)

    korzen = generuj_drzewo_z_wlas_listy(wlas_lista)
    return korzen

def lewa_szerokosc(korzen):
    return szerokosc(korzen.lewe)

def prawa_szerokosc(korzen):
    return szerokosc(korzen.prawe)

def szerokosc(korzen):
    if korzen == None:
        return 0
    return szerokosc(korzen.lewe) + 1 + szerokosc(korzen.prawe)

def wysokosc(korzen):
    if korzen == None:
        return 0
    return max(wysokosc(korzen.lewe), wysokosc(korzen.prawe)) + 1

d_hor = 4   #odleglosc pomiedzy wierzcholkami (szerokosc)
d_vec = 8   #odleglosc pomiedzy wierzcholkami (wysokosc)
radius = 2  #wierzcholek radius

def szerokosc_wysokosc(korzen):
    w = szerokosc(korzen)
    h = wysokosc(korzen)
    return w, h
def plot_wierzcholki(x, y, val, ax):
    c_node = Circle((x,y), radius=radius, color='yellow')
    ax.add_patch(c_node)
    plt.text(x, y, '%d' % val, ha='center', va= 'bottom',fontsize=11)

def plot_krawedzie(x1, y1, x2, y2, r=radius):
    x = (x1, x2)
    y = (y1, y2)
    plt.plot(x, y, 'k-')

def stworz_okno(korzen):
    SZEROKOSC, WYSOKOSC = szerokosc_wysokosc(korzen)
    SZEROKOSC = (SZEROKOSC+1)*d_hor
    WYSOKOSC = (WYSOKOSC+1)*d_vec
    fig = plt.figure(figsize=(11, 9))
    ax = fig.add_subplot(111)
    plt.xlim(0, SZEROKOSC)
    plt.ylim(0, WYSOKOSC)

    x = (lewa_szerokosc(korzen) + 1) * d_hor
    y = WYSOKOSC - d_vec
    return fig, ax, x, y

def przejscie_inorder(korzen, x, y, ax):
    if korzen == None:
        return
    plot_wierzcholki(x, y, korzen.dane, ax)
    lx = rx = 0
    ly = ry = y - d_vec
    if korzen.lewe != None:
        lx = x - d_hor * (prawa_szerokosc(korzen.lewe) + 1)
        plot_krawedzie(x, y, lx, ly, radius)
    if korzen.prawe != None:
        rx = x + d_hor * (lewa_szerokosc(korzen.prawe) + 1)
        plot_krawedzie(x, y, rx, ry, radius)

    przejscie_inorder(korzen.lewe, lx, ly, ax)
    przejscie_inorder(korzen.prawe, rx, ry, ax)


def wyswietl_BT(korzen):
    _, ax, x, y = stworz_okno(korzen)
    przejscie_inorder(korzen, x, y, ax)
    plt.show()

def main():
    root = generuj_drzewo(wektor_pomocniczy, True)
    wyswietl_BT(root)


if __name__ == '__main__':
    main()
