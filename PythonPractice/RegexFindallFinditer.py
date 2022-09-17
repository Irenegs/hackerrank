import re
'''
L=map(str.replace(r'[^aeiou]',''),re.finiter(r'[^aeiou](a|e|i|o|u)+[^aeiou]', input()))
for i in L:
    print(i)
'''
L=re.findall(r'(?=([^AEIOUaeiou][A|E|I|O|U|a|e|i|o|u][A|E|I|O|U|a|e|i|o|u]+[^AEIOUaeiou]))', input())
print(L)
if len(L)==0:
    print(-1)
else:
    for i in L:
        if not(bool(re.search(r'[^a-zA-Z]',i))):
            print(re.sub(r'[^AEIOUaeiou]','',i))

#abaabaabaabaae - no coge todas
#re.findall no coge las que se solapan para ello se incluye r'(?=(regex))'
