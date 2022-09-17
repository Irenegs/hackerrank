from collections import deque

if __name__ == '__main__':
    d=deque()
    for i in range(int(input())):
        action=input().split()
        fnc=getattr(d, action[0])
        arg=map(int, action[1:])
        fnc(*arg)
        '''
        if len(action)==1:
            fnc=getattr(d, action[0])
            fnc()
        else:
            fnc=getattr(d, action[0])
            arg=map(int, action[1:])
            fnc(*arg)'''
print(" ".join(map(str,d)))
