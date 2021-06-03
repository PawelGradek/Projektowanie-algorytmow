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

# inorder - poprzeczne LVR
# preorder - wzdłużne VLR
# postorder - wsteczne

robot = Robot()
wektor1 = robot.opis_M_robotow(10)
print(wektor1)

a = int(input('Podaj parametr robota 2, 3, 4: '))
wektor_pomocniczy = []
for i in range(len(wektor1)):
    wektor_pomocniczy.append(wektor1[i][a])
print(wektor_pomocniczy)

#wektor_pomocniczy = [58, 3, 100, 15, 100, 4, 19, 86, 89, 60, 70]

class Wezel:
    def __init__(self, dane=None):
        self.dane = dane
        self.lewe_dziecko = None
        self.prawe_dziecko = None


class BST:
    def __init__(self):
        self.korzen = Wezel()

    def dodaj(self, dane):
        if self.korzen.dane == None:
            self.korzen.dane = int(dane)
        else:

            def dodaj_do_wierzcholka(dane, wierzcholek):
                if int(dane) < wierzcholek.dane:
                    if wierzcholek.lewe_dziecko == None:
                        wierzcholek.lewe_dziecko = Wezel(int(dane))
                    else:
                        dodaj_do_wierzcholka(int(dane), wierzcholek.lewe_dziecko)
                if int(dane) > wierzcholek.dane:
                    if wierzcholek.prawe_dziecko == None:
                        wierzcholek.prawe_dziecko = Wezel(int(dane))
                    else:
                        dodaj_do_wierzcholka(int(dane), wierzcholek.prawe_dziecko)

            dodaj_do_wierzcholka(int(dane), self.korzen)

    def wyswietl(self):
        wynik = ""

        def przechodzenie_preorder(wynik, wierzcholek):
            if wierzcholek:
                if wierzcholek.dane:
                    wynik += str(wierzcholek.dane) + " "
                    wynik = przechodzenie_preorder(wynik, wierzcholek.lewe_dziecko)
                    wynik = przechodzenie_preorder(wynik, wierzcholek.prawe_dziecko)
            return wynik

        def przechodzenie_inorder(wynik, wierzcholek):
            if wierzcholek:
                if wierzcholek.dane:
                    wynik = przechodzenie_inorder(wynik, wierzcholek.lewe_dziecko)
                    wynik += str(wierzcholek.dane) + " "
                    wynik = przechodzenie_inorder(wynik, wierzcholek.prawe_dziecko)
            return wynik

        def przechodzenie_postorder(wynik, wierzcholek):
            if wierzcholek:
                if wierzcholek.dane:
                    wynik = przechodzenie_postorder(wynik, wierzcholek.lewe_dziecko)
                    wynik = przechodzenie_postorder(wynik, wierzcholek.prawe_dziecko)
                    wynik += str(wierzcholek.dane) + " "
            return wynik

        def sciezka(wynik, wierzcholek, docelowy):
            if wierzcholek:
                if wierzcholek.dane:
                    wynik += str(wierzcholek.dane) + "->"
                    if wierzcholek.dane == docelowy:
                        return wynik
                    if wierzcholek.dane > docelowy:
                        wynik = 'L ' + sciezka(wynik, wierzcholek.lewe_dziecko, docelowy)
                    if wierzcholek.dane < docelowy:
                        wynik = 'R '+ sciezka(wynik, wierzcholek.prawe_dziecko, docelowy)
            return wynik


        def minimum(korzen):
            current = korzen
            while (current.lewe_dziecko):
                current = current.lewe_dziecko
            return current.dane

        def maximum(korzen):
            current = korzen
            while (current.prawe_dziecko):
                current = current.prawe_dziecko
            return current.dane

        def poprzednik_nastepnik(wektor, dane):
            def znajdz_poprz_nast(korzen, dane):

                if korzen is None:
                    return

                if korzen.dane == dane:

                    # the maximum value in lewe_dziecko subtree is predecessor
                    if korzen.lewe_dziecko is not None:
                        tmp = korzen.lewe_dziecko
                        while (tmp.prawe_dziecko):
                            tmp = tmp.prawe_dziecko
                        znajdz_poprz_nast.pre = tmp

                    # the minimum value in prawe_dziecko subtree is successor
                    if korzen.prawe_dziecko is not None:
                        tmp = korzen.prawe_dziecko
                        while (tmp.lewe_dziecko):
                            tmp = tmp.lewe_dziecko
                        znajdz_poprz_nast.suc = tmp
                    return

                if korzen.dane > dane:
                    znajdz_poprz_nast.suc = korzen
                    znajdz_poprz_nast(korzen.lewe_dziecko, dane)

                else:
                    znajdz_poprz_nast.pre = korzen
                    znajdz_poprz_nast(korzen.prawe_dziecko, dane)

            def insert(wierzcholek, dane):
                if wierzcholek is None:
                    return Wezel(dane)
                if dane < wierzcholek.dane:
                    wierzcholek.lewe_dziecko = insert(wierzcholek.lewe_dziecko, dane)
                else:
                    wierzcholek.prawe_dziecko = insert(wierzcholek.prawe_dziecko, dane)
                return wierzcholek


            korzen = None
            korzen = insert(korzen, 58)
            for i in wektor:
                insert(korzen, i)

            znajdz_poprz_nast.pre = None
            znajdz_poprz_nast.suc = None

            znajdz_poprz_nast(korzen, dane)

            if znajdz_poprz_nast.pre is not None:
                print(f"Poprzednik {dane} to: ", znajdz_poprz_nast.pre.dane)
            else:
                print("Nie ma poprzednika ")

            if znajdz_poprz_nast.suc is not None:
                print(f"Następnik {dane} to: ", znajdz_poprz_nast.suc.dane)
            else:
                print("Nie ma następnika")

        print('Przechodzenie preorder: ',przechodzenie_preorder(wynik, self.korzen))
        print('Przechodzenie inorder: ',przechodzenie_inorder(wynik, self.korzen))
        print('Przechodzenie postorder: ',przechodzenie_postorder(wynik, self.korzen))
        print(f'Sciezszka od korzenia do wierzchoła ',sciezka(wynik, self.korzen, 19))
        print('Minimalny element w drzewie to: ',minimum(self.korzen))
        print('Maksymalny element w drzewie to: ',maximum(self.korzen))
        print(poprzednik_nastepnik(wektor_pomocniczy[1:],48))

    def wyszukaj(self, element_szukany):
        self.fun_pom_wyszukaj(self.korzen, element_szukany)

    def fun_pom_wyszukaj(self, obecny_korzen, element_szukany):
        if obecny_korzen:
            if obecny_korzen.dane == element_szukany:
                print(True)
            elif obecny_korzen.dane < element_szukany:
                return self.fun_pom_wyszukaj(obecny_korzen.prawe_dziecko, element_szukany)
            else:
                return self.fun_pom_wyszukaj(obecny_korzen.lewe_dziecko, element_szukany)



drzewo = BST()
for i in wektor_pomocniczy:
    drzewo.dodaj(i)
print(f'Sprawdzenie czy w drzewie istnieje element 4: '), drzewo.wyszukaj(4)
drzewo.wyswietl()