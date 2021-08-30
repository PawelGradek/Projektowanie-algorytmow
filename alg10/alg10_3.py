

def szukaj_slowa(ciag, zbior):
    n = len(ciag)

    tablica = [False] * (n + 1) # [False, False, False]
    tablica[0] = True # [True, False, False]

    for i in range(1, n + 1):
        for j in range(i):
            if tablica[j] and ciag[j:i] in zbior:

                print(ciag[j:i])
                tablica[i] = True

    return tablica[-1]


s = "domkotmały"
wordDict = ["dom", "pies", "kot", "mały", "samochód"]
szukaj_slowa(s, wordDict)