class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ret = []
        self.dfs(ret, sorted(candidates), 0, target, [])
        return ret

    def dfs(self, ret, cand, idx, target, temp):

        for i in range(idx, len(cand)):
            if i > idx and cand[i] == cand[i - 1]:
                continue
            if cand[i] == target:
                # print idx, i, cand[i], target
                ret.append(temp + [cand[i]])
                break
            elif cand[i] > target:  # sorted, so any future candidates will also be too big
                break  # these two breaks save time but do not prevent duplicates in earlier idx, only this idx
            else:
                self.dfs(ret, cand, i + 1, target - cand[i],
                         temp + [cand[i]])  # idx+1 since we cannot use duplicates this time


class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ret_ans = []

        def back_tracking(self, candidates, index, target, curr_list):
            for i in range(index, len(candidates)):
                new_target = target - candidates[i]
                if new_target == 0:
                    if curr_list + [candidates[i]] not in ret_ans: #去重
                        ret_ans.append(curr_list + [candidates[i]])
                if new_target >= candidates[i]:
                    back_tracking(self, candidates, i + 1, new_target, curr_list + [candidates[i]])#不可以再选它本身了

        candidates.sort()
        back_tracking(self, candidates, 0, target, [])
        return ret_ans


class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candidates.sort()
        self.dfs(candidates, target, 0, [], res)
        return res

    def dfs(self, candidates, target, index, path, res):
        if not target:
            res.append(path)
            return
        for i in range(index, len((candidates))):
            if i > index and candidates[i] == candidates[i - 1]: continue
            if candidates[i] > target: break
            self.dfs(candidates, target - candidates[i], i + 1, path + [candidates[i]], res)
            # del path[len(path)-1]


class Solution3(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        table = [None] + [set() for i in range(target)]
        for i in candidates:
            if i > target:
                break
            for j in range(target - i, 0, -1):
                table[i + j] |= {elem + (i,) for elem in table[j]}
            table[i].add((i,))
        return map(list, table[target])
s=Solution3()
print(s.combinationSum2([1,2,3,4,6,1,2,3,4],8))