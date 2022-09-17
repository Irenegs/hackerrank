
data=list(map(int, input().split()))

p=data[0]/data[1]

k=int(input())

prob=p*pow(1-p,k)

print('{0:.3f}'.format(prob))
