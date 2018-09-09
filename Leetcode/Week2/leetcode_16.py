def threeSumClosest( nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    root = {}
    nums.sort()
    for i in range(len(nums)):
        # if i>0 and  nums[i] == nums[i - 1]:
        #     continue                    无需去重
        l, r = i + 1, len(nums) - 1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            root[abs(s-target)]=s
            if s-target>0:
                r=r-1
            elif s-target<0:
                l=l+1
            else:
               return s

    return root[min(root)]


s=[0,0,0]
target=1
print(threeSumClosest(s,target))                    