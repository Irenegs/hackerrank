#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cavityMap' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY grid as parameter.
#

def cavityMap(grid):
	n=len(grid)
	Matrix=[]
	for i in grid:
		a=[int(x) for x in i]
		Matrix.append(a)
	GRID=list([] for i in range(n))
	GRID[0]=''.join(list(map(str,Matrix[0])))
	for i in range(1,n-1):
		for j in range(n):
			if j==0 or j==n-1:
				GRID[i].append(Matrix[i][j])#añade acada fila
			else:
				if Matrix[i][j]<=max(Matrix[i-1][j],Matrix[i+1][j],Matrix[i][j-1],Matrix[i][j+1]):
					GRID[i].append(Matrix[i][j])
				else:
					GRID[i].append('X')
		GRID[i]=''.join(list(map(str,GRID[i])))
	GRID[n-1]=''.join(list(map(str,Matrix[n-1])))
	return GRID


grid=['9999999999','9999999999','9999999999','9999999999','9999999999','9999999999','9999999999','9999999999','9999999999','9999999999']
print(cavityMap(grid))
