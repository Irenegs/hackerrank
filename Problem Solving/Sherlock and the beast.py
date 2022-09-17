#https://www.hackerrank.com/challenges/sherlock-and-the-beast/problem

'''
#A Decent Number has the following properties:

    Its digits can only be 3's and/or 5's.
    The number of 3's it contains is divisible by 5.
    The number of 5's it contains is divisible by 3.
    It is the largest such number for its length.
'''
# The function accepts INTEGER n as parameter.
#

def decentNumber(n):
	for i in range(n//3,-1,-1):
		if (n-3*i)%5==0:
			print('5'*(3*i)+'3'*(n-3*i))
			return
	print(-1)


#segunda opción

def DecentNumber(n):
	if n%3==0:
		print('5'*n)
	elif n%3==2 and n>3:
		print('5'*(n//3-1)*3+'3'*5)
	elif n%3==1 and n>9:
		print('5'*(n//3-3)*3+'3'*10)
	else:
		print(-1)
		
for i in range(1,100):
	print(i)
	print(int(decentNumber(i))-int(DecentNumber(i)))
