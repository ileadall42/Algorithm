
def longestValidParentheses(s):
    """
    :type s: str
    :rtype: int  #暴力搜索法也就是 遍寻字符串 n2 再判断是不是合法的同时记录长度
    """
    stack = []
    for e in s:
        if e == "(":
            stack.append(e)
        else:
            stack.pop()
    if stack==[]:
        return len(s)


def longestValidParentheses(self, s):
    """ as the ")" will not effect the final result, which acts as a dummy  element to
        make the all the  original elements of s equivalently,
        otherwise the first element needs to be dealt with separately.
    """
    s = ")" + s
    stack, ans = [], 0
    for index in range(len(s)):
        element = s[index]
        if element == ")" and stack and stack[-1][1] == "(":  #直接一次  边更新最大长度边向前 在最前面加一个
            #这道题的特点就是遇到"）"开始记录下标  只要这是一个孤儿也就是坏的）那我们就把它作为起始计算
            stack.pop()
            ans = max(ans, index - stack[-1][0])
        else:
            stack.append((index, element))
    return ans



class Solution(object):
    def longestValidParentheses(self, s):  #DP解法
        """
        :type s: str
        :rtype: int
        """
        # use 1D DP
        # dp[i] records the longestValidParenthese EXACTLY ENDING at s[i]
        dp = [0 for x in range(len(s))]  #构造一个数组
        max_to_now = 0
        for i in range(1,len(s)):
            if s[i] == ')':
                # case 1: ()()
                if s[i-1] == '(':
                    # add nearest parentheses pairs + 2
                    dp[i] = dp[i-2] + 2
                # case 2: (())
                # i-dp[i-1]-1 is the index of last "(" not paired until this ")"
                elif i-dp[i-1]-1 >= 0 and s[i-dp[i-1]-1] == '(':
                    if dp[i-1] > 0: # content within current matching pair is valid
                    # add nearest parentheses pairs + 2 + parentheses before last "("
                        dp[i] = dp[i-1] + 2 + dp[i-dp[i-1]-2]
                    else:
                    # otherwise is 0
                        dp[i] = 0
                max_to_now = max(max_to_now, dp[i])
        return max_to_now


def longestValidParentheses2( s):
    s = ')' + s
    dp = [0] * len(s)
    for i in range(1, len(s)):
        if s[i] == ')' and s[i - dp[i - 1] - 1] == '(':  #这个dp正常人真心很难想- -
            dp[i] = dp[i - 1] + 2 + dp[i - 2 - dp[i - 1]]
    return max(dp)

s=('()()()(')
print(longestValidParentheses2(s))