import math
import os
import random
import re
import sys

#
# Complete the 'interQuartile' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY values
#  2. INTEGER_ARRAY freqs
#

def interQuartile(values, freqs):
	dic={}#guarda la frecuencia de cada dato, por si hay repeticiones
	for i in range(len(values)):
		if values[i] in dic:
			dic[values[i]]+=freqs[i]
		dic[values[i]]=freqs[i]
	V=list(set(values))
	V.sort()
	data=[]
	for i in V:
		data.extend([i]*dic[i])
	n=len(data)
	if n%4==0:
		Q1=(data[n//4-1]+data[n//4])/2
		Q3=(data[n//4*3-1]+data[n//4*3])/2
	elif n%4==2:
		Q1=data[n//4]
		Q3=data[n//4*3+1]
	elif n%4==1:
		Q1=(data[n//4-1]+data[n//4])/2
		Q3=(data[n//4*3]+data[n//4*3+1])/2
	else:
		Q1=data[n//4]
		Q3=data[3*n//4+2]
	print('{0:.1f}'.format(Q3-Q1))

values = [10, 40, 30, 50, 20, 10, 40, 30, 50, 20, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
freqs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 40, 30, 50, 20, 10, 40, 30, 50, 20]

interQuartile(values, freqs)

'''
    # Print your answer to 1 decimal place within this function
    n=len(values)
    if n%4<2:
		Q1=[n//4-1,n//4]
		if n%4==0:
			Q3=[n//4*3-1,n//4*3]
		else:
			Q3=[n//4*3,n//4*3+1]
	else:
		Q1=n//4
		if n%2==0:
			Q3=n//4*3+1
		else:
			Q3=n//4*3+2
	dic={}
	for i in range(n):
		dic[values[i]]=i
	values.sort()
	Freq=[freqs[dic[values[0]]]]
	for i range(1,n):
		a=Freq[i-1]+freqs[dic[values[i]]]
		Freq.append(a)
		if a>Q1:
'''
	
