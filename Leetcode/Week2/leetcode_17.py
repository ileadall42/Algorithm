from functools import reduce
import time

def cst_time(func, *args, **kwargs):
    def wrapper(*args, **kwargs):
        start = time.time()
        ret = func(*args, **kwargs)
        end = time.time()
        timestrap = end -start
        print('function %s running time is %s'%(func.__name__,timestrap))
        return ret
    return wrapper


@cst_time
def letterCombinations(digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    if '' == digits: return []
    kvmaps = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }
    return reduce(lambda acc, digit: [x + y for x in acc for y in kvmaps[digit]], digits, [''])  #reduce
#就是执行一个二元函数，并把函数的结果作为下一次的输入输入进去  在这里是【''】首先输入一个空字符串 和 digits字符串（用来遍历传入的）


import itertools
@cst_time
def letterCombinations2(digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        mapping = {'0':'', '1':'', '2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        groups = [mapping[d] for d in digits if d != '0' and d != '1']     #取出所有数字对应的结果
        return [''.join(x) for x in itertools.product(*groups)]           #把所有结果一一列举 笛卡尔积


digit='37972'
print(letterCombinations(digit))
print(letterCombinations2(digit))
