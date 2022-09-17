A=set(input().split())
superset=True
for _ in range(int(input())):
    B=set(input().split())
    if len(A)<=len(B):
        superset=False
    else:
        for i in B:
            if not(i in A):
                superset=False
                break
print(superset)
