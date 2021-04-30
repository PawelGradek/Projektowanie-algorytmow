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
        masa = int(random.randint(50, 2000))
        zasieg = int(random.randint(1, 100))
        rozdzielczosc = int(random.randint(1, 30))

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


def wyszukiwanie_binarne(wektor, wartosc, parametr):
    for w in wartosc:
        lewa_gra = 0
        prawa_gra = len(wektor)
        ind = 0
        print('\nWartość ktora sprawdzamy:', w)
        while lewa_gra < prawa_gra:
            ind = (lewa_gra + prawa_gra) // 2
            print('Lewa granica:', lewa_gra, 'Prawa granica:', prawa_gra, 'Indeks środkowy:', ind)
            if wektor[ind][parametr] == w:
                return wektor[ind]
            elif wektor[ind][parametr] < w:
                lewa_gra = ind + 1
            else:
                prawa_gra = ind
    return None


random.seed(156894)
robot = Robot()
a = int(input('Wpisz rozmiar wektora robotow:')) #20
wektor = robot.opis_M_robotow(a)
print(wektor)
wartosci = [] # [300, 450, 270, 628]
b = int(input('Podaj liczbę ile wartości chcesz sprawdzić:')) #4
for i in range(1, b + 1):
    c = int(input(f'Wpisz {i} wartosc: '))
    wartosci.append(c)
wartosci.sort()
d = int(input('Wpisz numer parametru wzgledem którego chcesz sortować: ')) #2
parametr = d
sortowanie_parametr(parametr)
print(wyszukiwanie_binarne(wektor, wartosci, parametr))

