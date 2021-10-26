def descendants(ind, pir):
    global min_col
    if 2 * ind <= n:
        if pir[ind] >= pir[2 * ind]:
            return False
        else:
            return descendants(2 * ind, pir)
    elif 2 * ind + 1 <= n:
        if pir[ind] >= pir[2 * ind + 1]:
            return False
        else:
            return descendants(2 * ind + 1, pir)
    else:
        return True


input_file = open("isheap.in")
min_col = int(input_file.readline())
arr = list(map(int, input_file.readline().split()))
arr.insert(0, 0)
print(descendants(1, arr))
output_file = open("isheap.out", 'w')
if descendants(1, arr):
    output_file.write('YES')
else:
    output_file.write('NO')
