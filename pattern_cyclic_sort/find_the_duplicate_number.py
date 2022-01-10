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

def find_duplicate(nums):
    arr = cyclic_sort(nums)
    size = len(arr)
    duplicates= []
    for i in range(size):
        if arr[i] != i+1 and arr[i] <= size and arr[i] not in duplicates:
            duplicates.append(arr[i])
    return duplicates

# print(find_duplicate([1, 4, 4, 3, 2]))
# print(find_duplicate([2, 1, 3, 3, 5, 4]))
# print(find_duplicate([2, 4, 1, 4, 4]))

def cyclic_sort_and_duplicates(nums):
    i = 0
    size = len(nums)
    duplicates = []
    while i < size:
        if nums[i] != i+1 and nums[i] != nums[nums[i] - 1]:
            swap = nums[i]
            nums[i] = nums[swap - 1]
            nums[swap - 1] = swap

        else:
            i += 1
            conditions1 = nums[i - 1] != i and nums[i - 1] == nums[nums[i - 1] - 1] and nums[i - 1] not in duplicates
            if conditions1:
                duplicates.append(nums[i - 1])


    return duplicates

print(cyclic_sort_and_duplicates([1, 4, 4, 3, 2]))
print(cyclic_sort_and_duplicates([2, 1, 3, 3, 5, 4]))
print(cyclic_sort_and_duplicates([2,1]))

