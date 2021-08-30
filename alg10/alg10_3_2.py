def szukaj_slow(ciag, zbior):
    lista_slow_w_ciagu = []
    n = len(ciag)  # długość ciągu znaków
    if n == 0:
        print('ciąg jest pusty')

    for i in range(1, n + 1):
        prefix = ciag[:i]

        if prefix in zbior:
            lista_slow_w_ciagu.append(prefix)
        for j in range(1,i):
            prefix2 = ciag[j:i]
            if prefix2 in zbior:
                lista_slow_w_ciagu.append(prefix2)
    print(lista_slow_w_ciagu)


if __name__ == '__main__':
    lista_slow_w_ciagu = []
    zbior = ["dom", "kot", "pies", "świat","mały",  "samochód"]
    ciag = "domałyfgtkotserwtypies"
    szukaj_slow(ciag, zbior)
