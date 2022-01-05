# Given a string, find the length of the longest substring in it with no more than K distinct characters.
string = "cbbebi"
k = 3


def longest_subst_with_KCharcter (_string, _k):
    start = 0
    freq = {}
    maxLength= 0
    size = len(_string)
    for end in range(size):
        right_char = _string[end]
        if right_char not in freq.keys():
            freq[right_char] = 0
        freq[right_char] += 1

        while len(freq) > _k:
            left_char = _string[start]
            freq[left_char] -= 1
            if freq[left_char] == 0:
                del freq[left_char]
            start += 1
        maxLength = max(maxLength, end - start + 1 )
    return maxLength


answer = longest_subst_with_KCharcter(string, k)
print(answer)