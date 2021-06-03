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

a = 3 #int(input('Podaj parametr robota 2, 3, 4: '))
wektor_pomocniczy = []
for i in range(len(wektor1)):
    wektor_pomocniczy.append(wektor1[i][a])
print(wektor_pomocniczy)

class Wezel:

    def __init__(self, dane):
        self.dane = dane
        self.lewe_dziecko = None
        self.prawe_dziecko = None

def inorder(korzen):
    if korzen is not None:
        inorder(korzen.lewe_dziecko)
        print(korzen.dane, end=" ")
        inorder(korzen.prawe_dziecko)

def wstaw_wierzcholek(wierzcholek, dane):
    if wierzcholek is None:
        return Wezel(dane)
    if dane < wierzcholek.dane:
        wierzcholek.lewe_dziecko = wstaw_wierzcholek(wierzcholek.lewe_dziecko, dane)
    else:
        wierzcholek.prawe_dziecko = wstaw_wierzcholek(wierzcholek.prawe_dziecko, dane)
    return wierzcholek


def usun_wierzcholek(korzen, dane):
    if korzen is None:
        return korzen

    if dane < korzen.dane:
        korzen.lewe_dziecko = usun_wierzcholek(korzen.lewe_dziecko, dane)
        return korzen
    elif (dane > korzen.dane):
        korzen.prawe_dziecko = usun_wierzcholek(korzen.prawe_dziecko, dane)
        return korzen

    if korzen.lewe_dziecko is None and korzen.prawe_dziecko is None:
        return None

    if korzen.lewe_dziecko is None:
        pomocnicza = korzen.prawe_dziecko
        korzen = None
        return pomocnicza
    elif korzen.prawe_dziecko is None:
        pomocnicza = korzen.lewe_dziecko
        korzen = None
        return pomocnicza

    successor0 = korzen
    successor = korzen.prawe_dziecko

    while successor.lewe_dziecko != None:
        successor0 = successor
        successor = successor.lewe_dziecko

    if successor0 != korzen:
        successor0.lewe_dziecko = successor.prawe_dziecko
    else:
        successor0.prawe_dziecko = successor.prawe_dziecko
    korzen.dane = successor.dane
    return korzen


korzen = None
for i in wektor_pomocniczy:
    korzen = wstaw_wierzcholek(korzen, i)

print("Przechodzenie drzewa Inorder")
inorder(korzen)

print("\nUsuń 55")
korzen = usun_wierzcholek(korzen, 55)
print("Przechodzenie drzewa Inorder po modyfikacji, po usunieciu wierzchołka 55")
inorder(korzen)

