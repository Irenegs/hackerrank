from collections import OrderedDict
words=OrderedDict()

for i in range(int(input())):
    w=input()
    if w in words:
        words[w] +=1
    else:
        words[w] =1
print(len(words))
print(" ".join(list(map(str, words.values()))))
