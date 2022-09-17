'''import regex as re
if bool(re.search(k, S)):
    for i in re.finditer(k, S, overlapped=True):
        print((i.start(), i.end()-1))
else:
    print((-1,-1))
'''
import re
S=input()
k='(?='+input()+')'#re.compile(input())


if bool(re.search(k, S)):
    for i in re.finditer(k, S):
        print((i.start(), i.start()+len(k)-5))#cutrecito xq sin(?=) no coge las que se superponen y con ello .start y .end dan el mismo resultado
else:
    print((-1,-1))
