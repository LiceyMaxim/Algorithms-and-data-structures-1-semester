input_file = open("antiqs.in", "r")
n = int(input_file.readline())
m = [i for i in range(1, n+1)]
for i in range(n):
    m[i//2], m[i] = m[i], m[i//2]
output_file = open("antiqs.out", 'w')
output_file.write(' '.join(map(str, m)))
