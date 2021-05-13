import matplotlib.pyplot as plt
from celluloid import Camera

fig = plt.figure()
camera = Camera(fig)
comparisons = 0

title = 'Algorytm sortowania przez kopcowanie'
graph = plt.bar


def Plot(highlight, data):
    x = list(range(len(data)))
    global comparisons
    comparisons += 1
    if graph == plt.bar:
        colors = list(len(data) * 'b')
        #colors[highlight] = 'r'
        graph(x, data, color=colors)

    plt.title(title)
    plt.xlabel('Rozmiar danych:{}, Ilość porównań:{}'.format(len(data), comparisons))
    camera.snap()

def heapify(unsorted, index, heap_size):
    largest = index
    left_index = 2 * index + 1
    right_index = 2 * index + 2
    if left_index < heap_size and unsorted[left_index] > unsorted[largest]:
        largest = left_index

    if right_index < heap_size and unsorted[right_index] > unsorted[largest]:
        largest = right_index

    if largest != index:
        unsorted[largest], unsorted[index] = unsorted[index], unsorted[largest]
        heapify(unsorted, largest, heap_size)
        Plot(largest, unsorted)

def heapSort(unsorted):

    n = len(unsorted)
    for i in range(n // 2 - 1, -1, -1):
        heapify(unsorted, i, n)
    for i in range(n - 1, 0, -1):
        unsorted[0], unsorted[i] = unsorted[i], unsorted[0]
        heapify(unsorted, 0, i)
    return unsorted


import random
random.seed(157268)

data = []
for i in range(0, 20):
    data.append(random.randint(0, 100))
print(data)

func = heapSort
func(data)

interval_time = 200
animation = camera.animate(interval=interval_time)
plt.show()
