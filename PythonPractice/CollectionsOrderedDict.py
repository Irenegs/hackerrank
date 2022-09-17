from collections import OrderedDict
market=OrderedDict()

for _ in range(int(input())):
    #name, p=input().rsplit(None, 1)   ------- de esta forma se corta desde la derecha 1 corte, None=espacios o similar, p queda str, habría que convertir en int en las líneas 10 y 12
    product=input().split()
    name=' '.join(product[:(len(product)-1)])
    p=int(product[(len(product)-1)])
    if name in market:
        market[name] += p
    else:
        market[name] = p

for i in market:
    print(i, market[i])
