# Начало функций для  сортировки
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


def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    m = len(nums) // 2
    left = merge_sort(nums[:m])
    right = merge_sort(nums[m:])
    return merge(left, right)
# Конец функций для  сортировки


input_file = open("race.in.", "r")
results = []

n = int(input_file.readline())
for i in range(n):
    items = input_file.readline().split()
    results.append([items[0], i, items[1]])

results = merge_sort(results)
t = ''
output_file = open("race.out", 'w')

for items in results:
    if items[0] != t:
        output_file.write('=== ' + items[0] + ' ===\n')
    output_file.write(items[2] + '\n')
    t = items[0]
