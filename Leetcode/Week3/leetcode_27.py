def removeDuplicates(nums,val):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) <= 1:
        return len(nums)
    tail=0
    for i in range(len(nums)):
        if nums[i]!=val:
            nums[tail]=nums[i]
            tail+=1
    return tail


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        point = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[point] = nums[i]
                point += 1
        return point


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        while True:
            if val in nums:
                nums.remove(val)
            else:
                break
        return len(nums)



class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        n = len(nums)
        p1, p2 = 0, 0
        while p2 < n:
            if nums[p2] != val:
                nums[p1]= nums[p2]
                p1 += 1
            p2 += 1
        return p1


print(removeDuplicates([3,2,2,3,5,7],8))