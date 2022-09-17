#https://www.hackerrank.com/challenges/nim-game-1/problem

from collections import Counter

# The function is expected to return a STRING (First/Second)
# The function accepts INTEGER_ARRAY pile as parameter.
#

def nimGame(pile):
	n=len(pile)
	C=Counter(pile)
	if C[1]==n and n%2!=0:
		return 'First'
	elif C[1]==n and n%2==0:
		return 'Second'
	if C[1]==n-1:
		if n%2==0:
			pile=[1]*n
		else:
			pile=[1]*(n-1)
