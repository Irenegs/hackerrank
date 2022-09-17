import numpy

n=int(input())
a=[]
b=[]
c=[]
for _ in range(n):
    a.append(list(map(int, input().split())))
for _ in range(n):
    b.append(list(map(int, input().split())))
A=numpy.array(a)
B=numpy.array(b)
for i in range(n):
    c.append([numpy.dot(A[i,:],B[:,j])for j in range(n)])
print(numpy.array(c))

#n=2
#numpy.cross(vector, vector) es el determinante 2x2
