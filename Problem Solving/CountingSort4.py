#https://www.hackerrank.com/challenges/countingsort4/problem


import math
import os
import random
import re
import sys

def countingSort(arr):
	n=len(arr)
	Freqarr=list([0,''] for i in range(100))
	for i in range(n):
		if i<n//2:
			arr[i][1]='-'
		arr[i][0]=int(arr[i][0])
		Freqarr[arr[i][0]][0]+=1
		if Freqarr[arr[i][0]][1]=='':
			Freqarr[arr[i][0]][1]=arr[i][1]
		else:
			Freqarr[arr[i][0]][1]+=' '+arr[i][1]
	S=''
	for i in range(100):
		if Freqarr[i][1]!='':
			S+=' '+Freqarr[i][1]
	return S
['a','','b']

print(countingSort([['0', 'ab'], ['6', 'cd'], ['0', 'ef'], ['6', 'gh'], ['4', 'ij'], ['0', 'ab'], ['6', 'cd'], ['0', 'ef'], ['6', 'gh'], ['0', 'ij'], ['4', 'that'], ['3', 'be'], ['0', 'to'], ['1', 'be'], ['5', 'question'], ['1', 'or'], ['2', 'not'], ['4', 'is'], ['2', 'to'], ['4', 'the']]))
print(countingSort([['1', 'e'], ['2', 'a'], ['1', 'b'], ['3', 'a'], ['4', 'f'], ['1', 'f'], ['2', 'a'], ['1', 'e'], ['1', 'b'], ['1', 'c']]))
