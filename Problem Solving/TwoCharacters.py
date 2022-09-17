#https://www.hackerrank.com/challenges/two-characters/problem

from copy import deepcopy
from itertools import combinations
import re
# Complete the 'alternate' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def alternate(s):
	L=[0]
	S=set(s)
	for i in S:
		if bool(re.search(i*2,s)):
			s=re.sub(i,'',s)
	S=set(s)
	if len(S)<2:
		return 0
	def isalternate(STRING):
		LEN=len(STRING)
		if LEN%2==0 and STRING==STRING[:2]*(LEN//2) or LEN%2!=0 and STRING==STRING[:2]*(LEN//2)+STRING[0]:
			return LEN
		else:
			return 0
	if len(S)==2:
		return isalternate(s)
	for i in combinations(S,len(S)-2):
		t=deepcopy(s)
		for j in i:
			t=re.sub(j,'',t)
		L.append(isalternate(t))
	return max(L)

print(alternate('beabeefeab'))		
