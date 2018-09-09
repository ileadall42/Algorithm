def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    stack = []
    dict = {"]": "[", "}": "{", ")": "("}  #利用了字典一对一的索引关系及列表的pop
    for char in s:
        if char in dict.values():
            stack.append(char)
        elif char in dict.keys():
            if stack == [] or dict[char] != stack.pop():
                return False
        else:
            return False
    return stack == []

def isValid2(s):
    """
    :type s: str
    :rtype: bool
    """
    stack = ['N']
    m = {')': '(', ']': '[', '}': '{'}
    for i in s:
        if i in m.keys():
            if stack.pop() != m[i]:
                return False
        else:
            stack.append(i)

    return len(stack) == 1


s='(dfsdfs)'
print(isValid(s))