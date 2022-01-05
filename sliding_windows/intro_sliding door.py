# Given an array, find the average of all contiguous subarrays of size ‘K’ in it.
# Array: [1, 3, 2, 6, -1, 4, 1, 8, 2], K=5

Array= [1, 3, 2, 6, -1, 4, 1, 8, 2]
K=5

def average_subarray(_array, k):
    sum = 0             #the sum for the k amounts in the subarray
    start = 0           #the starting point
    end = start + k     #end of the the subarray
    avg_array = []      #the array of averages that are being returned at the end

    # Loop to get the first  k sum
    for i in range (start, end):
        sum += _array[i]
    avg_array.append(sum/k)

    # slide 1 to the left by the subtracting the one before and adding the one after
    start += 1
    size = len(_array)

    for i in range (start ,size):
        if start + k <= size:
            sum -= _array[start - 1]
            sum += _array[start + k - 1]
            avg_array.append(sum / k)
            start += 1
    return avg_array


def avg_subarray(_array, k):
    sum = 0             #the sum for the k amounts in the subarray
    start = 0           #the starting point
    end = len(_array)     #end of the the subarray
    avg_array = []      #the array of averages that are being returned at the end


    for i in range (start, end):
        sum += _array[i]

        if (i >= k-1):
            avg_array.append(sum / k)
            sum-= _array[start]
            start += 1
    return avg_array



answer = avg_subarray(Array, K)
print(answer)

#SOLVED
