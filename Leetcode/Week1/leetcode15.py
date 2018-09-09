def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    #暴力枚举
    root=[]
    for i in range(len(nums)-2):
        for j in range(i+1,len(nums)-1):
            for k in range(j+1,len(nums)):
                if nums[i]+nums[j]+nums[k]==0:
                    a=sorted([nums[i],nums[j],nums[k]])
                    if a not in root:
                        root.append(a)

    return root



def threeSum2(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    #类似一个最左最右向中间靠拢的搜索方法，什么时候向左，什么时候向右，类似装水的那题。这里
    #利用了相同元素就向下一个标签进行来去重
    res = []
    nums.sort()
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        l, r = i + 1, len(nums) - 1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s < 0:
                l += 1
            elif s > 0:
                r -= 1
            else:
                res.append((nums[i], nums[l], nums[r]))
                while l < r and nums[l] == nums[l + 1]:
                    l += 1
                while l < r and nums[r] == nums[r - 1]:
                    r -= 1
                l += 1
                r -= 1
    return res

nums=[-1,0,1,2,-1,-4,-1]
print(threeSum2(nums))