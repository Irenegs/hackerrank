import numpy

n,m=map(int, input().split())
A=[]
B=[]
for _ in range(n):
    A.append(list(map(int, input().split())))
for _ in range(n):
    B.append(list(map(int, input().split())))

#operaciones punto a punto - la multiplicación no es multiplicación de matrices
print(numpy.add(A,B))
print(numpy.subtract(A,B))
print(numpy.multiply(A,B))
print(numpy.floor_divide(A,B))#división entera, numpy.divide es para división con decimales
print(numpy.mod(A,B))
print(numpy.power(A,B))
