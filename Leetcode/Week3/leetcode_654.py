def checkPossibility(A):
    p = None
    for i in range(len(A) - 1):
        if A[i] > A[i+1]:
            if p is not None: #p 不再是None 了 遇到2次大于的情况了
                return False
            p = i #第一次遇到 要看情况 如果

    return (p is None or p == 0 or p == len(A)-2 or
            A[p-1] <= A[p+1] or A[p] <= A[p+2])

s=[3,4,3,10]
print(checkPossibility(s))



def checkPossibility3( nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    one, two = nums[:], nums[:]
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            one[i] = nums[i + 1]
            two[i + 1] = nums[i]
            break
    def valid(arr):
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                return False
        return True
    return valid(one) or valid(two)

    def checkPossibility(self, nums):
        isND = lambda ns: all(map(operator.le, ns[:-1], ns[1:]))
        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                return isND(nums[:i - 1] + nums[i:]) or isND(nums[:i] + nums[i + 1:])
        return True


a=[3,4,2,3]
print(checkPossibility3(a))