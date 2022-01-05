# Given an array of characters where each character represents a fruit tree,
# you are given two baskets and your goal is to put maximum number of fruits in each basket.
# The only restriction is that each basket can have only one type of fruit.
# You can start with any tree, but once you have started you can’t skip a tree.
# You will pick one fruit from each tree until you cannot, i.e., you will stop when you have to pick from a third fruit type.
# Write a function to return the maximum number of fruits in both the baskets.
_fruit= ['A', 'B', 'C', 'A', 'C']
_fruit2 = ['A', 'B', 'C', 'B', 'B', 'C']

def fruits_into_baskets(fruits):
    start = 0
    max_fruits = 0
    freq = {}
    size = len(fruits)
    for end in range(size):
        if fruits[end] not in freq.keys():
            freq[fruits[end]] = 0
        freq[fruits[end]] += 1

        while len(freq) > 2:
            freq[fruits[start]] -= 1
            if freq[fruits[start]] == 0:
                del freq[fruits[start]]
            start += 1
        max_fruits = max(max_fruits, end - start + 1)
    return max_fruits

print(fruits_into_baskets(_fruit))
print(fruits_into_baskets(_fruit2))