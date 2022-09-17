import re

for _ in range(int(input())):
    N=input()
    fn=False
    if not(bool(re.search(r'[^\d\.\+\-]',N))) and not(re.search(r'.\..\.',N)) and not(re.search(r'.(\+|\-)',N)) and bool(re.match(r'\.|\d|\+|\-',N)) and bool(re.search(r'\.\d+', N)):#sin caracteres raros
        fn=True
    print(fn)
