'''
import statistics

Ndata=list(map(int,input().split()))


N=statistics.NormalDist(Ndata[0],Ndata[1])

p1=N.cdf(float(input()))

data=list(map(float,input().split()))

p2=N.cdf(data[1])-N.cdf(data[0])

print('{0:.3f}'.format(p1))

print('{0:.3f}'.format(p2))
'''


import statistics

Ndata=list(map(int,input().split()))


N=statistics.NormalDist(Ndata[0],Ndata[1])

p1=100-N.cdf(float(input()))*100

p2=N.cdf(float(input()))*100

print('{0:.2f}'.format(p1))

print('{0:.2f}'.format(100-p2))

print('{0:.2f}'.format(p2))
