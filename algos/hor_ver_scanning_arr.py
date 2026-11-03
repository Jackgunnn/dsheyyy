s = [
    "flower",
    "flow",
    "flight"
]

#HORIZONTAL SCANNING 
print("HORIZONTAL SCANNING")

for i in range(len(s)):
    for j in range(len(s[i])):
        print(s[i][j])

#VERTICAL SCANNING
print("VERTICAL SCANNING")

short_word = min(s, key=len)

for i in range(len(short_word)):
    for j in range(len(s)):
        print(s[j][i])