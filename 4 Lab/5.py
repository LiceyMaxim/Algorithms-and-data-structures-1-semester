def bin_search(left, right, purpose):
    while left < right:
        mid = (left + right) // 2
        if arr[mid] > purpose:
            right = mid
        elif arr[mid] == purpose:
            right = mid
        else:
            left = mid + 1
    return left


input_file = open('binsearch.in', 'r')
output_file = open('binsearch.out', 'w')
n = int(input_file.readline())
arr = [int(x) for x in input_file.readline().split()]
m = int(input_file.readline())
requests = [int(x) for x in input_file.readline().split()]

for request in requests:
    t_1 = bin_search(0, n, request)
    t_2 = bin_search(0, n, request + 1)

    if t_1 >= n:
        print('-1 -1', file=output_file)
    elif arr[t_1] != request:
        print('-1 -1', file=output_file)
    else:
        print(t_1 + 1, t_2, file=output_file)
