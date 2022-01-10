# Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target.
# Write a function to return the indices of the two numbers (i.e. the pair) such that they add up to the given target.
_arr1 = [1, 2, 3, 4, 6]
_arr2 = [3, 3]
_target1 = 6
_target2 = 6


def twoSum( nums, target) :
    left = 0
    right = len(nums) - 1
    arr = []
    for i in nums:
        arr.append(i)
    nums.sort()
    # print(nums)
    # print(arr)

    while left < right:
        if nums[left] + nums[right] < target:
            left += 1
        elif nums[left] + nums[right] > target:
            right -= 1
        else:
            if arr.index(nums[left]) == arr.index(nums[right]):
                first = arr.index(nums[left])
                arr.pop(first)
                return [first, arr.index(nums[right])+1]
            return [arr.index(nums[left]), arr.index(nums[right])]

print(twoSum(_arr1, _target1))
print(twoSum(_arr2, _target2))
