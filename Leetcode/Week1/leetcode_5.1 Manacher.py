# -*- coding: utf-8 -*-
# @Author: Mr.Jhonson
# @Date:   2017-08-20 12:00:37
# @Last Modified by:   Mr.Jhonson
# @Last Modified time: 2017-08-20 12:36:50


def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    中心扩展的方法，分为奇数和偶数的情况,
    时间复杂度为n2次方 ，把遍历子串的功夫弄出来一次遍历。（降维！）
    """
    start=0
    max_length=0
    for i in range(len(s)):#奇数的情况下
    	tmp_l=i-1
    	tmp_r=i+1
    	while (tmp_l>0 and tmp_r<len(s) and s[tmp_l]==s[tmp_r]):
    		if (tmp_r-tmp_l+1>max_length):
    			max_length=tmp_r-tmp_l+1
    			start=tmp_l

    		tmp_r=tmp_r+1
    		tmp_l=tmp_l-1



    for i in range(len(s)):#奇数的情况下
    	tmp_l=i
    	tmp_r=i+1
    	while (tmp_l>0 and tmp_r<len(s) and s[tmp_l]==s[tmp_r]):
    		if (tmp_r-tmp_l+1>max_length):
    			max_length=tmp_r-tmp_l+1
    			start=tmp_l

    		tmp_r=tmp_r+1
    		tmp_l=tmp_l-1


    if max_length>0:
    	return max_length,s[start:start+max_length]
    else:
    	return max_length,s[max_length]



s='3gdabccbaef'
print(longestPalindrome(s))
    	
    		

