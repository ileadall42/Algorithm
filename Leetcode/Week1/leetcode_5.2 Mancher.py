# -*- coding: utf-8 -*-
# @Author: Mr.Jhonson
# @Date:   2017-08-20 12:37:16
# @Last Modified by:   Mr.Jhonson
# @Last Modified time: 2017-08-21 07:07:53


def longestPalindrome(s):
    #用符号插入的方法很好地解决了个数不够以及奇数偶数的问题！非常棒！但同时也造成更多的空间浪费

    s='\n'+'\n'.join(s)+'\n'
    # if len(s)==1:
    #     return s[0]
    p = len(s) * [0]
    id, mx = 0, 0

    for i in range(len(s)-1):
        p[i] = min(p[2 * id - i], mx - i) if (mx > i) else 1

        while  i+p[i]<len(s) and i-p[i]>=0 and (s[i + p[i]] == s[i - p[i]]):
        # while   (s[i + p[i]] == s[i - p[i]]):
            p[i] = p[i] + 1
        if (i + p[i] > mx):
            mx = i + p[i]
            id = i

    pos=p.index(max(p))
    max_length=max(p)
    s=s[pos-max_length+1:pos+max_length].replace('\n','')
    return s


s = 'csdavcsscaa'

print(longestPalindrome(s))
