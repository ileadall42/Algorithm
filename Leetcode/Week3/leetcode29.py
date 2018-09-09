#Divide two integers without using multiplication, division and mod operator. 不用乘除求余数。
def divide(dividend, divisor):
    positive = (dividend < 0) is (divisor < 0)
    dividend, divisor = abs(dividend), abs(divisor)  #50，3 就是50里面最多有多少个3
    #过程便是  看看1个3  剩下47  47比3大  看看（2+1） x 3 2个3 也就是47-6  看看（3+4）个3  也就是41-12 =29 或者 50-21
    #如此往返 到了16的时候



    res = 0
    while dividend >= divisor:  #位运算的操作 有关操作 一定要分清正负  用sign 去判别就最好了
                                #位运算利用所有数都是2的幂数来表示的性质来计算结果
        temp, i = divisor, 1
        while dividend >= temp:
            dividend -= temp  #temp 是记录当前数字的  24 如果能行 48肯定也能行，只要判断出了48<50  如果48不行则返回最外层必定是到了一个小范围内了
            res += i
            i <<= 1
            temp <<= 1
    if not positive:
        res = -res
    return min(max(-2147483648, res), 2147483647)


print(divide(50,3))