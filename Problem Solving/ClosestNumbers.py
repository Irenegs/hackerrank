#https://www.hackerrank.com/challenges/closest-numbers/problem

import math
import os
import random
import re
import sys

#n=len(arr)

def closestNumbers(arr):
	arr.sort()
	print(arr)
	dist=[]
	d=abs(arr[1]-arr[0])
	for i in range(1,n):
		D=abs(arr[i]-arr[i-1])
		if D==d:
			dist.append(arr[i-1])
		if D<d:
			d=abs(arr[i]-arr[i-1])
			dist=[arr[i-1]]
	S=[]
	for i in dist:
		S.append(i)
		S.append(i+d)
	return S
	
n=5
print(closestNumbers([5,2,3,4,1]))

print('###')
n=10
print(closestNumbers([-20, -3916237, -357920, -3620601, 7374819, -7330761, 30, 6246457, -6461594, 266854]))

print('###')
n=12
print(closestNumbers([-20, -3916237, -357920, -3620601, 7374819, -7330761, 30, 6246457, -6461594, 266854, -520, -470]))

print('###')
n=4
print(closestNumbers([5, 4, 3, 2]))

print('###')
