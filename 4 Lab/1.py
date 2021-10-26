def push(item):
    values.append(item)


def delete():
    if values:
        return values.pop()
    return None


values = []
input_file = open('stack.in', 'r')
output_file = open('stack.out', 'w')
n = int(input_file.readline())
for _ in range(n):
    commands = input_file.readline().split()
    if commands[0] == '+':
        push(commands[1])
    else:
        print(delete(), file=output_file)
output_file.close()
