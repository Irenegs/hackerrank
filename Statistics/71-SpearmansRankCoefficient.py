

import statistics

n=10#int(input())

dataX=[10, 9.8, 8, 7.8, 7.7, 1.7, 6, 5, 1.4, 2]#list(map(float,input().split()))

SX=sorted(set(dataX))


dataY=[200, 44, 32, 24, 22, 17, 15, 12, 8, 4]#list(map(float,input().split()))

SY=sorted(set(dataY))


s=0
for i in range(n):
	s+=pow(SX.index(dataX[i])-SY.index(dataY[i]),2)

r_s=1-(6*s)/(n*(pow(n,2)-1))

print('{0:.3f}'.format(r_s))

