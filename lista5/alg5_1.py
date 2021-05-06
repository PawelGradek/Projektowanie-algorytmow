from random import randint

def generate_vector(n = 10): #funckja losująca wektor o długości n
    x = [str(randint(1, 10000)) for i in range(n)]
    return x

def get_num_from_vector(vec, n): #funckja wybiera z danego wektora liczby z ilością cyfr >= n
    res = []
    for v in vec:
        if len(v) >= n:
            res.append(v)
    if res:
        return res
    else:
        return False


def sort_vector(vector, pos, rev, num=10): #sortowanie wektora według kolejnych cyfr

    res = get_num_from_vector(vector, pos)
    if res:
        sorted_res = sorted(res, key = lambda r: r[(pos-1):], reverse=rev)
        print(f'\nWektor posortowany według {pos} cyfry: \n{sorted_res}')
        return sorted_res
    else:
        print(f'\nW wektorze nie ma liczb składających sie z {pos} cyfr')


def main():
    vector = generate_vector()
    print(f'Wektor wejściowy: \n{vector}')
    rev = False
    for i in range(1,5):
        sort_vector(vector, i, rev)
        if rev:
            rev = False
        else:
            rev = True

main()
