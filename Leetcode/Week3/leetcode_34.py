class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """  #向中心靠拢的方法 中心靠拢法
        if not nums:
            return [-1,-1]
        pl=0
        pr=len(nums)-1
        while  nums and  (nums[pl]!=target or nums[pr]!=target) and pr!=pl:
            if nums[pl]!=target:
                pl+=1
            elif nums[pr]!=target:
                pr-=1
        return[pl,pr] if nums[pl]==target and nums[pr]==target else [-1,-1]

from bisect import bisect_left, bisect_right
def searchRange( nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]#左插入，重复元素在插入index以左  insort
    """              # bisect_right()      #right=mid+1  left=mid  #默认 是right  以左边相同元素处理
                    #bisect_left     right=mid  left=mid
    l, r = bisect_right(nums, target - 1), bisect_left(nums, target + 1) - 1   #搜搜某个target-1 以右的  某个target+1以左的
    if l < len(nums) and nums[l] == target:
        return [l, r]
    return [-1, -1]
nums=[1,2,3,4,5,6,7,8,8,8,8,10,12,15]
target=8
print(searchRange(nums,target))