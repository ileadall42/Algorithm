def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    #罗马数字的特点就是大字母在前就是正的 大数字字母在后就是前面少了。
    roman = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    z = 0
    for i in range(0, len(s) - 1):
        if roman[s[i]] < roman[s[i + 1]]:
            z -= roman[s[i]]
        else:
            z += roman[s[i]]
    return z + roman[s[-1]]


s='MDDCLXI'
print(romanToInt(s))