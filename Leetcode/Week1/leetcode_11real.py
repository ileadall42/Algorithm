def maxArea( height):
    """
    :type height: List[int]
    :rtype: int
    """
    #短板决定了装水的上限，所以底*较小的边为容积 底是i的差 高是ai较小的一个
    # 两个下标变量，分别表示数组的头部和尾部，逐步向中心推移。这个推移的过程是这样的：
    # 假设现在是初始状态，下标变量i = 0
    # 表示头部, 下标变量j = height.size()，表示尾部，那么显然此时的容器的装水量取决一个矩形的大小，这个矩形的长度为j - i，高度为height[i]
    # 与height[j]
    # 的最小值(假设height[i]
    # 小于height[j])。接下来考虑是把头部下标i向右移动还是把尾部下标j向左移动呢?如果移动尾部变量j, 那么就算height[j]
    # 变高了，装水量依然没有变得更大，因为短板在头部变量i。所以应该移动头部变量i。也就是说，每次移动头部变量i和尾部变量j中的一个，哪个变量的高度小，就把这个变量向中心移动。计算此时的装水量并且和最大装水量的当前值做比较。
    # 解答如下，在LeetCode的OJ上用100ms通过。要改变短板那一块，因为改变长板的花，短板依然决定了水位，没有更多
    j=len(height)-1
    mx,i=0,0
    while(i<j):
        mx=max(mx,(j-i)*min(height[i],height[j]))
        if (height[i]<height[j]):
            i=i+1
        elif height[i]>=height[j]:
            j=j-1
    return mx
s=[5,6,87,4,2,3]
print(maxArea(s))