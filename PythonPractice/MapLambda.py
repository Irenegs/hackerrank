cube = lambda x: pow(x,3)# complete the lambda function

def fibonacci(n):
    # return a list of fibonacci numbers
    if n==0:
        F=[]
    elif n==1:
        F=[0]
    else:
        F=[0,1]
        for i in range(2,n):
            F.append(F[i-1]+F[i-2])
    return F
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
