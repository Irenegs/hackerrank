a=int(input())
A=set(map(int,input().split()))
for i in range(int(input())):
    op, b=input().split()
    B=set(map(int,input().split()))
    fnc=getattr(A, op)
    fnc(B)
print(sum(A))
