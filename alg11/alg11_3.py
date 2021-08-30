from collections import namedtuple
import matplotlib.pyplot as plt
import random

Point = namedtuple('Point', 'x y')


class Wypukla_otoczka(object):
    punkty = []
    punkty_na_otoczce = []

    def __init__(self):
        pass

    def dodaj(self, point):
        self.punkty.append(point)

    def znajdowanie_kierunku(self, origin, p1, p2):
        roznica = (((p2.x - origin.x) * (p1.y - origin.y)) - ((p1.x - origin.x) * (p2.y - origin.y)))

        return roznica

    def znajdowanie_otoczki(self):

        punkty1 = self.punkty

        start = punkty1[0]
        min_x = start.x
        for p in punkty1[1:]:
            if p.x < min_x:
                min_x = p.x
                start = p

        punkt1 = start
        self.punkty_na_otoczce.append(start)

        odlegly_punkt = None
        while odlegly_punkt is not start:

            p1 = None
            for p in punkty1:
                if p is punkt1:
                    continue
                else:
                    p1 = p
                    break

            odlegly_punkt = p1

            for p2 in punkty1:

                if p2 is punkt1 or p2 is p1:
                    continue
                else:
                    kierunek = self.znajdowanie_kierunku(punkt1, odlegly_punkt, p2)
                    if kierunek > 0:
                        odlegly_punkt = p2

            self.punkty_na_otoczce.append(odlegly_punkt)
            punkt1 = odlegly_punkt

    def pobierz_punkty_na_otoczce(self):
        if self.punkty and not self.punkty_na_otoczce:
            self.znajdowanie_otoczki()

        return self.punkty_na_otoczce

    def wisualization(self):
        # all points
        x = [p.x for p in self.punkty]
        y = [p.y for p in self.punkty]
        plt.plot(x, y, linestyle='None', marker='D')#

        hx = [p.x for p in self.punkty_na_otoczce]
        hy = [p.y for p in self.punkty_na_otoczce]
        plt.plot(hx, hy)
        plt.title('figura utworona z wypukłej otoczki')
        plt.show()


def main():
    figura = Wypukla_otoczka()
    for _ in range(20):
        figura.dodaj(Point(random.randint(-100, 100), random.randint(-100, 100)))

    print("Punkty należące do wypukłej otoczki:", figura.pobierz_punkty_na_otoczce())
    figura.wisualization()


if __name__ == '__main__':
    main()