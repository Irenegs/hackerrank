#https://www.hackerrank.com/challenges/maximizing-xor/problem

# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER l
#  2. INTEGER r
#

def maximizingXor(l, r):
	L=0
	for i in range(l,r):
		for j in range(i+1,r+1):
			if L<i^j:
				L=i^j
	return L
	
print(maximizingXor(10,15))


