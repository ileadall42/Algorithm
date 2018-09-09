# -*- coding: utf-8 -*-
# @Author: mr.jhonson
# @Date:   2017-08-19 13:37:00
# @Last Modified by:   mr.jhonson
# @Last Modified time: 2017-08-19 13:48:28

import timeit
import time
from functools import wraps
import profile
import cProfile

def fn_timer(function):
    @wraps(function)
    def function_timer(*args, **kwargs):
        t0 = time.time()
        result = function(*args, **kwargs)
        t1 = time.time()
        print("Total time running %s: %s seconds" %
              (function.func_name, str(t1 - t0))
              )
        return result
    return function_timer


@fn_timer
def test2(number):
	i = 0
	while(i <= number):
		i += 1


@fn_timer
def test3(number):
	i=0
	while(i <= number):
		i =  i + 1
    


if __name__ == '__main__':

	test2(10)
	test3(10)
