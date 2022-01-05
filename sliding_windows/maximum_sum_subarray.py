# Given an array of positive numbers and a positive number ‘k’,
# find the maximum sum of any contiguous subarray of size ‘k’.

Array = [2, 1, 5, 1, 3, 2]
Array2 = [2, 3, 4, 1, 5]
p=2
K = 3

def max_sum_sub(_array, k):
    start = 0
    highest_sum = 0
    sum = 0
    size = len(_array)

    for i in range(size):
        sum += _array[i]

        if (i >= k -1):
            if highest_sum < sum:
                highest_sum = sum
            sum -= _array[start]
            start += 1
    return highest_sum

answer = max_sum_sub(Array2, p)
print(answer)

# SOLVED
