# 解决该问题的关键是理解清楚要求。
# 给定一个目标字符串s，一个单词集合words。
# 要求使得words集合中所有元素连续出现在s中的首位置组成的集合（元素顺序不考虑）。
#
# 正如所给实例，目标字符串s: “barfoothefoobarman”
# 对比单词集合words: [“foo”, “bar”]
# 我们发现，在pos=0 ~ 5时“barfoo”恰好匹配，则0压入结果vector；
# 在pos=9 ~ 14时“foobar”恰好匹配，则9压入结果vector；
# You are given a string, s, and a list of words, words, that are all of the same length.
# Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and
# without any intervening characters.




class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or words==[]:
            return []
        lenstr=len(s)
        lenword=len(words[0])
        lensubstr=len(words)*lenword
        times={}
        for word in words:
            if word in times:
                times[word]+=1
            else:
                times[word]=1
        ans=[]
        for i in range(min(lenword,lenstr-lensubstr+1)):
            self.findAnswer(i,lenstr,lenword,lensubstr,s,times,ans)
        return ans
    def findAnswer(self,strstart,lenstr,lenword,lensubstr,s,times,ans):
        wordstart=strstart
        curr={}
        while strstart+lensubstr<=lenstr:
            word=s[wordstart:wordstart+lenword]
            wordstart+=lenword
            if word not in times:
                strstart=wordstart
                curr.clear()
            else:
                if word in curr:
                    curr[word]+=1
                else:
                    curr[word]=1
                while curr[word]>times[word]:
                    curr[s[strstart:strstart+lenword]]-=1
                    strstart+=lenword
                if wordstart-strstart==lensubstr:
                    ans.append(strstart)


class Solution2(object):
    def _findSubstring(self, l, r, n, k, t, s, req, ans):
        curr = {}
        while r + k <= n:
            w = s[r:r + k]
            r += k
            if w not in req:
                l = r
                curr.clear()
            else:
                curr[w] = curr[w] + 1 if w in curr else 1
                while curr[w] > req[w]:
                    curr[s[l:l + k]] -= 1
                    l += k
                if r - l == t:
                    ans.append(l)

    def findSubstring(self, s, words):
        if not s or not words or not words[0]:
            return []
        n = len(s)
        k = len(words[0])
        t = len(words) * k
        req = {}
        for w in words:
            req[w] = req[w] + 1 if w in req else 1
        ans = []
        for i in range(min(k, n - t + 1)): #min  这里比较了大小，是判断n 与 t 的关系
            self._findSubstring(i, i, n , k, t, s, req, ans)
        return ans

if __name__=="__main__":
    slou=Solution2()
    s="barfoothefoobarbarman"
    words=["foo", "bar"]
    print(slou.findSubstring(s,words))