# Given an array of sorted numbers, remove all duplicates from it. You should not use any extra space;
# after removing the duplicates in-place return the new length of the array.

_arr1 = [2, 3, 3, 3, 6, 9, 9]
_arr2 = [2, 2, 2, 11]

def remove_duplicates(arr):
    left, right = 0, 1

    while right < len(arr):
        if arr[left] == arr[right]:
            arr.pop(right)
        else:
            left += 1
            right += 1
    return len(arr)

print(remove_duplicates(_arr1))
print(remove_duplicates(_arr2))

# Similar question
# Problem 1: Given an unsorted array of numbers and a target ‘key’,
# remove all instances of ‘key’ in-place and return the new length of the array.

def remove_all_target(arr, target):