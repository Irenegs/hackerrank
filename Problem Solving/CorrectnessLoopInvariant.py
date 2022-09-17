#https://www.hackerrank.com/challenges/correctness-invariant/problem

#In the InsertionSort code below, there is an error. Can you fix it? Print the array only once, when it is fully sorted. 
'''
ORIGINAL
def insertion_sort(l):
    for i in range(1, len(l)):
        j = i-1
        key = l[i]
        while (j > 0) and (l[j] > key):
           l[j+1] = l[j]
           j -= 1
        l[j+1] = key

m = int(input().strip())
ar = [int(i) for i in input().strip().split()]
insertion_sort(ar)
print(" ".join(map(str,ar)))
'''

def insertion_sort(l):
    for i in range(1, len(l)):
        j = i-1
        key = l[i]
        print(i)
        while j>=0 and l[j] > key:
           l[j+1] = l[j]
           j -= 1
        l[j+1] = key

m = 6#int(input().strip())
ar = [7, 4, 3, 5, 6, 2]#[int(i) for i in input().strip().split()]
insertion_sort(ar)
print(" ".join(map(str,ar)))
