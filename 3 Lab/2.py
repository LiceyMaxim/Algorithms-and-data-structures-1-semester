input_file = open("sort.in")
min_col = int(input_file.readline())
arr = list(map(int, input_file.readline().split()))


# Сделаем как в Кормене написано
def heap_sort(not_heap):

    build_max_heap(not_heap)
    for i in range(len(not_heap) - 1, 0, -1):
        not_heap[0], not_heap[i] = not_heap[i], not_heap[0]
        max_heapify(not_heap, index=0, size=i)


def parent(i):
    return (i - 1) // 2


def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


def build_max_heap(arr):
    length = len(arr)
    start = parent(length - 1)
    while start >= 0:
        max_heapify(arr, index=start, size=length)
        start = start - 1


def max_heapify(arr, index, size):
    l_child = left(index)
    r_child = right(index)
    largest = index
    if l_child < size and arr[l_child] > arr[index]:
        largest = l_child
    if r_child < size and arr[r_child] > arr[largest]:
        largest = r_child
    if largest != index:
        arr[largest], arr[index] = arr[index], arr[largest]
        max_heapify(arr, largest, size)


heap_sort(arr)
output_file = open("sort.out", 'w')
output_file.write(" ".join([str(x) for x in arr]))
