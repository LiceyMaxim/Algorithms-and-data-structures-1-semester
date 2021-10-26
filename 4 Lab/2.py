def delete():
    global iterator
    iterator += 1
    return values[iterator - 1]


def push(curr):
    values.append(curr)


values = []
iterator = 0

input_file = open('queue.in', 'r')
output_file = open('queue.out', 'w')

n = int(input_file.readline())

for _ in range(n):
    a = input_file.readline().split()
    if a[0] == '+':
        push(a[1])
    else:
        print(delete(), file=output_file)
