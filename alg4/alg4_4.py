
import random

class Robot():
    def __init__(self):
        self.identyfikator = ''.join(random.sample('abcdefghijklmnoprstuwyz0123456789', 5))
        self.typ = random.choice(['AUV', 'AFV', 'AGV'])
        self.masa = random.randint(50, 2000)
        self.zasieg = random.randint(1, 1000)
        self.rozdzielczosc = random.randint(1, 30)

    def opis_robota(self):
        identyfikator = ''.join(random.sample('abcdefghijklmnoprstuwyz0123456789', 5))
        typ = random.choice(['AUV', 'AFV', 'AGV'])
        masa = random.randint(50, 2000)
        zasieg = random.randint(1, 1000)
        rozdzielczosc = random.randint(1, 30)
        return [identyfikator, typ, masa, zasieg, rozdzielczosc]

    def opis_M_robotow(self, M):
        wektor_robotow = []
        for m in range(M):
            wektor_robotow.append(self.opis_robota())
        return wektor_robotow



def sortowanie_parametr(p):
    def sort_identyfikator(parametr):
        return parametr[0]

    if p == 0:
        return wektor.sort(key=sort_identyfikator)

    def sort_typ(parametr):
        return parametr[1]

    if p == 1:
        return wektor.sort(key=sort_typ)
    def sort_masa(parametr):
        return parametr[2]

    if p == 2:
        return wektor.sort(key=sort_masa)

    def sort_zakres(parametr):
        return parametr[3]

    if p == 3:
        return wektor.sort(key=sort_zakres)

    def sort_rozdzielczosc(parametr):
        return parametr[4]

    if p == 4:
        return wektor.sort(key=sort_rozdzielczosc)


def wyszukiwanie_binarne(wektor, wartosc, parametr, lewa_gra, prawa_gra, index):
    print('\nSprawdzamy:', wartosc)
    while lewa_gra <= index and index <= prawa_gra:
        index = (lewa_gra + prawa_gra) // 2
        if lewa_gra == index == prawa_gra:
            break

        print('Lewa granica:', lewa_gra, 'Prawa granica:', prawa_gra, 'Numer indexu:', index, 'Sprawdzana wartosc:', wektor[index][parametr])
        if wektor[index][parametr] == wartosc:
            if wektor[index] in tab1:
                break
            tab1.append(wektor[index])
            tab2.append(index)
            if lewa_gra == index and index == prawa_gra:
                break
            wyszukiwanie_binarne(wektor, wartosc, parametr, lewa_gra, index, (lewa_gra + index) // 2)
            if lewa_gra == index and index == prawa_gra:
                break
            wyszukiwanie_binarne(wektor, wartosc, parametr, index, prawa_gra, (prawa_gra + index) // 2)
        elif wektor[index][parametr] < wartosc:
            lewa_gra = index + 1
            index += 1
        else:
            prawa_gra = index

    return tab2


def func_glob(vector, targets, parameter, left, right, index):
    global tab1
    global tab2
    tab1 = []
    tab2 = []

    for target in targets:
        x = wyszukiwanie_binarne(vector, target, parameter, left, right, index)
        x.sort()
    return x





random.seed(254279)
robot = Robot()
a = int(input('Wpisz rozmiar wektora robotów: ')) #1000
wektor = robot.opis_M_robotow(a)

wartosci = [] # sprawdzamy czy w naszym wektorze znajdują sie wartosci z zakresu 420 -430
for i in range(420, 430):
    wartosci.append(i)
wartosci.sort()

b = int(input('Wpisz parametr wzgledem ktorego chcesz sortować: ')) # 3
parametr = b
sortowanie_parametr(parametr)
print(func_glob(wektor, wartosci, parametr, 0, len(wektor), 1))
print(wektor)
