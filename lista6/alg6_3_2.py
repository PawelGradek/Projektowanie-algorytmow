import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib as mp

import random
random.seed(157268)

wektor= []
for i in range(0,21):
    wektor.append(random.randint(0,100))
print(wektor)


def sortowanie_szybkie(a, l, r):#tablica, piwot,  długość tablicy - 1
    if l >= r:
        return
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[j], a[i] = a[i], a[j]
        yield a
    a[l], a[j] = a[j], a[l]
    yield a # zwraca generator, operacje, do wywoływania funkci animation


    yield from sortowanie_szybkie(a, l, j - 1)
    yield from sortowanie_szybkie(a, j + 1, r)




def wyswietl_wykres(tablica_do_sortowania):
    n = len(tablica_do_sortowania)
    a = tablica_do_sortowania

    generator = sortowanie_szybkie(a, 0, n - 1)
    nazwa_alg = 'Sortowanie szybkie'

    plt.style.use('seaborn')
    fig, ax = plt.subplots(figsize=(6,5))
    colors = list(len(wektor) * 'b')
    #colors[highlight] = 'r'
    bar_rects = ax.bar(range(len(a)), a, align="edge",color=colors)  # Zrób wykres słupkowy.

    ax.set_xlim(0, len(a))
    ax.set_ylim(0, int(100))
    ax.set_title("Algorytm : " + nazwa_alg )  # wstaw tytuł wykresu

    text = ax.text(0.01, 0.95, "", transform=ax.transAxes, color="#E4365D") # Dodaj tekst do osi.
    iteration = [0]

    def animate(A, rects, iteration):
        for rect, val in zip(rects, A):  # zwraca krotke z elementami z rects i A

            rect.set_height(val)  # ustaw szerokosc
        iteration[0] += 1
        text.set_text("iterations : {}".format(iteration[0]))  # ustaw tekst


    anim = FuncAnimation(fig, func=animate,
                         fargs=(bar_rects, iteration), frames=generator, interval=50,
                         repeat=False)
    plt.show()


wyswietl_wykres(wektor)