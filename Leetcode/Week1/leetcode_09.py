def isPalindrome(x):
    """
    :type x: int
    :rtype: bool  #判断数字是否为回文数字，只需要对数字进行翻转即可 python里面有倒叙索引
    """
    flag = 1 if x >= 0 and abs(x) < 2 ** 31 - 1 else 0
    if flag == 1:
        number = int(str(x)[::-1])
        if number == x:
            return True
        else:
            return False
    else:
        return False


x=-32432532
print(isPalindrome(x))