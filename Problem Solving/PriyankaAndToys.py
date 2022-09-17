#https://www.hackerrank.com/challenges/priyanka-and-toys/problem

#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY w as parameter.
#

def toys(w):
	c=0
	W=set(w)
	while len(W)!=0:
		m=min(W)
		cont=False
		for i in range(5):
			if m+i in W:
				W.remove(m+i)
				if not cont:
					c+=1
					cont=True
	return c
print(toys([1, 2, 3, 21, 7, 12, 14, 21]))
