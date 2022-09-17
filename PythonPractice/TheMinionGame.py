import re

def minion_game(string):
    # your code goes here
    K=0
    S=0
    vowels=re.compile(r'^[AEIOU]$')
    for i in range(len(string)):
        if vowels.match(string[i]):
            K=K+len(string)-i
        else:
            S=S+len(string)-i
    if K>S:
        print('Kevin', K)
    elif K==S:
        print('Dwarf')
    else:
        print('Stuart', S)

if __name__ == '__main__':
    s = input()
    minion_game(s)
