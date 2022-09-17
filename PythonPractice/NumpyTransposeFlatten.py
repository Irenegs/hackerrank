import numpy

n,m=map(int, input().split())
S=[]
for _ in range(n):
    S.append(list(map(int, input().split())))

print(numpy.transpose(numpy.array(S)))
print(numpy.array(S).flatten())
