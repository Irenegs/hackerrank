import re
T=int(input())
pattern=re.compile(r'(7|8|9)\d+')#compile?

for _ in range(T):
    n=input()
    if len(n)==10 and not(bool(re.search(r'\D',n))) and bool(pattern.match(n)):
        print('YES')
    else:
        print('NO')
