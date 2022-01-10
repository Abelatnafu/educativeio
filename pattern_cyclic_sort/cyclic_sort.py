def cyclic_sort(nums):
    i = 0
    size = len(nums)
    while i < size:
        if nums[i] != i+1:
            swap = nums[i]
            nums[i] = nums[swap - 1]
            nums[swap - 1] = swap
        else:
            i += 1
    return nums

arr1 = [3, 1, 5, 4, 2]
arr2 = [2, 6, 4, 3, 1, 5]
arr3 = [1, 5, 6, 4, 3, 2]

print(cyclic_sort(arr1))
print(cyclic_sort(arr2))
print(cyclic_sort(arr3))