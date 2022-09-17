#https://www.hackerrank.com/challenges/sherlock-and-array/problem
'''
balancedSums has the following parameter(s):

    int arr[n]: an array of integers

Returns

    string: either YES or NO


'''


def balanceSums(arr):
	if arr==arr[::-1]:
		if len(arr)%2==1:
			return 'YES'
		else:
			return 'NO'
	i=0
	j=len(arr)-1
	cl=0
	cr=0
	print(i,j)
	while i<=j:
		if arr[i]==0:
			i+=1
		if arr[j]==0:
			j-=1
		if cl<cr:
			cl+=arr[i]
			i+=1
		elif cl>cr:
			cr+=arr[j]
			j-=1
		else:
			if i==j:
				return 'YES'
			else:
				if arr[i]<arr[j]:
					cl+=arr[i]
					i+=1
				elif arr[i]>arr[j]:
					cr+=arr[j]
					j-=1
				else:
					cl+=arr[i]
					cr+=arr[j]
					i+=1
					j-=1
	return 'NO'
		
	


print(balanceSums([5,6,8,11]))
print('#####')
print(balanceSums([1,2,3]))
print('#####')
print(balanceSums([1,2,3,3]))
print('#####')
print(balanceSums([1,1,4,1,1]))
print('#####')
print(balanceSums([2,0,0,0]))
print('#####')
print(balanceSums([0,0,2,0]))
