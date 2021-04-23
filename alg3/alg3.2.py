import math
import time
import matplotlib.pyplot as plt
import numpy as np

#zad2.1
def czp(p):
    a = int(math.floor(math.sqrt(p)))
    if p < 2:
        return lista
    lista.append(p)
    for i in range(2, a + 1):
        if p % i == 0:
            lista.pop()
            lista.append(i)
            czp(int(p / i))
            break
    return lista

def fun_globalna(p):
    global lista
    lista = []
    czp(p)
    return lista


def aczp(a, b):
    lista1 = fun_globalna(a)
    lista2 = fun_globalna(b)
    dlugosc1 = len(lista1)
    dlugosc2 = len(lista2)
    wspolna_lista = []
    for i in range(0, dlugosc1):
        for j in range(0, dlugosc2):
            if lista1[i] == lista2[j]:
                wspolna_lista.append(lista2[j])
                lista2.remove(lista2[j]) # usuwa pierwszy pasujący element (przekazany jako argument) z listy
                dlugosc2 -= 1
                break
    if not wspolna_lista:
        print("Podane liczby nie mają wspólnych dzielników")
    wynik = 1
    for i in range(0, len(wspolna_lista)):
        wynik = wynik * wspolna_lista[i]
    return wynik

a = 6
b = 30

print(f'aczp : Największy wspolny dzielnik {a} i {b} to: ', aczp(a, b))

#zad 2.2
def aeuc(x,y):
    if y == 0:
        return x
    else:
        return aeuc(y, x % y)

print(f'aeuc : Największy wspolny dzielnik {a} i {b} to: ',aeuc(a,b))

