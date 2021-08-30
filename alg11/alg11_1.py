import matplotlib.pyplot as plt
import numpy as np

# wektory ze wspolrzednymi
X11 = [[-10], [-2], [10], [10]]
X22 = [[-8], [2], [-2], [4]]
X33 = [[-5], [9], [8], [2]]
X44 = [[1], [9], [10], [7]]
X = [
        [[-10],[-2],[10],[10]],
        [[-8],[2],[-2],[4]],
        [[-5], [9], [8], [2]],
        [[1], [9], [10], [7]]
]
X1 = [[-10], [-2], [-1*X11[0][0]+10], [-1*X11[1][0]+10]]
X2 = [[-8], [2], [-1*X22[0][0]+(-2)], [-1*X22[1][0]+4]]
X3 = [[-5], [9], [-1*X33[0][0]+8], [-1*X33[1][0]+2]]
X4 = [[1], [9], [-1*X44[0][0]+10], [-1*X44[1][0]+7]]
fig, ax = plt.subplots()

plt.quiver(X1[0], X1[1], X1[2], X1[3], units='xy', scale=1)
plt.quiver(X2[0], X2[1], X2[2], X2[3], units='xy', scale=1)
plt.quiver(X3[0], X3[1], X3[2], X3[3], units='xy', scale=1)
plt.quiver(X4[0], X4[1], X4[2], X4[3], units='xy', scale=1)

plt.grid()

ax.set_aspect('equal')

def line_intersect(Ax1, Ay1, Ax2, Ay2, Bx1, By1, Bx2, By2):
    d = (By2 - By1) * (Ax2 - Ax1) - (Bx2 - Bx1) * (Ay2 - Ay1)
    if d:
        uA = ((Bx2 - Bx1) * (Ay1 - By1) - (By2 - By1) * (Ax1 - Bx1)) / d
        uB = ((Ax2 - Ax1) * (Ay1 - By1) - (Ay2 - Ay1) * (Ax1 - Bx1)) / d
    else:
        return
    if not (0 <= uA <= 1 and 0 <= uB <= 1):
        return
    x = round((Ax1 + uA * (Ax2 - Ax1)), 3)
    y = round((Ay1 + uA * (Ay2 - Ay1)), 3)

    return[x, y]


lista_punktow_przeciecia = []

for i in range(0,len(X)):
    for j in range(0, len(X)):
        if i == j:
            continue
        a = line_intersect(X[i][0][0], X[i][1][0],X[i][2][0], X[i][3][0], X[j][0][0], X[j][1][0],X[j][2][0], X[j][3][0])
        lista_punktow_przeciecia.append(a)
print('lista punktów przecięcia',lista_punktow_przeciecia)


czysta_lista = []
for i in range(len(lista_punktow_przeciecia)):
    if lista_punktow_przeciecia[i] != None and lista_punktow_przeciecia[i] not in czysta_lista:
        czysta_lista.append(lista_punktow_przeciecia[i])
print('czysta lista',czysta_lista)

x = []
y = []

for i in czysta_lista:
    x.append(i[0])
    y.append(i[1])

plt.plot(x, y,'*', color='r')

for i in range(len(czysta_lista)):
    for j in range(len(X)):
        if czysta_lista[i][0] > X[j][2][0]: # zależy ja definiujemy prawą stronę wektora czy środek wektora się wlicza? jeśli tak to powinno być czysta_lista[i][0] > X[j][0][0]
            print(f'punkt {czysta_lista[i]}, jest po prawej stronie wektorów o wpółrzędnych: {X[j]}')

plt.xlim(-12,12)
plt.ylim(-12,12)

plt.title('Przecięcie wektorów',fontsize=10)


plt.show()


