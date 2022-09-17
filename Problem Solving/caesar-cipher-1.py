#https://www.hackerrank.com/challenges/caesar-cipher-1/problem

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
	q=''
	k=k%26
	for i in s:
		if i.isalpha():
			if ord(i) in range(65,91):
				NN=(ord(i)+k-65)%26+65
			if ord(i) in range(97,123):
				NN=(ord(i)+k-97)%26+97
			q+=chr(NN)
		else:
			q+=i
	return q

print(caesarCipher('middle-Outz',2))
