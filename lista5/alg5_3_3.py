import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib as mp
import alg5_0
import random
random.seed(157268)

robot = alg5_0.Robot()
d = int(input("Podaj ilosc elementow tablicy: "))
b = 3

wektor1 = robot.opis_M_robotow(d)

tablica_do_sortowania = []
for i in range(len(wektor1)):
    tablica_do_sortowania.append(wektor1[i][b])

a = tablica_do_sortowania



def sortowanie_przez_wstawianie(a):
    for j in range(1, len(a)):
        klucz = a[j]
        i = j - 1
        while (i >= 0 and a[i] > klucz):
            a[i + 1] = a[i]
            i -= 1
            yield a
        a[i + 1] = klucz
        yield a


def wyswietl_wykres(tablica_do_sortowania):
    a = tablica_do_sortowania

    generator = sortowanie_przez_wstawianie(a)
    nazwa_alg = 'Sortowanie przez wstawianie'

    plt.style.use('seaborn')
    fig, ax = plt.subplots()

    bar_rects = ax.bar(range(len(a)), a, align="edge",)#Zrób wykres słupkowy.

    ax.set_xlim(0, len(a))
    ax.set_ylim(0, int(100))
    ax.set_title("Algorytm : " + nazwa_alg )

    text = ax.text(0.01, 0.95, "", transform=ax.transAxes, color="#E4365D")#Dodaj tekst do osi.
    iteration = [0]

    def animate(A, rects, iteration):
        for rect, val in zip(rects, A):

            rect.set_height(val)
        iteration[0] += 1
        text.set_text("iterations : {}".format(iteration[0]))#ustaw tekst


    anim = FuncAnimation(fig, func=animate,
                         fargs=(bar_rects, iteration), frames=generator, interval=50,
                         repeat=False)
    plt.show()


wyswietl_wykres(tablica_do_sortowania)