class Solution:
    # @param {integer[]} height
    # @return {integer}
    def trap(self, height):
        n = len(height)
        l, r, water, minHeight = 0, n - 1, 0, 0
        while l < r:
            while l < r and height[l] <= minHeight:
                water += minHeight - height[l]
                l += 1
            while r > l and height[r] <= minHeight:
                water += minHeight - height[r]
                r -= 1
            minHeight = min(height[l], height[r])
        return water


class Solution(object):
    def trap(self, height):
        if not height or len(height) < 3:
            return 0
        l, r, water, l_max, r_max = 0, len(height) - 1, 0, 0, 0
        while l < r:
            if height[l] <= height[r]:
                if l_max >= height[l]:
                    water += l_max - height[l]
                else:
                    l_max = max(height[l], l_max)
                l += 1
            else:
                if r_max >= height[r]:
                    water += r_max - height[r]
                else:
                    r_max = max(height[r], r_max)
                r -= 1
        return water


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r = 0, len(height) - 1
    	ml, mr = 0, 0
    	res = 0
    	 #two pointers
        while l < r:
            if height[l] <= height[r]:
            	if height[l] >= ml:
            		ml = height[l]
            	else:
            		res += ml - height[l]  #左右夹击，有时候解决一些普通问题的同时就能解决极端情况，要考虑极端情况但是，先从
                    #简单下手  比如说以0开头，这样的话 就不会更新res
                l += 1
            else:
            	if height[r] >= mr:
            		mr = height[r]
            	else:
            		res += mr - height[r]
                r -= 1
        return res


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        if n < 2:
            return 0
        left = 0
        right = n - 1
        leftMax = 0
        rightMax = 0
        res = 0
        while left < right:
            if height[left] < height[right]:
                if height[left] < leftMax:
                    res += leftMax - height[left]
                else:
                    leftMax = height[left]
                left += 1
            else:
                if height[right] < rightMax:
                    res += rightMax - height[right]
                else:
                    rightMax = height[right]
                right -= 1
        return res