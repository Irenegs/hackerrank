from itertools import combinations_with_replacement

s, k=input().split()

letters=''.join(sorted(list(s)))

comb=list(combinations_with_replacement(letters,int(k)))
for c in comb:
    l=''.join(c)
    print(l)
