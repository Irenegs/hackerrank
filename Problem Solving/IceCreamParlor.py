#https://www.hackerrank.com/challenges/icecream-parlor/problem

# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER m
#  2. INTEGER_ARRAY arr
#

def icecreamParlor(m, arr):
	for i in range(len(arr)):
		if m-arr[i] in arr[:i]+arr[i+1:]:
			L=arr[:i]+arr[i+1:]
			return sorted([i+1,L.index(m-arr[i])+2])

print(icecreamParlor(4,[2,2,3,4]))

'''
fichero=open('inputICP.txt')
lineas=fichero.readlines()
for j in range(int(lineas[0])):
	c=int(lineas[j*3+1])
	lista=list(map(int, lineas[j*3+3].split()))
	print(icecreamParlor(c,lista))
fichero.close()
'''
