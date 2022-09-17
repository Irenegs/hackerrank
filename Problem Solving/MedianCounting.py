#https://www.hackerrank.com/challenges/find-the-median/problem


def findMedian(arr):
	Freqarr=list(0 for i in range(20001))
	for i in range(n):
		Freqarr[arr[i]+10000]+=1
	for i in range(1, 20001):
		Freqarr[i]=Freqarr[i-1]+Freqarr[i]
		if Freqarr[i]>n//2:
			return i-10000

n=7
print(findMedian([0, 1, 2, 4, 6, 5, 3]))
