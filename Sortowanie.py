def bubble_sort(lista):
    n = len(lista)
    flag = True # ustawiamy flage na True

    while flag: #pętla wykonuje się w zależności jaką wartość przyjmuje flaga
        for i in range(0, n - 1):
            if lista[i] > lista[i + 1]: #sprawdzamy czy element jest mniejszy od następnego elementu
                lista[i], lista[i + 1] = lista[i + 1], lista[i] #zamieniamy elementy miejscami
        n = n - 1
        #print(lista) #możemy zobaczyć krok po kroku jak zmienia się nasza lista na poszczególnych etapach sortowania
        if n == 1:
            flag = False # ustawiamy flage na False
    return lista

#sortowanie_przez_wstawianie
def sort_by_insert(lista):
    n = len(lista)
    for i in range(1, n):
        klucz = lista[i] #aktualnie wybrany element
        j = i - 1 #przygotowujemy iteracje poprzez pozostale elementy
        while j >= 0 and lista[j] > klucz: #dopoki nie znajdziemy elementu mniejszego od wybranego i nie natrafimy na poczatek tablicy
            lista[j + 1] = lista[j] #zamieniamy elementy miejscami
            j = j - 1 #modyfikujemy zmienna iteracyjna
        lista[j + 1] = klucz #po znalezieniu mniejszego elementu, zamieniamy go z wybranym
    return lista

tab = [7, 3, -4, 12, 5]
print(bubble_sort(tab))
print(sort_by_insert(tab))




