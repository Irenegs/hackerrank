#https://www.hackerrank.com/challenges/happy-ladybugs/problem
import math
import os
import random
import re
import sys
from collections import Counter
#
# Complete the 'happyLadybugs' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING b as parameter.
#

def happyLadybugs(b):
	n=len(b)
	if n==1 and b!='_':
		return 'NO'
	if "_" in b:
		C=Counter(b)
		for i in b:
			if C[i]==1 and i!='_':
				return 'NO'
	else:
		if b[0]!=b[1] or b[n-1]!=b[n-2]:
			return 'NO'
		for i in range(1,n-1):
			if b[i-1]!=b[i] and b[i]!=b[i+1]:
				return 'NO'
	return 'YES'

print(happyLadybugs('G'))
print(happyLadybugs('GR'))
print(happyLadybugs('_GR_'))
print(happyLadybugs('_R_G_'))
print(happyLadybugs('R_R_R'))
print(happyLadybugs('RRGGBBXX'))
print(happyLadybugs('RRGGBBXY'))
