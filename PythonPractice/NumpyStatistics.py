import numpy
numpy.set_printoptions(legacy='1.13')

n,m=map(int, input().split())
S=[]
for _ in range(n):
    S.append(list(map(int, input().split())))
print(numpy.mean(S, axis=1))
print(numpy.var(S, axis=0))
'''
if numpy.std(S)==float(0):
    print(numpy.std(S))
else:
    print('{:.11f}'.format(numpy.std(S)))
'''
print(numpy.std(S))#hay un problema con el formato del ejercicio, en el ejercicio para [[1 2][3 4]] da 11 decimales mientras que para [1] da 0.0
