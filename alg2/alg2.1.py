def licz_funkcje1(n):
    if n >= 0 :
        if type(n) == int:
            if n == 0:
                x = 0
            elif n > 0:
                x = 3 ** n + licz_funkcje1(n - 1)
        else:
            x = "Funkcja obsługuje liczby całkowite >= 0 "
    else:
        x = "Funkcja nie obsługuje liczb z zakresu < 0 "
    return x

def licz_funkcje2(n):
    if n  >= -1 :
        if type(n) == int:
            if n == -1 or n == 0:
                x = 0
            elif n > 0:
                x = n + licz_funkcje2(n - 2)
        else:
            x = "Funkcja obsługuje liczby całkowite >= 0 "
    else:
        x = "Funkcja nie obsługuje liczb z zakresu < 0 "
    return x


def licz_funkcje3(n):
    if n  >= 0 :
        if type(n) == int:
            if n == 0 :
                x = 0
            elif n == 1:
                x = 1
            elif n > 0:
                x = licz_funkcje3(n - 1) + licz_funkcje3(n - 2)
        else:
            x = "Funkcja obsługuje liczby całkowite >= 0 "
    else:
        x = "Funkcja nie obsługuje liczb z zakresu < 0 "
    return x

# od tego momentu definiuje funkcje analitycznie
def ind_licz_funkcje1(n):
    if n  >= 0 :
        if type(n) == int:
            if n == 0:
                x = 0
            elif n > 0:
                return sum([3**i for i in range(1, n + 1)])
        else:
            x = "Funkcja obsługuje liczby całkowite >= 0 "
    else:
        x = "Funkcja nie obsługuje liczb z zakresu < 0 "
    return x

def ind_licz_funkcje2(n):
    if n  >= -1 :
        if type(n) == int:
            if n == -1 or n == 0:
                x = 0
            elif n > 0:
                if n % 2 == 0:
                    x = n + (n / 2) * (n / 2 - 1)
                else:
                    x = n + ((n - 1) / 2) ** 2
        else:
            x = "Funkcja obsługuje liczby całkowite >= 0 "
    else:
        x = "Funkcja nie obsługuje liczb z zakresu < 0 "
    return int(x)


def ind_licz_funkcje3(n):
    if n  >= 0 :
        if type(n) == int:
            if n == 0 :
                x = 0
            elif n == 1:
                x = 1
            elif n > 0:
                x = int(round((((1+5**0.5)/2)**n/5**0.5)- (((1-5**0.5)/2)**n/5**0.5),2))
        else:
            x = "Funkcja obsługuje liczby całkowite >= 0 "
    else:
        x = "Funkcja nie obsługuje liczb z zakresu < 0 "
    return x

def procedura_weryfikujaca(n):
    for i in range(n):
        print(f"n ={i} dla 1 funkcji wynik numeryczny: {licz_funkcje1(i)} - wynik analityczny: {ind_licz_funkcje1(i)} ")
        print(f"n ={i} dla 2 funkcji wynik numeryczny: {licz_funkcje2(i)} - wynik analityczny: {ind_licz_funkcje2(i)} ")
        print(f"n = {i} dla 3 funkcji wynik numeryczny: {licz_funkcje3(i)} - wynik analityczny: {ind_licz_funkcje3(i)} ")
procedura_weryfikujaca(4)




