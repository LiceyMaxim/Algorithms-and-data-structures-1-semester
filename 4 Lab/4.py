def push(item):
    global length
    length += 1
    stack[length] = item


def delete():
    global length
    number = stack[length]
    length -= 1
    return number


input_file = open('postfix.in', 'r')
output_file = open('postfix.out', 'w')

stack = [0 for i in range(1000001)]
length = -1
record = input_file.readline().split()
for symbol in record:
    if symbol == '+':
        num_2 = delete()
        num_1 = delete()
        push(num_1 + num_2)
    elif symbol == '-':
        num_2 = delete()
        num_1 = delete()
        push(num_1 - num_2)
    elif symbol == '*':
        num_2 = delete()
        num_1 = delete()
        push(num_1 * num_2)
    else:
        push(int(symbol))

print(delete(), file=output_file)
