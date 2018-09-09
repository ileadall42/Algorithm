import itertools


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        for i in itertools.permutations(nums, len(nums)):
            ans.append(i)
        return ans


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        from itertools import permutations
        l = list(permutations(nums))

        return l


class Solution(object):
    def _permute(self, unused, partial, res):
        """
        :type nums: List[int]
        :type unused: Set[int]
        :type partial: List[int]
        :type
        """
        if (len(unused) == 0):  # A permutation is ready when all items are used
            res.append(partial)
            return

        unused_list = list(unused)

        for n in unused_list:
            unused.remove(n)
            self._permute(unused, partial + [n], res)
            unused.add(n)

    def permute(self, nums): #递归版本的  用set来看看
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if (len(nums) == 0):
            return []

        partial = []
        res = []
        unused = set(nums)

        self._permute(unused, partial, res)

        return res

class Solution(object):
    def __init__(self):
        self.res = []
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.permuteRecursive(nums, [])
        return self.res

    def permuteRecursive(self, nums, result):
        if not nums:
            new_result = result[:]
            self.res.append(new_result)
            return
        for i in range(len(nums)):
            result.append(nums[i])
            self.permuteRecursive(nums[:i] + nums[i + 1:], result)
            result.pop()