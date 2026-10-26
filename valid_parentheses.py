def valid_parentheses(s): #stack problem

    hashMap = {
        '[' : ']',
        '{' : '}',
        '(' : ')'
    }

    stack = []


    for i in s:
        if i in ['{', '[', '(']:
            stack.append(i)
        else:
            if not stack:
                return False

            j = stack.pop()

            if i != hashMap[j]:
                return False

    return len(stack) == 0 # returns True if stack has no parentheses or False

print(valid_parentheses("{[}]}"))