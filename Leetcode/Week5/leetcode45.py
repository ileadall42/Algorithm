class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        ans = []
        curr = 0
        if n == 1:
            return 0

        def dfs(nums, ans, curr, index, target):
            for step in reversed(range(1, nums[index] + 1)):
                if step > target - 1:
                    continue

                if step == target - 1:
                    ans.append(curr + 1)
                    continue

                else:
                    dfs(nums, ans, curr + 1, index + step, target - step)

        dfs(nums, ans, curr, 0, n)
        return min(ans)

class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        ans = []
        curr = 0

        # if n == 1:
        #     return 0

        def bfs(nums, ans, curr, index, target):
            flag = 0
            next_step = {'index':0,'values':0}
            for step in range(1, nums[index] + 1):
                if step > target - 1:
                    break

                if step == target - 1:
                    ans.append(curr + 1)
                    flag=1
                    break
                if next_step['index']<step and next_step['values']<=nums[index+step]:
                    next_step['index']=step#走多少步
                    next_step['values']=nums[index+step]#走的步数遇到对应最大的步数的值
            if flag==0:
                bfs(nums, ans, curr + 1, index+next_step['index'] , target-next_step['index'])

        bfs(nums, ans, curr, 0, n)
        return min(ans)
#bfs  25000的时候不行 超出时间了


class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = lastIdx = nextIdx = 0
        while nextIdx < len(nums) - 1:
            ans += 1
            lastIdx, nextIdx = nextIdx, max(i + nums[i] for i in range(lastIdx, nextIdx + 1))#在当前index 和最大步数中的数字选一个#nums[i] 最大的步数的下表及位置就过去
        return ans



class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        curr = 0
        maximum = 0
        count = 0
        while maximum<n-1:
            count += 1
            temp = maximum
            while curr<=temp and curr<n:
                if curr+nums[curr]>maximum:
                    maximum = curr+nums[curr]
                curr += 1
        return count





class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        curr = 0
        maximum = 0
        count = 0
        while maximum<n-1:
            count += 1
            temp = maximum#最快的
            while curr<=temp and curr<n:
                if curr+nums[curr]>maximum:
                    maximum = curr+nums[curr]
                curr += 1
        return count




S=Solution()
nums=[6,2,6,1,7,9,3,5,3,7,2,8,9,4,7,7,2,2,8,4,6,6,1,3]
print(len(nums))
# print(S.jump(nums))
        #超时的 dfs  n=24就超时了