# -*- coding:utf-8 -*-
__author__ = 'Shining'

'''
Leetcode-Python-461. - Hamming Distance

461. Hamming Distance
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
Given two integers x and y, calculate the Hamming distance.
Note:
0 ≤ x, y < 231.

Example
Input: x = 1, y = 4
Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑
The above arrows point to positions where the corresponding bits are different.
'''

def hammingDistance(x, y):

	two_x = []
	two_y = []
	ans = 0

	if x == 0:
		for i in range(33):
			two_x.append(0)
	if y == 0:
		for i in range(33):
			two_y.append(0)

	while x != 0:
		for i in range(33):
			if x/2**(32-i) == 1:
				two_x.append(1)
				x -= 2**(32-i)
			else:
				two_x.append(0)
	while y != 0:
		for i in range(33):
			if y/2**(32-i) == 1:
				two_y.append(1)
				y -= 2**(32-i)
			else:
				two_y.append(0)

	for i in range(33):
		if two_x[i] != two_y[i]:
			ans += 1
		else:
			pass

	return ans

def hammingDistance(x, y):

	two_x = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	two_y = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	ans = 0

	while x != 0:
		for i in range(33):
			if x/2**(32-i) == 1:
				two_x[i-1] = 1
				x -= 2**(32-i)
			else:
				pass
	while y != 0:
		for i in range(33):
			if y/2**(32-i) == 1:
				two_y[i-1] = 1
				y -= 2**(32-i)
			else:
				pass
	for i in range(32):
		if two_x[i] != two_y[i]:
			ans += 1
		else:
			pass

	return ans