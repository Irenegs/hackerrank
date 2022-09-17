from collections import namedtuple
n=int(input())
order=input().split()
al=namedtuple('al',order)
s=0

for i in range(n):
    A=al(*input().split())
    s=s+int(A.MARKS)

print("{0:.2f}".format(float(s/n)))
