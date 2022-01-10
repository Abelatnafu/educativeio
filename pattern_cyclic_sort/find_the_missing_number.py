def cyclic_sort(nums):
    i = 0
    size = len(nums)
    while i < size:
        if nums[i] != i and nums[i] < size:
            swap = nums[i]
            nums[i] = nums[swap]
            nums[swap] = swap
        else:
            i += 1
    return nums

def find_missing_number(nums):
    arr = cyclic_sort(nums)
    size = len(arr)
    for i in range(size):
        if i != arr[i]:
            return i
    return size

arr1 = [4, 0, 3, 1]
arr2 = [8, 3, 5, 2, 4, 6, 0, 1]
print(find_missing_number(arr1))
print(find_missing_number(arr2))