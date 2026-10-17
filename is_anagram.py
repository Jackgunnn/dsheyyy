#sorting method

def is_anagram(s, t):

    if len(s) != len(t):
        return False

    ss = sorted(s)
    tt = sorted(t)

    return ss == tt




print(is_anagram("rat", "car"))   # False
print(is_anagram("", ""))         # True
print(is_anagram("aab", "aba"))   # True
