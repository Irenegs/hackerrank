import numpy

n,m=map(int, input().split())
S=[]
for _ in range(n):
    S.append(list(map(int, input().split())))

A=numpy.min(S, axis=1)#mínimo de los elementos axis=0 columnas, axis=1 filas, axis=None (default) mínimo o máximo de todo
print(numpy.max(A))
