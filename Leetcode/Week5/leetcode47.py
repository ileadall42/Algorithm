import itertools
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = list(set(itertools.permutations(nums))) #有重复的字母，要去重的话
        return ans


class Solution(object):
    def __init__(self):
        self.res = []
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.permuteRecursive(nums, [])
        return self.res

    def permuteRecursive(self, nums, result):
        if not nums:
            new_result = result[:]
            if new_result not in self.res:
                self.res.append(new_result)#超时了
                return
        for i in range(len(nums)):
            result.append(nums[i])
            self.permuteRecursive(nums[:i] + nums[i + 1:], result)
            result.pop()



class Solution(object):
    def __init__(self):
        self.res = []
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.permuteRecursive(nums, [])
        return self.res

    def permuteRecursive(self, nums, result):
        if not nums:
            new_result = result[:]
            # if new_result not in self.res:
            self.res.append(new_result)
            return
        used=[]
        for i in range(len(nums)):
            if nums[i] not in used:
                used.append(nums[i])
                result.append(nums[i])
                self.permuteRecursive(nums[:i] + nums[i + 1:], result)
                result.pop()


class Solution5(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        finalList = [[]]
        for n in nums:
            new_list = []
            for l in finalList:
                for i in range(len(l) + 1):
                    new_list.append(l[:i] + [n] + l[i:])
                    if i < len(l) and l[i] == n: break  # handles duplication#列斯广度优先搜索
            finalList = new_list
        return finalList


from collections import defaultdict
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums = sorted(nums)
        self.permuteUnique_helper(nums, 0, len(nums)-1, result)
        return result

    def permuteUnique_helper(self, nums, s, e, result):
        if s == e:
            result.append(nums[:])
            return
        for i in range(s, e+1):
            if i != s and nums[i] == nums[s]:
                continue
            nums[i],nums[s] = nums[s],nums[i]
            self.permuteUnique_helper(nums[:], s+1, e, result)


s=Solution5()
nums=[1,1,2,4,5,7]
print(s.permuteUnique(nums))


class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        for n in nums:
            temp = []
            for r in res:
                for i in range(len(r) + 1):
                    temp.append(r[:i] + [n] + r[i:])
                    if i < len(r) and r[i] == n:
                        break
            res = temp
        return res