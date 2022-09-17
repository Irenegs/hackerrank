# Enter your code here. Read input from STDIN. Print output to STDOUT
N,M=map(int, input().split())
l=[]
for i in range(N//2):
    x='-'*(M//2-3*i-1)+'.|.'*(2*i+1)+'-'*(M//2-3*i-1)
    l.append(x)
    print(x)
print('-'*(M//2-3)+'WELCOME'+'-'*(M//2-3))
for i  in range(len(l)):
    print(l[len(l)-(i+1)])
