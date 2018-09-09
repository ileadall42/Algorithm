# -*- coding: utf-8 -*-
# @Author: mr.jhonson
# @Date:   2017-08-19 12:25:31
# @Last Modified by:   Mr.Jhonson
# @Last Modified time: 2017-08-20 11:59:56

def longestPalindrome(s):
	"""
	:type : str
	:rtype: str
	暴力求解法：1、遍历找出子串2、同时利用i++,i--双向遍历判断是否为回文子串
	先循环再if 可以达到一个目的就是循环的同时筛选
	考虑长度为1的情况判断
	"""
	start=0
	max_length=0
	for i in range(len(s)):
		if len(s)==1 or len(s)==2:
			return s
		for j in range(i+1,len(s)):
			teml,temr=i,j
			while(teml<temr):
				if (s[teml]!=s[temr]):
					break	
				temr=temr-1
				teml=teml+1
				
			if (teml>=temr) and j-i>max_length:
				max_length=j-i+1
				start=i

	if max_length>0:
		return s[start:start+max_length],max_length#起始问题一定要弄懂，就是
		#最长和起始长度一定不要忘记加开始。。利用!= if条件一般取反。
	else:
		return s[max_length],max_length#各种情况都要包含


s='abcda'
print(longestPalindrome(s))

