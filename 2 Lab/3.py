input_file = open("inversions.in")
n = int(input_file.readline())
a = list(map(int, input_file.readline().split()))

count = 0


def merge(left, right):
    s = []
    global count
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
                count += l_len - l_i
        elif l_i == l_len:
            s.append(right[r_i])
            r_i += 1
        elif r_i == r_len:
            s.append(left[l_i])
            l_i += 1
    return s


def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    m = len(nums) // 2
    left = merge_sort(nums[:m])
    right = merge_sort(nums[m:])
    return merge(left, right)


merge_sort(a)
output_file = open('inversions.out', 'w')
output_file.write(str(count))
