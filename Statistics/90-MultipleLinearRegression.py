#https://www.hackerrank.com/challenges/s10-multiple-linear-regression/problem
from sklearn import linear_model


m,n=list(map(int,input().split()))

X=[]
Y=[]
for _ in range(n):
	data=list(map(float, input().split()))
	X.append(data[:m])
	Y.append(data[m])

lm = linear_model.LinearRegression()
lm.fit(X, Y)
a = lm.intercept_
b = lm.coef_

q=int(input())

for _ in range(q):
	Ndata=list(map(float, input().split()))
	s=a
	for i in range(m):
		s+=b[i]*Ndata[i]
	print('{0:.2f}'.format(s))
