# -*- coding: utf-8 -*-
# @Author: Mr.Jhonson
# @Date:   2017-08-23 09:33:19
# @Last Modified by:   Mr.Jhonson
# @Last Modified time: 2017-08-23 09:45:52
import re

def myAtoi(str):
    str = str.strip(' ')
    str = re.findall('(^[\+\-0]*\d+)\D*', str)        #正则匹配返回的是一个列表

    try:
        res = int(''.join(str))                    #然后把列表中的每个数连成字符串 
        MAX = 2147483647        #
        MIN = -2147483648
        if res > MAX:
            return MAX
        if res < MIN:
            return MIN
        return res
    except:
        return 0


str='-032'
print(myAtoi(str))
