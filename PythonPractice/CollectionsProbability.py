#from collections import Counter ---para la 1ª opción
#from math import comb --- para la 2ª opción
from itertools import combinations
#import cardinality --- para la 1ª opción

def probabilityofa(numn, LIST, numk):
	Pos = sum(1 for _ in combinations(LIST, k))
	while 'a' in LIST:
		LIST.remove('a')
	Qfav= sum(1 for _ in combinations(LIST,k))
	return 1-Qfav/Pos
'''	Pos=cardinality.count(combinations(LIST, k)) --- HR no importa cardinality
	E['a']=0
	Qfav=cardinality.count(combinations(list(E),k))
''''''
	Qfav=comb(numn-E['a'],numk) -- HR no importa math.comb
	Pos=comb(numn,numk)
	
'''
if __name__=='__main__':
	n=int(input())
	s=input().split()
	k=int(input())
	print('{:.4f}'.format(probabilityofa(n,s,k)))
