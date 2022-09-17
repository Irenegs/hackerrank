import math

#a special problem is in the page numbered with its own number
#arr = número de ejercicios en cada capítulo
#k= exercises per page

def specialProblem(arr, k):
	if k==1:
		return arr[0]
	p=0
	SP=0
	for a in arr:
		cp=a//k#pages used for the chapter a
		if a%k!=0:
			cp+=1
		if a>=p+1:
			for i in range(1,cp+1):
				if p+i>k*(i-1) and p+i<=min(k*i,a):
					SP+=1
					print('Page:',p+i)
		p+=cp
	return SP

arr=map(int,input().split())

k=int(input())

print(specialProblem(arr,k))
