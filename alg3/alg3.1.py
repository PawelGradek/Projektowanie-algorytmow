import math

#zad1.1
lista = []
def czp(p):
    a = int(math.floor(math.sqrt(p)))
    if p < 2:
        return lista
    lista.append(p)
    for i in range(2, a + 1):
        if p % i == 0:
            lista.pop()
            lista.append(i)
            czp(int(p/i))
            break
    return lista

p = 24
print(f'Liczba {p} posiada takie czynniki pierwsze: ', czp(p))

#zad 1.2 dobrze

def sera(p):
    lista = [0] * (p + 1)
    lista_koncowa = []
    b = int(math.floor(math.sqrt(p))) + 1
    for i in range(2, b):
        if lista[i] == 0:
            lista_koncowa.append(i)
            lista[i] = 1
            for j in range(i, len(lista)):
                c = i*j
                if c > p:
                    break
                lista[c] = 1
    for i in range(2, len(lista)):
        if lista[i] == 0:
            lista_koncowa.append(i)
    return lista_koncowa

p = 100
print(f'Liczby pierwsze z przedziału od 2 do {p} to: ', sera(p))





