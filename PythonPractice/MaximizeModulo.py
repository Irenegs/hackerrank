#https://www.hackerrank.com/challenges/maximize-it/problem
from itertools import product

K, M=map(int, input().split())

N=[]
for _ in range(K):
	N.append(list(map(int, input().split())))


for i in range(K):
	del(N[i][0])
	for j in range(len(N[i])):
		N[i][j]=pow((N[i][j]%M),2)%M#representantes clase (mod n)
	N[i]=set(N[i])#eliminar repeticiones

def maximizar(Matrix,num):
	maximum=0
	sel=[]
	for i in product(*N):
		a=sum(i)%M
		if a>maximum:
			maximum=a
	return maximum

print(maximizar(N,K))


'''
    6 767

    2 488512261 423332742 - 100

    *2 625040505 443232774 - 4

    *1 4553600 - 1

    4 92134264 617699202 124100179 337650738 - 536

    *2 778493847 932097163 - 4

    5 489894997 496724555 693361712 935903331 518538304 - 121
766
'''
