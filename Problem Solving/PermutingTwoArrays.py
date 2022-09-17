#https://www.hackerrank.com/challenges/two-arrays/problem


# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#  3. INTEGER_ARRAY B
#

def twoArrays(k, A, B):
	A.sort()
	B.sort(reverse=True)
	for i in range(len(A)):
		if A[i]+B[i]<k:
			return 'NO'
	return 'YES'
	
	
	
'''
	for i in A:
		if i<k:
			found=False
			for j in B:
				if i+j>=k:
					found=True
					if k-(i+k)!=
					S.append(k-(i+k))
					if j in B:
						B.remove(j)
						found=True
						break
					print(i,j)
				if not found:
					return 'NO'
	return 'YES'

time out error n=1000
	M=max(B)
	m=min(B)
	for i in A:
		if i<k:
			found=False
			if k-i>m:
				for j in range(max(k-i,m),M+1):
					if j in B:
						B.remove(j)
						found=True
						break
					print(i,j)
				if not found:
					return 'NO'
	return 'YES'
'''
print(twoArrays(5,[2, 1, 3],[7, 8, 9]))
