# Given an array of positive numbers and a positive number ‘S’,
# find the length of the smallest contiguous subarray whose sum is greater than or equal to ‘S’.
# Return 0, if no such subarray exists.

array = [3, 4,1, 1, 6]
s= 8


def small_subarray(_array, S):
    size = len(_array)
    start = 0
    amount = 0
    least_amount=0
    sum = 0
    for i in range(size):
        sum+= array[i]
        amount += 1
        while sum >= S:
            sum -= array[start]
            if least_amount == 0 or amount < least_amount:
                least_amount = amount
            amount -= 1
            start += 1
    return least_amount



answer = small_subarray(array, s)
print(answer)

 # SOLVED