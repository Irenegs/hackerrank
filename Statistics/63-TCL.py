
import statistics

n=100

mu=500#int(input())

sigma=80#int(input())

p=0.95#float(input())

z=1.96#float(input())

N=statistics.NormalDist(mu*n,pow(n,0.5)*sigma)

A=N.inv_cdf(0.5+p/2)/100


print('{0:.2f}'.format(2*mu-A))

print('{0:.2f}'.format(A))
