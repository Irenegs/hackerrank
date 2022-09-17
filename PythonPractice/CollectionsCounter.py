from collections import Counter

n=int(input())
sizes=Counter(map(int, input().split()))
sold=Counter()
m=0#money

for _ in range(int(input())):
    s,p=map(int, input().split())
    sold[s] +=1
    if sold[s]<=sizes[s]:
        m=m+p
print(m)
