print(set([10 ** 10, 10 ** 10]))
input_file = open("radixsort.in")
min_col, m, k = map(int, input_file.readline().split())
arr = []
for _ in range(min_col):
    arr.append(input_file.readline()[:-1])

for i in range(1, k + 1):
    arr.sort(key=lambda x: x[-i])

output_file = open("radixsort.out", 'w')
for i in range(min_col):
    output_file.write(arr[i] + '\n')
