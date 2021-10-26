def bubble_sort(nums):
    flag = True
    while flag:
        flag = False
        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                flag = True
    return nums


input_file = open('sortland.in')
n = int(input_file.readline())
numbers = list(map(float, input_file.readline().split()))
list_sort = bubble_sort(numbers.copy())

output_file = open('sortland.out', 'w')
output_file.write(str(numbers.index(list_sort[0]) + 1) + " ")
output_file.write(str(numbers.index(list_sort[n // 2]) + 1) + " ")
output_file.write(str(numbers.index(list_sort[-1]) + 1))
