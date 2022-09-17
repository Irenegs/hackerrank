from itertools import groupby

def contador(string):
    cont=[]
    for k,g in groupby(string):
        cont.append((len(list(g)),int(k)))
    return cont
'''def contador(string):
for k,g in groupby(string):
    yield (len(list(g)),int(k))
Versión que hace un generador directamente
'''

if __name__=="__main__":
    s=input()
    print(*contador(s))
