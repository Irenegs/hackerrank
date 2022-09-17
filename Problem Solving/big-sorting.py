#https://www.hackerrank.com/challenges/big-sorting/problem

import math
import os
import random
import re
import sys

#
# Complete the 'bigSorting' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY unsorted as parameter.
#

def bigSorting(unsorted):
	lengths=[]
	for i in unsorted:
		lengths.append(len(i))
	BL=zip(lengths,unsorted)
	return [i[1] for i in sorted(BL)]

'''
n = 8
unsorted = ['1','2','300','12303479849857341718340192371','3084193741082939','3084193741082938','111','200']
lengths = []

for k in unsorted:
	#number = str(input().strip())
    #unsorted.append(number)
    lengths.append(len(k))

biglist = zip(lengths,unsorted)

#print(sorted(biglist))
print(list(biglist))

for i in sorted(biglist):
    print(i[1])


	unsorted.sort(key=int)
	for s in unsorted:
		print(s)


	L=list(0 for i in range(1,pow(10,pow(10,6))+1))
	for i in unsorted:
		print(i)
		L[int(i)]+=1
	R=[]
	for i in range(pow(10,6)):
		for j in range(L[i]):
			R.append(str(i))
	return R


def bigSorting(unsorted):
	unsorted.sort(key=int)
	return unsorted
	

SANTOS
def bigSorting(unsorted):
    # Write your code here
    for i in sorted(unsorted, key=int):
        yield i

def read_input(n):
    # Evita meter la entrada en una lista
    for _ in range(n):
        unsorted_item = input()
        yield unsorted_item

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())
    unsorted = read_input(n)
    result = bigSorting(unsorted)
    for i in result:
        # Evita tener que recorrer la lista para hacer el join
        fptr.write(i+'\n')

    fptr.close()
'''
print(bigSorting(['1','2','100','12303479849857341718340192371','3084193741082937','3084193741082938','111','200']))
print(bigSorting(['31415926535897932384626433832795','1','3','10','3','5']))

#list.sort() is faster than sorted(list)
