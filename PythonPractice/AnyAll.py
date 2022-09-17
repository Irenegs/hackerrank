n=int(input())
S=input().split()
N=map(int, S)

if all(i>0 for i in N):
    if any(a==a[::-1] for a in S):
        print(True)
    else:
        print(False)
else:
    print(False)
