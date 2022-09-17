import numpy

n,m=map(int, input().split())
S=[]
for _ in range(n):
    S.append(list(map(int, input().split())))

A=numpy.sum(S, axis=0)#axis=0 suma columnas, axis=1 suma filas, default value: axis=None suma todos los elementos
print(numpy.prod(A))
