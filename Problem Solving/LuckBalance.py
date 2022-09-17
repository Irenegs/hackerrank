#https://www.hackerrank.com/challenges/luck-balance/problem

import math
import os
import random
import re
import sys

#
# Complete the 'luckBalance' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. 2D_INTEGER_ARRAY contests
#

def luckBalance(k, contests):
	contests.sort(reverse=True)#no es optimo, pero suficiente para el tamaño len(contests)<100
	c=0
	m=0
	for x in contests:
		if x[1]==0:
			c+=x[0]
		else:
			if m<k:
				c+=x[0]
			else:
				c-=x[0]
			m+=1
	return c
'''
	IC=[lambda x: x[0] if x[1]==1 else None, contest]
	IC.sort()
	c=0
	for i in IC
	for i in contest:
		if i[1]==1:
	
'''

print(luckBalance(3,[[5, 1], [2, 1], [1, 1], [8, 1], [10, 0], [5, 0]]))
