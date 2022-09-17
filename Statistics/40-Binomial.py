from math import comb

prop=list(map(float,input().split()))

p=prop[0]/sum(prop)

def binomial(n,k,p):
    c=comb(n,k)
    return c*pow(p,k)*pow(1-p,n-k)

P=1
for i in range(3):
    P-=binomial(6,i,p)
    
print('{0:.3f}'.format(P))
