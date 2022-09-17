import statistics

n,x=map(int, input().split())
data=[]
for _ in range(x):
    mark=map(float, input().split())
    data.append(list(mark))
for i in zip(*data):
    print(statistics.mean(i))
