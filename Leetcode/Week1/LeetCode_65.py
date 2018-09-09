# -*- coding: utf-8 -*-
# @Author: Mr.Jhonson
# @Date:   2017-08-20 11:22:24
# @Last Modified by:   Mr.Jhonson
# @Last Modified time: 2017-08-22 23:45:00
def get_number(s):#用异常去处理，这是传入参数的异常
    try:
        float(s)
    except ValueError:
        return False
    else:
        return True


s = "+ 1"
print(get_number(s))