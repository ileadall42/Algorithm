# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1

# 找出下一个排列让数字更大，如果没有更大的话就排序返回  不能另起内存
#实际上一是一个插入移位的操作


class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]ums in-place instead.
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # Use two-pointers: two pointers start from back
        # first pointer j stop at descending point
        # second pointer i stop at value > nums[j]
        # swap and sort rest
        if not nums: return None
        i = len(nums)-1
        j = -1 # j is set to -1 for case `4321`, so need to reverse all in following step
        while i > 0:
            if nums[i-1] < nums[i]: # first one violates the trendi + 1]
              j = i-1
              break
            i-=1
        for i in    range(len(nums)-1, -1, -1):
            if nums[i] > nums[j]: #
                nums[i], nums[j] = nums[j], nums[i] # swap position


class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # find longest non-increasing suffix
        right = len(nums) - 1
        while nums[right] <= nums[right - 1] and right - 1 >= 0:
            right -= 1
        if right == 0:
            return self.reverse(nums, 0, len(nums) - 1)
        # find pivot
        pivot = right - 1
        successor = 0
        # find rightmost succesor
        for i in range(len(nums) - 1, pivot, -1):
            if nums[i] > nums[pivot]:
                successor = i
                break
        # swap pivot and successor
        nums[pivot], nums[successor] = nums[successor], nums[pivot]
        # reverse suffix
        self.reverse(nums, pivot + 1, len(nums) - 1)

    def reverse(self, nums, l, r):
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1


class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        l, r = 1, len(nums) - 1
        pivot = None
        while l <= r:
            if nums[r] <= nums[r - 1]:  # mistake: should find non increasing, not non decreasing
                r -= 1
            else:
                break
        if r == 0:
            self.reverse(nums, 0)  # why nums[::-1] does not work
        else:
            pivot = r - 1
            for i in range(len(nums) - 1, pivot, -1):  # find the right most successor!!!
                if nums[i] > nums[pivot]:
                    nums[i], nums[pivot] = nums[pivot], nums[i]
                    break
            self.reverse(nums, pivot + 1)

    def reverse(self, nums, posit):
        l, r = posit, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        return nums

nums=[3,2,2,5]
print('this is the original：{dizhi}'.format(dizhi=id(nums)))
print(nextPermutation(nums))