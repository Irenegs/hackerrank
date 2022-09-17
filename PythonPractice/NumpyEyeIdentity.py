import numpy

n,m=map(int, input().split())
#numpy.identity(n) da una matriz identidad de tamaño nxn, tipo FLOAT
#numpy.eye(m,n,k=a) da una matriz mxn de 0 con 1 en la diagonal indicada por a, default k=0 es diagonal principal, si k=1 diagonal superior a la principal, si k=-1 diagonal inferior a la principal

print(numpy.eye(n,m))
