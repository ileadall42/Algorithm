class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        def run(self, result, target, s, pre):
            # print pre
            for i in range(s, len(candidates)):

                new_target = target - candidates[i]

                if new_target == 0:
                    result.append(pre + [candidates[i]])# 一直递归回溯 ，不需要return  True or False  这个思路更直接地省去了判断
                    #求和的过程

                if new_target >= candidates[i]:
                    run(self, result, new_target, i, pre + [candidates[i]])

        result = []
        candidates.sort()
        run(self, result, target, 0, [])

        # print result

        return result


class Solution(object):
    def combinationSum(self, candidates, target):
        ret_list = []

        def backtracing(target, candidates, index, temp_list):
            if target == 0:
                ret_list.append(temp_list)
            elif target > 0:
                for i in range(index, len(candidates)):
                    new_target=target - candidates[i]
                    backtracing(new_target, candidates, i, temp_list + [candidates[i]])
        candidates.sort()
        backtracing(target,candidates , 0, [])
        return ret_list



class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.resList = []
        candidates = sorted(candidates) #已经去重了
        self.dfs(candidates,[],target,0)
        return self.resList
    def dfs(self, candidates, sublist, target, last):
        if target == 0:
            # chose "sublist" not "sublist[:]"
            # cause sublist is pointer,and sublist[:] is a list not pointer
            self.resList.append(sublist[:])
        if target< candidates[0]:
            return
        for n in candidates:
            if n > target:
                return
            if n < last:
                continue
            sublist.append(n)
            self.dfs(candidates,sublist,target - n, n)#所以为了重复只要在哪里不断 选大于当前数的就好
            sublist.pop()#很动态很抽象的操作 不过考虑情况很全




class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ways = [[] for _ in range(target+1)]
        ways[0] = [[]]
        for c in candidates:
            for i in range(c,target+1):
                for way in ways[i-c]:
                    ways[i].append(way + [c])
        return ways[target]