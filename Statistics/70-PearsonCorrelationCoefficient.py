
import statistics

n=10#int(input())

dataX=[10, 9.8, 8, 7.8, 7.7, 7, 6, 5, 4, 2]#list(map(float,input().split()))

dataY=[200, 44, 32, 24, 22, 17, 15, 12, 8, 4]#list(map(float,input().split()))

EX=statistics.mean(dataX)

EY=statistics.mean(dataY)

s=0

for i in range(n):
    s+=(dataX[i]-EX)*(dataY[i]-EY)

r=s/(n*statistics.pstdev(dataX)*statistics.pstdev(dataY))

print('{0:.3f}'.format(r))

print(EX, EY, statistics.pstdev(dataX), statistics.pstdev(dataY))
