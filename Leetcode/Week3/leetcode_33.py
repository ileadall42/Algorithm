class Solution(object):
    def search(self, nums, target):
        begin, end = 0, len(nums) - 1
        while begin < end:      #这不是普通的二分查找方法  普通的二分查找是有序的  这个只是部分有序
            mid = (begin + end) / 2    #二分法关键在于设置对的区间   拿  0和中点大小比较是为了确定旋转轴在哪 特点决定了入手的方向
            if nums[0] <= target <= nums[mid] or (nums[0] > nums[mid] and target >= nums[0]) or (nums[0] > nums[mid] and target <= nums[mid]):
                end = mid  #如果pivot 在mid右边的话一定满足 nums[0]<=target<=nums[mid] 但是如果旋转轴在mid 左边的话 那么一定nums[0]>nums[mid]  那么什么时候可以移动
                #移动end呢？也就是在那两个取值内可以移动
            else:
                begin = mid + 1
        return begin if target in nums[begin:begin+1] else -1