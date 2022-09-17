#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'weightedUniformStrings' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER_ARRAY queries
#

def weightedUniformStrings(s, queries):
	Val=[]
	VA=ord(s[0])-96
	LU=0
	for i in range(1,len(s)):
		if s[i]!=s[i-1]:
			Val.append([VA,i-LU])
			VA=ord(s[i])-96
			LU=i
	Val.append([VA,len(s)-LU])
	Answer=[]
	for i in queries:
		found=False
		for j in Val:
			if i%j[0]==0 and i<=j[0]*j[1]:
				found=True
				Answer.append('Yes')
				break
		if not found:
			Answer.append('No')
	return Answer

print(weightedUniformStrings('abccddde',[1,3,12,5,9,10]))


'''
ERROR
	def value(x):
		return ord(x)-96
	C=Counter(map(value,s))
	print(C)
	del C[-86]
	Answer=[]
	for i in queries:
		found=False
		for l in C.keys():
			if i%l==0 and i<=l*C[l]:
				if i==34503:
					print(i,l,l*C[l])
				Answer.append('Yes')
				found=True
				break
		if not found:
			Answer.append('No')
	return Answer
fichero=open('DatosWUS.txt')
lineas=fichero.readlines()
s=lineas[0]
queries=[494025,173303,1012102,92100,31920,34503]
f = open("myfile.txt", "w") 
for i in weightedUniformStrings(s,queries):
	f.write(str(i)+'\n')
f.close()
fichero.close()


TIME OUT	
	n=len(s)
	l=s[0]
	vl=ord(s[0])-96
	W=[vl]
	for i in range(1,n):
		if s[i]==l:
			W.append(W[-1]+vl)
		else:
			l=s[i]
			vl=ord(s[i])-96
			W.append(vl)
	Answer=[]
	for i in queries:
		if i in W:
			Answer.append('Yes')
		else:
			Answer.append('No')
	return Answer

fichero=open('DatosWUS.txt')
lineas=fichero.readlines()
s=lineas[0]
queries=list(map(int,lineas[2:]))
f = open("myfile.txt", "w") 
#for i in weightedUniformStrings(s,queries):
#	f.write(str(i)+'\n')
f.close()
weightedUniformStrings(s,queries)
fichero.close()

def weightedUniformStrings(s, queries):
    # Write your code here
    Result=['No']*len(queries)
    A=dict([(chr(i),i-96) for i in range(97,123)])
    for i in A.keys():
		if i in s:
			M=max(map(len,re.findall(r'(*i*)\1*'))#maximo de las longitudes de las cadenas del caracter repetido.
    st=s[0]
    c=0
    if A[s[0]] in queries:
        Result[queries.index(A[s[0]])]='Yes'
        c+=1
    for i in range(1,len(s)):
        if s[i]==s[i-1]:
            st=st+s[i]
        else:
            st=s[i]
        v=A[s[i]]*len(st)
        if v in queries:
            Result[queries.index(v)]='Yes'
            c+=1
        if c==len(queries):
            break
    return Result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
'''
