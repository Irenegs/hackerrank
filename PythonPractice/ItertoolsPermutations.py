from itertools import permutations

s, k=input().split()

letters=''.join(sorted(list(s)))

per=list(permutations(letters,int(k)))

for i in per:
    l=''.join(i)
    print(l)
