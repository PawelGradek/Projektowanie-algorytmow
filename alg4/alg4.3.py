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
        masa = str(random.randint(50, 2000))
        zasieg = str(random.randint(1, 100))
        rozdzielczosc = str(random.randint(1, 30))

        return [identyfikator, typ, masa, zasieg, rozdzielczosc]


    def opis_M_robotow2(self):
        M = 20
        wektor = [[] for _ in range(M)]
        for i in range(M):
            wektor[i].append(''.join(random.sample('abcdefghijklmnoprstuwyz0123456789', 5)))
            wektor[i].append(random.choice(['AUV', 'AFV', 'AGV']))
            wektor[i].append(str(random.randint(50, 2000)))
            wektor[i].append(str(random.randint(1, 100)))
            wektor[i].append(str(random.randint(1, 30)))

        return wektor

    def opis_M_robotow(self, M):
        wektor_robotow = []
        for m in range(M):
            wektor_robotow.append(self.opis_robota())
        return wektor_robotow


    def wyswietl_strukture(self):
        struktura = self.opis_M_robotow()
        for i in range(len(struktura)):
            print(struktura[i], end='\n')

    def zapis_odczyt(self, odczyt = False, zapis = False, struktura = ''):
        if odczyt == True:
            filepath = "dane.txt"
            f = open(filepath, "wartosc", encoding="utf-8")
            for line in f:
                print(line, end="")
            f.close()

        if zapis == True:
            filepath = "dane.txt"
            f = open(filepath, "w")
            f.write(struktura) # argumentem do zapisu musi być string nie lista krotka
            f.close()

#zad 3.1
def funkcja_haszujaca(wektor1, H, liczba=0, nazwa= 0):
    for i in wektor1:
        if type(i) == str:
            nazwa = nazwa + len(i)
        if type(i) == int:
            zmienna_pomocnicza = 0
            mnoznik = 1
            for l in str(i):
                zmienna_pomocnicza = zmienna_pomocnicza + int(l) * mnoznik
                mnoznik = mnoznik + 1
            liczba = liczba + zmienna_pomocnicza
    return liczba * nazwa % H


#zad3.2
# noinspection PyTypeChecker
def wektor_wartosci_fun_hasz(wektor, H):
    assert H > len(wektor), 'niepoprawne H'
    wektor_wartosci = [None] * H
    for n in range(len(wektor)):
        h = funkcja_haszujaca(wektor[n], H)
        if wektor_wartosci[h] is None:
            wektor_wartosci[h] = n
        else:
            flag = True
            for i in range(h, len(wektor_wartosci)-h):
                if wektor_wartosci[h+i] is None:
                    wektor_wartosci[h + i] = n
                    flag = False
                    break
            if flag:
                for i in range(h):
                    if wektor_wartosci[i] is None:
                        wektor_wartosci[i] = n
                        break
    return wektor_wartosci

#zad3.3
def wyszukiwanie_robota_hasz(wartosci, wektor, wektor_wartosci, H):
    h = funkcja_haszujaca(wartosci, H)
    n = wektor_wartosci[h]
    if wartosci == wektor[n]:
        return True
    else:
        for i in range(n, len(wektor)):
            if wartosci == wektor[i]:
                return True
    return False


random.seed(157268)
robot = Robot()
wektor1 = robot.opis_robota()
wektor = robot.opis_M_robotow(10)
print(wektor)
print(funkcja_haszujaca(wektor1, 7))

wektor_wartosci = wektor_wartosci_fun_hasz(wektor, int(len(wektor) * 1.5))
print(wektor_wartosci)
print(wyszukiwanie_robota_hasz(['imcft', 'AGV', '1295', '15', '24'], wektor, wektor_wartosci, len(wektor_wartosci)))
