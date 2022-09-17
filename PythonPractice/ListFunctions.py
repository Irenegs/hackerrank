if __name__ == '__main__':
    N = int(input())
    L=[]
    for i in range(N):
        action=input().split()
        if action[0]=="print":
            print(L)
        else:
            fnc=getattr(L, action[0])
            arg=map(int, action[1:])
            fnc(*arg)
        '''
        if action[0]=="print":
            print(L)
        if action[0]=="pop":
            L.pop()
        if action[0]=="reverse":
            L.reverse()
        if action[0]=="sort":
            L.sort()
        if action[0]=="append":
            L.append(int(action[1]))
        if action[0]=="remove":
            L.remove(int(action[1]))
        if action[0]=="insert":
            L.insert(int(action[1]),int(action[2]))'''
