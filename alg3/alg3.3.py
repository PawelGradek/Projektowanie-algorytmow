import random

#zad3
#Test fermata
def test_fermata(p, k):#p - badana liczba, k - ilość testow
    # Jeśli liczba jest parzysta, jest to liczba złożona
    if p == 2:
        return True
    if p % 2 == 0:
        return False
    for i in range(k):
        q = random.randint(1, p - 1)
        if pow(q, p - 1) % p != 1:
            return False
    return True
a = 31
b = 8
print(f'Wynik testu Fermata   powtorzony {b} razy czy liczb {a} jest pierwsza : ', test_fermata(a, b))

#Test Miller Rabina
def test_miller_rabin(p, k):
    # Jeśli liczba jest parzysta, jest to liczba złożona
    if p == 2 or p == 3:
        return True
    if p % 2 == 0:
        return False
    r, q = 0, p - 1
    while q % 2 == 0:
        r += 1
        q //= 2
    for i in range(k):
        a = random.randrange(2, p - 1)
        x = a ** q % p
        if x == 1 or x == p - 1:
            continue
        for i in range(r - 1):
            x = pow(x, 2, p)# t do potęgi 2 moduł p = t^2 % p
            if x == p - 1:
                break
        else:
            return False
        break
    return True


print(f'Wynik testu Miller Rabina powtorzony {b} razy czy liczba {a} jest pierwsza: ',test_miller_rabin(a, b))
