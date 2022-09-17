a=int(input())
A=set(map(int, input().split()))
b=int(input())
B=set(map(int, input().split()))

U=A.union(B)

print(len(U))
