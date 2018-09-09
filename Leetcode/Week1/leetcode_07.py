# -*- coding: utf-8 -*-
# @Author: Mr.Jhonson
# @Date:   2017-08-22 23:29:23
# @Last Modified by:   Mr.Jhonson
# @Last Modified time: 2017-08-23 09:18:34
def reverse( x):
    num = (int(str(x)[::-1]) if x > 0 else int(str(x * -1)[::-1]) * -1)#列表的遍历，通过对正数处理再变复数 3元表达式
    return 0 if abs(num) > 2**31 - 1 else num

x=-32424
print(reverse(x))