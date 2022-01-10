def cyclic_sort(nums):
    i = 0
    size = len(nums)
    while i < size:
        if nums[i] != i+1 and nums[i] != nums[nums[i] - 1]:
            swap = nums[i]
            nums[i] = nums[swap - 1]
            nums[swap - 1] = swap
        else:
            i += 1
    return nums
def find_all_missing(nums):
    arr = cyclic_sort(nums)
    size = len(arr)
    missing_nums = []
    for i in range(size):
        if nums[i] != i+1:
            missing_nums.append(i+1)
    if missing_nums == []:
        missing_nums.append(size)
        return missing_nums
    return missing_nums


print(find_all_missing([2, 3, 1, 8, 2, 3, 5, 1]))
print(find_all_missing([2, 4, 1, 2]))
print(find_all_missing([2, 3, 2, 1]))
