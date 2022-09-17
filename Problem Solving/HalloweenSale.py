#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'howManyGames' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER p
#  2. INTEGER d
#  3. INTEGER m
#  4. INTEGER s
#

def howManyGames(p, d, m, s):
	if s<p:
		return 0
	C=p
	G=1
	CL=p
	while CL-d>m:
		print(CL,G,'hola')
		G+=1
		CL=p-d*(G-1)
		C=C+CL
		if C>s:
			return G-1
	print(G)
	if C<s:
		G+=(s-C)//m
	else:
		G=G-1
	return G, (s-C)//m, CL
	'''
	gdis=(p-m)//d+1#games discounting prize
	Cgdis=(2*p-d*(gdis-1))*gdis//2#cost of gdis
	if Cgdis<=s:
		gmin=(s-Cgdis)//m#games with minimun prize
		G=gdis+gmin
		return G
	'''

if __name__ =='__main__':

    first_multiple_input = input().rstrip().split()

    p = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    m = int(first_multiple_input[2])

    s = int(first_multiple_input[3])

    answer = howManyGames(p, d, m, s)
    print(answer)

