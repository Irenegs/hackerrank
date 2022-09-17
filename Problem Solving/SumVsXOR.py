
#https://www.hackerrank.com/challenges/sum-vs-xor/problem
import math


def sumXor(n):
	c=-1
	s=str(bin(n))
	for i in s:
		if i=='0':
			c+=1
	return pow(2,c)
'''
TIME OUT
    c=1
    M=pow(2,int(math.log(n,2)+1))
    for i in range(1,M-n):
        if n+i==n^i:
            c+=1
    return c
'''
print(sumXor(5))
print(sumXor(1000000000000000))
