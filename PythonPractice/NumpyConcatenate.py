import numpy

n,m,p=map(int, input().split())
A=[]
B=[]
for _ in range(n):
    A.append(list(map(int, input().split())))

for _ in range(m):
    B.append(list(map(int, input().split())))

print(numpy.concatenate((A,B), axis=0))
