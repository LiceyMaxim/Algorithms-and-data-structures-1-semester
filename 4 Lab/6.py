input_file = open('garland.in', 'r')
output_file = open('garland.out', 'w')
n, A = input_file.readline().split()
n = int(n)
A = float(A)

heights = [0] * (n + 1)
heights[0] = A
l = 0
r = heights[0]
last = 0
while r - l > 0.00001:
    heights[1] = (l + r) / 2
    flag = True
    for i in range(2, n):
        heights[i] = 2 * (heights[i - 1]) - heights[i - 2] + 2
        if heights[i] < 0:
            flag = False
            break
    if flag:
        r = heights[1]
        last = heights[i]
    else:
        l = heights[1]

print(round(last, 2), file=output_file)
