import numpy

u=numpy.array(list(map(int, input().split())))
v=numpy.array(list(map(int, input().split())))

print(numpy.inner(u,v))
print(numpy.outer(u,v))
