def longest_common_prefix(s):
    prefix = ""
    char = s[0][0]

    for i in range(len(min(s, key=len))): #(0,4) 0 1 2 3
        for j in range(len(s)):           #(0,3) 0 1 2
            if char != s[j][i]: 
                break

            
            prefix+=char
            char = s[i][i+1]

    return prefix




s = ["flower", "flow", "flight"]
    #s[0][0] , s[1][0]   s[2][0]  s[j][i]
print(longest_common_prefix(s))