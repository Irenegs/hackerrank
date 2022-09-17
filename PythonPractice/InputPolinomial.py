a,k=map(int, input().split())
P=input()
print(eval(P.replace('x', str(a)))==k)
