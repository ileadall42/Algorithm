def longestCommonPrefix (strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    #给定一个数组找出数组的最长公共前缀。
    flag = False
    if len(strs) == 0:
        return ""
    answer = ''
    for i in range(1, len(strs[0]) + 1):
        common_pre = strs[0][0:i]
        for per_Str in strs:
            flag = per_Str.startswith(common_pre)
            if flag == False:
                break
        answer = strs[0][0:i] if flag else answer
        if flag == False:
            break
    return answer

def longestCommonPrefix2 (strs):
    if not strs:
        return ""

    for i, letter_group in enumerate(zip(*strs)):     #debug一看就知道返回的是什么了，利用了set的去重性
        if len(set(letter_group)) > 1:
            return strs[0][:i]
    else:
        return min(strs)


from functools import reduce

def longestCommonPrefix3(self, strs):
   def lcp(s, t):
       if len(s)>len(t):
           s, t = t, s
       for i in range(len(s)):
           if s[i]!=t[i]:
               return s[:i]
       return s
   return reduce(lcp,strs) if strs else ""    #坝上一次的结果利用到下一次使用这就是reduce






test_list=['33ab465','33ab2','33ab565']
print(longestCommonPrefix((test_list)))
print(longestCommonPrefix2((test_list)))
print(longestCommonPrefix3((test_list)))