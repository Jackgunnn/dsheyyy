# dict method

def is_anagram(s, t):

    if len(s) != len(t):
        return False

    char_freq = {}

    for i in s:
        if i not in char_freq:
            char_freq[i] = 1
        else:
            char_freq[i] += 1

    for j in t:
        if j not in char_freq:
            return False
        else:
            char_freq[j] -= 1


    for k in char_freq.values():
        if k != 0:
            return False

    return True



print(is_anagram("rat", "car"))   # False
print(is_anagram("", ""))         # True
print(is_anagram("aab", "aba"))   # True
