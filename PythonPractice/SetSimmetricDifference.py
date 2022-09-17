a=int(input())
A=set(map(int, sorted(input().split())))
b=int(input())
B=set(map(int, sorted(input().split())))

sd=(A.union(B)).difference(A.intersection(B))
l=sorted(list(sd))

for i in l:
    print(i)
