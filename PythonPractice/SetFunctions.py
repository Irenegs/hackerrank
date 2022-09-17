#Possible functions: pop, discard, remove
n = int(input())
s = set(map(int, input().split()))

if __name__ == '__main__':
    N = int(input())
    for i in range(N):
        action=input().split()
        if len(s)!=0:
            if action[0]=="remove" and int(action[1]) in s:
                s.remove(int(action[1]))
            elif action[0]=="discard":
                s.discard(int(action[1]))
            else:
                s.pop()
    print(sum(s))
