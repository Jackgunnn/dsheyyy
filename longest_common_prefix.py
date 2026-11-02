#CONCEPT: Vertical Scanning
#USECASE: Useful when comparing multiple strings, filenames, identifiers, or common prefixes in data

def longest_common_prefix(s):
    if not s:
        return ""
    
    prefix = ""
    shortest_word = min(s, key=len)

    for i in range(len(shortest_word)): #(0,4) 0 1 2 3
        char = shortest_word[i]
        for j in range(len(s)):           #(0,3) 0 1 2
            if char != s[j][i]: 
                return prefix

        prefix+=char
            

    return prefix




print(longest_common_prefix(["flower", "flow", "flight"]))
# "fl"

print(longest_common_prefix(["dog", "racecar", "car"]))
# ""

print(longest_common_prefix(["interview", "internet", "internal"]))
# "inter"

print(longest_common_prefix(["alone"]))
# "alone"

print(longest_common_prefix([]))
# ""