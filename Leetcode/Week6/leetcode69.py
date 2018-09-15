from sklearn.linear_model import LogisticRegression
from asyncio import concurrent
class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left, right, res = 0, x+1, 0
        while left < right:
            # print(res, left, right)
            
            res = left + (right - left)//2
            if res * res > x:
                right = res
            else:
                left = res + 1
        return left - 1

print("hello,world")