from itertools import combinations

s, k=input().split()

letters=''.join(sorted(list(s)))

for i in range(int(k)):
    comb=list(combinations(letters,i+1))
    for c in comb:
        l=''.join(c)
        print(l)
