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


    def opis_M_robotow(self):
        M = 20
        wektor = [[] for _ in range(M)]
        for i in range(M):
            wektor[i].append(''.join(random.sample('abcdefghijklmnoprstuwyz0123456789', 5)))
            wektor[i].append(random.choice(['AUV', 'AFV', 'AGV']))
            wektor[i].append(str(random.randint(50, 2000)))
            wektor[i].append(str(random.randint(1, 100)))
            wektor[i].append(str(random.randint(1, 30)))

        return wektor

    def opis_M_robotow2(self, M):
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


def sortowanie_wektora_robotow(wektor1, x= None):
    parametry = ['identyfikator - 0','typ - 1', 'masa - 2', 'zasieg - 3', 'rozdzielczosc - 4']
    print(f'Podaj jeden parametr wzgledem ktorego chcesz sortowac roboty z podanej listy {parametry}')
    x = str(input('Wpisz parametr: '))


    def sortuj(wektor1, x):
        z = []
        tabu = []
        for i in range(len(wektor1)):
            print('sortuje element',i)
            z.append(wektor1[i][x])
            z.sort()
        y = z.copy()

        for i in range(len(wektor1)):
            for j in range(len(z)):
                print('sprawdzam czy wartosc ', wektor1[i][x],' jest równa wartości ', z[j])
                if wektor1[i][x] == z[j] and (wektor1[i] not in tabu):
                    y[j] = wektor1[i]
                    tabu.append(wektor1[i])
        return y

    if x == '0':
        sortuj(wektor1, 0)

    if x == '1':
        sortuj(wektor1, 1)

    if x == '2':
        sortuj(wektor1, 2)

    if x == '3':
        sortuj(wektor1, 3)

    if x == '4':
        sortuj(wektor1, 4)



def wyszukiwanie_binarne(wektor, parametr, wartosc,  liczb = False, nazw = False):
    lewa_gra = 0
    prawa_gra = len(wektor)
    index = 0

    # Sprawdzamy czy zakres który jest badany, nie jest pusty
    while lewa_gra < prawa_gra:
        # dzielimy listę na 2 zbiory
        index = (lewa_gra + prawa_gra) // 2
        print('Obecnia numer indeksu wynosi ', index)

        # Jeżeli znaleźliśmy liczbę to kończymy
        # jeżeli lewa strona, jest mniejsza do ją odrzucamy
        # a jeżeli nie, to odrzucamy prawą stronę
        if wektor[index][parametr] == wartosc:
            return index
        else:
            if liczb:
                if wektor[index][parametr] < wartosc:
                    print('sprawdzam czy wartosc ',wektor[index][parametr],' jest mniejsza od', wartosc)
                    lewa_gra = index + 1
                else:
                    prawa_gra = index
            if nazw:
                u = []
                u.append(wektor[index][parametr])
                u.append(wartosc)
                u.sort()
                if wektor[index][parametr] == u[0]:
                    print('Sprawdzam czy wartosc ',wektor[index][parametr], ' jest rowna ', u[0])
                    lewa_gra = index + 1
                else:
                    prawa_gra = index

    return None



def szukaj_jednego_robota1(wektor1):
    parametry = ['identyfikator - 0','typ - 1', 'masa - 2', 'zasieg - 3', 'rozdzielczosc - 4']
    print(f'Podaj jeden p wzgledem ktorego chcesz szukac robota z podanej listy {parametry}')
    param = str(input('Wpisz p: '))
    wart = str(input('Wpisz wartosci: '))


    def szukaj1(wektor1, param, wart, liczb = False, nazw = False):
        z = []
        for i in range(len(wektor1)):
            print('Sortuje wartosc',wektor1[i][param])
            z.append(wektor1[i][param])
            z.sort()
            print(z)
        y = z.copy()
        print(y)
        index = wyszukiwanie_binarne(wektor1, param, wart, liczb = False, nazw = False)
        print(wektor1[index])

    if param == '0':
        szukaj1(wektor1, 0,wart, nazw=True)

    if param == '1':
        szukaj1(wektor1,1, wart, nazw=True)

    if param == '2':
        szukaj1(wektor1,2, wart, liczb=True)

    if param == '3':
        szukaj1(wektor1,3, wart, liczb=True)

    if param == '4':
        szukaj1(wektor1,4, wart, liczb=True)
    else:
        print(None)



def szukaj_jednego_robota2(wektor1):
    parametry = ['identyfikator - 0','typ - 1', 'masa - 2', 'zasieg - 3', 'rozdzielczosc - 4']
    print(f'Podaj jeden p wzgledem ktorego chcesz szukac robota z podanej listy {parametry}')
    param = str(input('Wpisz p: '))
    wart = str(input('Wpisz wartosci: '))
    wektor_wartosci = []
    dlugosc_wektora_wartosc = input('podaj liczbe elementów w wektorze wartosci parametrów')
    for i in dlugosc_wektora_wartosc:
        a = int(input('Podaj element wektora wartosci parametrow:'))
        wektor_wartosci.append(a)


    def szukaj1(wektor1, param, wart, liczb = False, nazw = False):
        z = []
        for i in range(len(wektor1)):
            print('Sortuje wartość',wektor1[i][param] )
            z.append(wektor1[i][param])
            z.sort()
            print(z)
        y = z.copy()
        print(y)
        index = wyszukiwanie_binarne(wektor1, param, wart, liczb = False, nazw = False)
        print(wektor1[index])

    if param == '0':
        for i in wektor_wartosci:
            szukaj1(wektor1, 0,wart, nazw=True)

    if param == '1':
        for i in wektor_wartosci:
            szukaj1(wektor1,1, wart, nazw=True)

    if param == '2':
        for i in wektor_wartosci:
            szukaj1(wektor1,2, wart, liczb=True)

    if param == '3':
        for i in wektor_wartosci:
            szukaj1(wektor1,3, wart, liczb=True)

    if param == '4':
        for i in wektor_wartosci:
            szukaj1(wektor1,4, wart, liczb=True)
    else:
        print(None)


random.seed(157268)
robot = Robot()
x = robot.opis_M_robotow()
szukaj_jednego_robota1(x)
#szukaj_jednego_robota2(x)


