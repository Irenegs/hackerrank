#https://www.hackerrank.com/challenges/manasa-and-stones/problem

import math
import os
import random
import re
import sys

#
# Complete the 'stones' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER a
#  3. INTEGER b
#

def stones(n, a, b):
	L=[]
	A=min(a,b)
	B=max(a,b)
	for i in range(n):
		L.append(i*B+(n-1-i)*A)
	return L

print(stones(73,25,25))
print(stones(83,86,81))
