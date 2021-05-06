import alg5_0
import random
random.seed(157268)

robot = alg5_0.Robot()

a = int(input("Podaj ilosc elementow tablicy: "))
b = int(input("Podaj parametr wzgledem którego chcesz sortować masa - 2, zasieg - 3, rozdzielczosc - 4: "))
assert b == 2 or b == 3 or b == 4, 'podano zły parametr'
wektor1 = robot.opis_M_robotow(a)
print(wektor1)

tablica_do_sortowania = []
for i in range(len(wektor1)):
    tablica_do_sortowania.append(wektor1[i][b])
print(tablica_do_sortowania)

def sortowanie_szybkie(lista):
    elementy_mniejsze = []
    elementy_rowne = []
    elementy_wieksze = []

    if len(lista) > 1:
        element_dzielacy = lista[0]
        for x in lista:
            if x > element_dzielacy:
                elementy_wieksze.append(x)
            elif x == element_dzielacy:
                elementy_rowne.append(x)
            else:
                elementy_mniejsze.append(x)
        return sortowanie_szybkie(elementy_mniejsze) + elementy_rowne + sortowanie_szybkie(elementy_wieksze)
    else:
        return lista

tablica_po_sortowaniu = sortowanie_szybkie(tablica_do_sortowania)
print(tablica_po_sortowaniu)

wektor1_posortowany = []
tabu = []
for i in tablica_po_sortowaniu:
    for j in range(len(wektor1)):
        if i == wektor1[j][b] and wektor1[j] not in tabu:
            wektor1_posortowany.append(wektor1[j])
            tabu.append(wektor1[j])

print('\n',wektor1_posortowany)

