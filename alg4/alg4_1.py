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




def szukaj_robota(wektor1):
    parametry = ['identyfikator - 0','typ - 1', 'masa - 2', 'zasieg - 3', 'rozdzielczosc - 4']
    print(f'Podaj jeden parametr wzgledem ktorego chcesz szukac robota z podanej listy {parametry}')
    x = str(input('Wpisz parametr: '))
    y = str(input('Wpisz wartosci: '))
    #z = None
    def szukaj(wektor1, x, y):
        for i in range(len(wektor1)):
            print('Przeszukuje element wektora:', i)
            print('Przeszukiwany element:',wektor1[i])
            print('Przeszukiwana wartosci:',wektor1[i][x])
            if wektor1[i][x] == y:
                z = wektor1[i]
                print(z)
                break

    if x == '0':
        szukaj(wektor1, 0, y)

    elif x == '1':
        szukaj(wektor1, 1, y)

    elif x == '2':
        szukaj(wektor1, 2, y)

    elif x == '3':
        szukaj(wektor1, 3, y)

    elif x == '4':
        szukaj(wektor1, 4, y)

    else:
        print(None)



def szukaj_robota2(wektor1):
    y0 = str(input('Wpisz wartosci nr.0: '))
    y1 = str(input('Wpisz wartosci nr.1: '))
    y2 = str(input('Wpisz wartosci nr.2: '))
    y3 = str(input('Wpisz wartosci nr.3: '))
    y4 = str(input('Wpisz wartosci nr.4: '))
    z = []

    for i in range(len(wektor1)):
        print('Przeszukuje element wektora:', i)
        print('Przeszukiwany element:', wektor1[i])
        if wektor1[i][0] == y0 or wektor1[i][1] == y1 or wektor1[i][2] == y2 or wektor1[i][3] == y3 or wektor1[i][4] == y4:

            x = []
            print('Przeszukiwana wartosci:', wektor1[i][0])
            if wektor1[i][0] == y0:
                x.append(wektor1[i][0])
            if wektor1[i][0] != y0:
                x.append(None)
            print('Przeszukiwana wartosci:', wektor1[i][1])
            if wektor1[i][1] == y1:
                x.append(wektor1[i][1])
            if wektor1[i][1] != y1:
                x.append(None)
            print('Przeszukiwana wartosci:', wektor1[i][2])
            if wektor1[i][2] == y2:
                x.append(wektor1[i][2])
            if wektor1[i][2] != y2:
                x.append(None)
            print('Przeszukiwana wartosci:', wektor1[i][3])
            if wektor1[i][3] == y3:
                x.append(wektor1[i][3])
            if wektor1[i][3] != y3:
                x.append(None)
            print('Przeszukiwana wartosci:', wektor1[i][4])
            if wektor1[i][4] == y4:
                x.append(wektor1[i][4])
            if wektor1[i][4] != y4:
                x.append(None)
            z.append(x)
        if len(z) == None:
            print('Nie istnieje wektor1 o takich wartosciach')
    print(z)


def szukaj_robota3(wektor1):
    y0 = str(input('Wpisz wartosci nr.0: '))
    y1 = str(input('Wpisz wartosci nr.1: '))
    y2 = []
    y3 = []
    q1 = int(input('Wpisz ile elementów ma 2 wartość: '))
    q2 = int(input('Wpisz ile elementów ma 3 wartość: '))
    for i in range(q1):
        e1 = str(input('Wpisz element 2 wartości: '))
        y2.append(e1)
    for j in range(q2):
        e2 = str(input('Wpisz element 3 wartości: '))
        y3.append(e2)
    y4 = str(input('Wpisz wartosci nr.4: '))

    z = []

    for i in range(len(wektor1)):
        print('Przeszukuje element wektora:', i)
        print('Przeszukiwany element:', wektor1[i])
        tabu = []
        for j in range(q1):
            for n in range(q2):
                if wektor1[i][0] == y0 or wektor1[i][1] == y1 or wektor1[i][2] == y2[j] or wektor1[i][3] == y3[n] or wektor1[i][4] == y4 and wektor1[i] not in tabu:

                    x = []
                    print('Przeszukiwana wartosci:', wektor1[i][0])
                    if wektor1[i][0] == y0 :
                        x.append(wektor1[i][0])
                    if wektor1[i][0] != y0:
                        x.append(None)
                    print('Przeszukiwana wartosci:', wektor1[i][1])
                    if wektor1[i][1] == y1:
                        x.append(wektor1[i][1])
                    if wektor1[i][1] != y1:
                        x.append(None)
                    print('Przeszukiwana wartosci:', wektor1[i][2])
                    if wektor1[i][2] == y2[j]:
                        x.append(wektor1[i][2])
                    if wektor1[i][2] != y2[j]:
                        x.append(None)
                    print('Przeszukiwana wartosci:', wektor1[i][3])
                    if wektor1[i][3] == y3[n]:
                        x.append(wektor1[i][3])
                    if wektor1[i][3] != y3[n]:
                        x.append(None)
                    print('Przeszukiwana wartosci:', wektor1[i][4])
                    if wektor1[i][4] == y4:
                        x.append(wektor1[i][4])
                    if wektor1[i][4] != y4:
                        x.append(None)
                    z.append(x)
                    tabu.append(wektor1[i])
                if len(z) == None:
                    print('Nie istnieje wektor1 o takich wartosciach')
            z = z[:8]
    print(z)


random.seed(157268)
robot = Robot()
a = int(input('wpisz rozmiar wektora robotów: '))
x = robot.opis_M_robotow2(a)
print(x)
#szukaj_robota(x) #2, 623
#szukaj_robota2(x) #['rsgfa', 'AGV', '623', '4', '12']
szukaj_robota3(x) # ['rsgfa', 'AGV','2','2' '623','1894', '4', '19', '12']