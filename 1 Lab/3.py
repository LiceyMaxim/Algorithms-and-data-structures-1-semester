input_file = open('turtle.in')
n, m = map(int, input_file.readline().split())
joy = []

for i in range(n):
    joy.append(list(map(int, input_file.readline().split())))
for i in range(1, m):
    joy[n-1][i] += joy[n-1][i-1]
for i in range(n-2, -1, -1):
    joy[i][0] += joy[i+1][0]
for i in range(n-2, -1, -1):
    for j in range(1, m):
        joy[i][j] += max(joy[i+1][j], joy[i][j-1])

output_file = open('turtle.out', 'w')
output_file.write(str(joy[0][m - 1]))
