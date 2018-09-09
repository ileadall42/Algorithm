class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return len(nums)
        wr = 0
        rd = 1
        while rd < len(nums):   #用不等于 逆向思维
            if nums[rd] != nums[wr]:  #这个思想在前面的题目里面遇到过  去重的好方法。。用移动下标或者指针来判断
                wr += 1
                nums[wr] = nums[rd]
            rd=rd+1
        return wr+1

a=Solution()
print(a.removeDuplicates([1,1,2,2,4,5,6,6]))
# class Solution(object):
#     def removeDuplicates(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         if not nums:
#             return 0
#         new_slice = 0
#         for i in range(1, len(nums)):
#             if nums[i] != nums[new_slice]:
#                 new_slice += 1
#                 nums[new_slice] = nums[i]
#
#         return new_slice + 1