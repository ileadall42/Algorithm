# -*- coding: utf-8 -*-
# @Author: Mr.Jhonson
# @Date:   2017-08-23 21:51:25
# @Last Modified by:   Mr.Jhonson
# @Last Modified time: 2017-08-23 22:05:05
import re
def isMatch( s, p):
    """
    :type s: str
    :type p: str
    :rtype: bool
    """
    pattern=re.compile(p)
    result=pattern.match(s)
    if result:

        return True if result.group()==s else False
    else:
        return False

def isMatch2( s, p):
    dp = [[False] * (len(s) + 1) for _ in range(len(p) + 1)]
    dp[0][0] = True
    for i in range(1, len(p)):
        dp[i + 1][0] = dp[i - 1][0] and p[i] == '*'
    for i in range(len(p)):
        for j in range(len(s)):
            if p[i] == '*':
                dp[i + 1][j + 1] = dp[i - 1][j + 1] or dp[i][j + 1]
                if p[i - 1] == s[j] or p[i - 1] == '.':
                    dp[i + 1][j + 1] |= dp[i + 1][j]
            else:
                dp[i + 1][j + 1] = dp[i][j] and (p[i] == s[j] or p[i] == '.')
    return dp[-1][-1]


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not p:
            return not s

        level = {0}
        for i, c in enumerate(p[:-1], 1):
            if not level:
                return False

            if c == ".":
                if p[i] == "*":
                    level = set(range(min(level), len(s) + 1))
                else:
                    level = {j + 1 for j in level if j < len(s)}
            elif c != "*":
                if p[i] == "*":
                    tmp = set()
                    for j in level:
                        while j < len(s) and s[j] == c:
                            j += 1
                            tmp.add(j)
                    level.update(tmp)
                else:
                    level = {j + 1 for j in level if j < len(s) and s[j] == c}

        if p[-1] == "*":
            return len(s) in level
        else:
            return len(s) - 1 in level and (s[-1] == p[-1] or "." == p[-1])


s=''
p='*'
print(isMatch2(s,p))



import unittest


class Solution(object):
    def isMatch(self, s, p):
        # The DP table and the string s and p use the same indexes i and j, but
        # table[i][j] means the match status between p[:i] and s[:j], i.e.
        # table[0][0] means the match status of two empty strings, and
        # table[1][1] means the match status of p[0] and s[0]. Therefore, when
        # refering to the i-th and the j-th characters of p and s for updating
        # table[i][j], we use p[i - 1] and s[j - 1].

        # Initialize the table with False. The first row is satisfied.
        table = [[False] * (len(s) + 1) for _ in range(len(p) + 1)]

        # Update the corner case of matching two empty strings.
        table[0][0] = True

        # Update the corner case of when s is an empty string but p is not.
        # Since each '*' can eliminate the charter before it, the table is
        # vertically updated by the one before previous. [test_symbol_0]
        for i in range(2, len(p) + 1):
            table[i][0] = table[i - 2][0] and p[i - 1] == '*'

        for i in range(1, len(p) + 1):
            for j in range(1, len(s) + 1):
                if p[i - 1] != "*":
                    # Update the table by referring the diagonal element.
                    table[i][j] = table[i - 1][j - 1] and \
                                  (p[i - 1] == s[j - 1] or p[i - 1] == '.')
                else:
                    # Eliminations (referring to the vertical element)
                    # Either refer to the one before previous or the previous.
                    # I.e. * eliminate the previous or count the previous.
                    # [test_symbol_1]
                    table[i][j] = table[i - 2][j] or table[i - 1][j]

                    # Propagations (referring to the horizontal element)
                    # If p's previous one is equal to the current s, with
                    # helps of *, the status can be propagated from the left.
                    # [test_symbol_2]
                    if p[i - 2] == s[j - 1] or p[i - 2] == '.':
                        table[i][j] |= table[i][j - 1]

        return table[-1][-1]


def isMatch(s, p):
    dp = [[True] + [False] * len(s)]
    for i, pc in enumerate(p):
        row = [pc == '*' and dp[-2][0]]
        for j, sc in enumerate(s):
            if pc == '.':
                row.append(dp[-1][j])
            elif pc == '*':
                row.append(dp[-2][j + 1] or ((p[i - 1] == '.' or p[i - 1] == sc) and row[j]))
            else:
                row.append(dp[-1][j] and pc == sc)
        dp.append(row)
    return dp[-1][-1]