class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        results = []
        self.findNsum1(nums, target, 4, [], results)
        self.findNsum(nums, target, 4, [], results)
        return results

    def findNsum(self, nums, target, N, result, results):
        if len(nums) < N or N < 2: return

        # solve 2-sum
        if N == 2:
            l, r = 0, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] == target:
                    results.append(result + [nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while r > l and nums[r] == nums[r + 1]:
                        r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
        else:
            for i in range(0, len(nums) - N + 1):  # careful about range
                if target < nums[i] * N or target > nums[-1] * N:  # take advantages of sorted list
                    break
                if i == 0 or i > 0 and nums[i - 1] != nums[i]:  # recursively reduce N
                    self.findNsum(nums[i + 1:], target - nums[i], N - 1, result + [nums[i]], results)
        return

    def findNsum1(self,nums, target, N, result, results):
        if len(nums) < N or N < 2: return

        if N == 2:
            l, r = 0, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] > target:
                    r = r - 1
                elif nums[l] + nums[r] < target:
                    l = l + 1
                else:
                    results.append(result + [nums[l], nums[r]])  # 递归方法 ，，一定要先添加
                    r = r - 1
                    l = l + 1
                    while nums[l] == nums[l - 1] and l < r:
                        l = l + 1
                    while nums[r] == nums[r + 1] and l < r:
                        r = r - 1



        else:
            for i in range(0,len(nums) - N + 1):
                if target < nums[i] * N or target > nums[-1] * N:
                    break
                if i == 0 or i > 0 and nums[i] != nums[i - 1]:
                    self.findNsum1(nums[i + 1:], target - nums[i], N - 1, result + [nums[i]], results)
        return

    def fourSum(self, num, target):
        num.sort()

        def ksum(num, k, target):
            i = 0
            if k == 2:
                j = len(num) - 1
                while i < j:
                    if num[i] + num[j] == target:
                        yield (num[i], num[j])
                        i += 1
                    elif num[i] + num[j] > target:
                        j -= 1
                    else:
                        i += 1
            else:
                while i < len(num) - k + 1:
                    newtarget = target - num[i]
                    for sub in ksum(num[i + 1:], k - 1, newtarget):
                        yield (num[i],) + sub
                    i += 1

        return [list(t) for t in set(ksum(num, 4, target))]

if __name__=="__main__":
    s=[-1,0,0,1,2,-2]
    target=0
    sample=Solution()

    print(print(sample.fourSum(s,target)))