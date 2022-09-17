#https://www.hackerrank.com/challenges/flatland-space-stations/problem

#n=number of cities
#m=number of space stations >=1
#c=list of cities with a space station - unordered. Each city has no more than one space station

#return: maximum distance to a s.s. 

import math

def flatlandSpaceStations(n, c):
	if len(c)==1:
		return max(c[0],n-c[0]-1)
	SS=sorted(c)
	print(SS)
	D=[]
	for i in range(1,len(SS)):
		D.append(math.ceil((SS[i]-SS[i-1])//2))
	if SS[0]!=0:
		D.append(SS[0])
	if SS[len(SS)-1]!=n-1:
		D.append(n-1-SS[len(SS)-1])
	return max(D)
	'''#idea por si sorted(c) lo hacía muy pesado
	LastSS=min(c)
	MD=LastSS
	c.remove(LastSS)
	NextSS=min(c)
	for i in range(LastSS+1,n):
		if i not in c:
			if i>NextSS:
				LastSS=NextSS
				c.remove(NextSS)
				if len(c)==1:
					MD=max(MD, LastSS-i)
				else:
					NextSS=min(c)
			MD=max(MD,i-LastSS,NextSS-i)
	return MD
	'''
n=int(input())
c=list(map(int, input().split()))

print(flatlandSpaceStations(n,c))
