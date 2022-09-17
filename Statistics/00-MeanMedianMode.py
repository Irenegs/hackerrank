import statistics
N=int(input())

data=list(map(int,input().split()))

mean=float(statistics.mean(data))

med=statistics.median(data)

mod=min(statistics.multimode(data))

print('{0:.1f}'.format(mean))
print('{0:.1f}'.format(med))
print(mod)
