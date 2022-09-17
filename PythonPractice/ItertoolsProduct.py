from itertools import product

A=map(int, sorted(input().split()))
B=map(int, sorted(input().split()))

for i in (list(product(A, B))):
    print(i, end=' ')

