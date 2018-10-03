def minWindow(s, t):
    if not s or not t:
        print("串为空")
        return ""
    left = 0
    minLen = len(s) + 2
    cnt = 0
    hash_map = {char: t.count(char) for char in t}
    result = ""
    for i in range(len(s)):
        char_count = hash_map.get(s[i], 0)
        if char_count - 1 >= 0:  # 等于0 都不能要了
            cnt += 1
            hash_map[s[i]] -= 1  # 减1
        while(len(t) == cnt):
            if i - left + 1 < minLen:
                minLen = i - left + 1
                result = s[left:minLen]

            left_count = hash_map.get(s[left], -1)
            if left_count == 0:  # 此时向左走得时候错过了多少好的数字 错过一个就得右边扩展了。
                hash_map[s[left]] += 1
                cnt -= 1
            left += 1
    print(left, minLen)
    return result


S = "ADOBECODEBANC"
T = "ABC"
minWindow(S, T)
