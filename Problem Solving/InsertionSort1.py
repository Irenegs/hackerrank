
#https://www.hackerrank.com/challenges/insertionsort1/problem

def insertionSort1(n, arr):
	elem=arr[n-1]
	for i in range(n-2,-1,-1):
		if elem>arr[i]:
			L=arr[:i+1]+[elem]+arr[i+1:n-1]
			print(' '.join(str(x) for x in L))
			break
		else:
			L=arr[:i+1]+arr[i:n-1]
			print(' '.join(str(x) for x in L))
	L=[elem]+arr[:n-1]
	print(' '.join(str(x) for x in L))	

insertionSort1(10,[2, 3, 4, 5, 6, 7, 8, 9, 10, 1])

'''
Sorting challenges
Insertion Sort challenges

    Insertion Sort 1 - Inserting
    Insertion Sort 2 - Sorting
    Correctness and loop invariant
    Running Time of Algorithms

Quicksort challenges

    Quicksort 1 - Partition
    Quicksort 2 - Sorting
    Quicksort In-place (advanced)
    Running time of Quicksort

Counting sort challenges

    Counting Sort 1 - Counting
    Counting Sort 2 - Simple sort
    Counting Sort 3 - Preparing
    Full Counting Sort (advanced)
'''
