def firstMissingPositive(nums):
    """
    :type nums: List[int]
    :rtype: int
     Basic idea:
    1. for any array whose length is l, the first missing positive must be in range [1,...,l+1],
        so we only have to care about those elements in this range and remove the rest.
    2. we can use the array index as the hash to restore the frequency of each number within
         the range [1,...,l+1]
    """
    nums.append(0)
    n = len(nums)
    for i in range(len(nums)):  # delete those useless elements
        if nums[i] < 0 or nums[i] >= n:
            nums[i] = 0
    for i in range(len(nums)):  # use the index as the hash to record the frequency of each number
        nums[nums[i] % n] += n
    for i in range(1, len(nums)):
        if nums[i] / n == 0:
            return i
    return n

# print(firstMissingPositive([2,4,5,6,7,10]))
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 1
        for i in range(len(nums)):
            try:
                while (nums[i] > 0 and nums[i] != i + 1 and nums[i] != nums[nums[i] - 1]):
                    temp = nums[nums[i] - 1]
                    nums[nums[i] - 1] = nums[i]
                    nums[i] = temp
            except:
                continue

        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        return nums[-1] + 1


class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        1. for any array whose length is l, the first missing positive must be in range [1,...,l+1],
        so we only have to care about those elements in this range and remove the rest.
        2. we can use the array index as the hash to restore the frequency of each number within
             the range [1,...,l+1]
        """
        for i in range(len(nums)):
            if nums[i] > 0 and nums[i] < len(nums) and nums[i] != nums[nums[i] - 1]:
                # nums[i], nums[nums[i] - 1] = nums[nums[i] - 1], nums[i]
                temp=nums[i]
                nums[i]=nums[nums[i]-1]
                nums[temp-1]=temp

        for i in range(len(nums)):
            if nums[i] - 1 != i:
                return i + 1
        return len(nums) + 1
S=Solution()
print(S.firstMissingPositive([-10,-3,-100,-1000,-239,1]))