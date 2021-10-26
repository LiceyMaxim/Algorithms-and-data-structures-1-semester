input_file = open("smallsort.in")
n = int(input_file.readline())
a = list(map(int, input_file.readline().split()))


def merge(left, right):
    s = []
    l_i = r_i = 0
    l_len = len(left)
    r_len = len(right)
    for _ in range(l_len + r_len):
        if l_i < l_len and r_i < r_len:
            if left[l_i] <= right[r_i]:
                s.append(left[l_i])
                l_i += 1
            else:
                s.append(right[r_i])
                r_i += 1
        elif l_i == l_len:
            s.append(right[r_i])
            r_i += 1
        elif r_i == r_len:
            s.append(left[l_i])
            l_i += 1
    return s


def merge_sort(numbers):
    if len(numbers) <= 1:
        return numbers
    mid = len(numbers) // 2
    l = merge_sort(numbers[:mid])
    r = merge_sort(numbers[mid:])
    return merge(l, r)


output_file = open('smallsort.out', 'w')
output_file.write(" ".join(map(str, merge_sort(a))))
