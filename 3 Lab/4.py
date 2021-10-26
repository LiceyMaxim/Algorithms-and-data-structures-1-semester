def pushUp(i):
    if i != 0:
        if heap[(i - 1) // 2][0] > heap[i][0]:
            heap[(i - 1) // 2], heap[i] = heap[i], heap[(i - 1) // 2]
            pushUp((i - 1) // 2)


def pushDown(i):
    global min_col
    left = 2 * i + 1
    right = 2 * i + 2
    if right < min_col and heap[right][0] < heap[i][0]:
        j = right
    else:
        j = i
    if left < min_col and heap[left][0] < heap[j][0]:
        j = left
    if i != j:
        heap[i], heap[j] = heap[j], heap[i]
        pushDown(j)


def heap_push(elem, i):
    global min_col
    heap[min_col][0] = elem
    heap[min_col][1] = i
    min_col += 1
    pushUp(min_col - 1)


def extractMin():
    global min_col
    ans = heap[0][0]
    min_col -= 1
    heap[0], heap[min_col] = heap[min_col], heap[0]
    pushDown(0)
    return ans


def decrease(x, y):
    for i in range(min_col):
        if heap[i][1] == x:
            break
    heap[i][0] = y
    pushUp(i)


min_col = 0
heap = [[0 for i in range(2)] for j in range(100000)]
input_file = open('priorityqueue.in', 'r')
command = input_file.readline().split()
output_file = open('priorityqueue.out', 'w')
count = 1
while command:
    if command[0] == 'push':
        heap_push(int(command[1]), count)
    elif command[0] == 'extract-min':
        if min_col == 0:
            print('*', file=output_file)
        else:
            print(extractMin(), file=output_file)
    elif command[0] == 'decrease-key':
        decrease(int(command[1]), int(command[2]))
    command = input_file.readline().split()
    count += 1
