for _ in range(int(input())):
    a=int(input())
    A=set(input().split())
    b=int(input())
    B=set(input().split())
    subset=True
    for i in A:
        if not(i in B):
            subset=False
            break
    print(subset)
