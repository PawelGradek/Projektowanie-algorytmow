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


#zad 3.1
def funkcja_haszujaca(wektor1, H):
    wartosc_int = 0
    wartosc_str = 0
    for i in wektor1:
        print('Sprawdzam element:',i)
        if type(i) == str:
            wartosc_str += len(i)
        if type(i) == int:
            zmienna_pomocnicza = 0
            mnoznik = 1
            for l in str(i):
                zmienna_pomocnicza += int(l) * mnoznik
                mnoznik += 1
            wartosc_int += zmienna_pomocnicza
    return wartosc_int * wartosc_str % H


#zad3.2
# noinspection PyTypeChecker
def wektor_wartosci_fun_hasz(wektor, H):
    assert H > len(wektor), 'niepoprawne H'

    wektor_wartosci = [None] * H
    for n in range(len(wektor)):
        h = funkcja_haszujaca(wektor[n], H)
        print(f'Sprawdzam czy element {wektor_wartosci[h]} ma wartosc None')
        if wektor_wartosci[h] is None:
            wektor_wartosci[h] = n
        else:
            flag = True
            for i in range(h, len(wektor_wartosci)-h):
                print(f'Sprawdzam czy element {wektor_wartosci[h+i]} ma wartosc None')
                if wektor_wartosci[h+i] is None:
                    wektor_wartosci[h + i] = n
                    flag = False
                    break

            if flag:
                for i in range(h):
                    #print(f'Sprawdzam czy element {wektor_wartosci[h + i]} ma wartosc None')
                    if wektor_wartosci[i] is None:
                        wektor_wartosci[i] = n
                        break

    return wektor_wartosci

#zad3.3
def wyszukiwanie_robota_hasz(wartosci, wektor, wektor_wartosci, H):
    h = funkcja_haszujaca(wartosci, H)
    n = wektor_wartosci[h]
    print(f'Sprawdzam czy element {wartosci} ma wartosc równą {wektor[n]}')
    if wartosci == wektor[n]:
        return True
    else:
        for i in range(n, len(wektor)):
            print(f'Sprawdzam czy element {wartosci} ma wartosc równą {wektor[i]}')
            if wartosci == wektor[i]:
                return True
    return False


random.seed(157268)
robot = Robot()
wektor1 = robot.opis_robota()
a = int(input('Wpisz rozmiar wektora robotów: '))#10
wektor = robot.opis_M_robotow(a)
print(wektor)

print(funkcja_haszujaca(wektor1, 7))

wektor_wartosci = wektor_wartosci_fun_hasz(wektor, int(len(wektor) * 1.3))
print(wektor_wartosci)

wartosci1 = ['rsgfa', 'AGV', 623, 26, 12]


print(wyszukiwanie_robota_hasz(wartosci1, wektor, wektor_wartosci, len(wektor_wartosci)))

wartosci2 =['l5ya0', 'AUV', 1608, 683, 19]

print(wyszukiwanie_robota_hasz(wartosci2, wektor, wektor_wartosci, len(wektor_wartosci)))
