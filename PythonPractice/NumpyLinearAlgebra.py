import numpy

#linalg es un submódulo del módulo numpy

n=int(input())
a=[]
for _ in range(n):
    a.append(list(map(float, input().split())))
A=numpy.array(a)
det='{:.2f}'.format(numpy.linalg.det(A))
if det[len(det)-1]=='0':
    print('{:.1f}'.format(numpy.linalg.det(A)))
else:
    print('{:.2f}'.format(numpy.linalg.det(A)))
'''
numpy.linalg.det(array)-determinante de la matriz
vals, vect=numpy.linalg.eig(array) - autovalores y autovectores
numpy.linalg.inv(array) - inversa
https://numpy.org/doc/stable/reference/routines.linalg.html
'''
