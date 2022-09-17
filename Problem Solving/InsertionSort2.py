#https://www.hackerrank.com/challenges/insertionsort2/problem


# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort2(n, arr):
	for i in range(1,n):
		for j in range(i-1,-1,-1):
			if arr[i]>arr[j]:
				arr=arr[:j+1]+[arr[i]]+[arr[k] for k in range(j+1,n) if k != i]
				print(' '.join(str(x) for x in arr))
				break
			if j==0 and arr[i]<arr[0]:
				arr=[arr[i]]+[arr[k] for k in range(n) if k != i]
				print(' '.join(str(x) for x in arr))


insertionSort2(7,[3, 4, 7, 5, 6, 2, 1])
print('#######')
insertionSort2(6,[1, 4, 3, 5, 6, 2])
