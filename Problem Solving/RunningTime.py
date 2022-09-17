#https://www.hackerrank.com/challenges/runningtime/problem


# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def runningTime(arr):
	shifts=0
	n=len(arr)
	for i in range(1,n):
		for j in range(i-1,-1,-1):
			shifts+=1
			if arr[i]>arr[j]:
				arr=arr[:j+1]+[arr[i]]+[arr[k] for k in range(j+1,n) if k != i]
				shifts-=1
				break
			if arr[i]==arr[j]:
				arr=arr[:j+1]+[arr[i]]+[arr[k] for k in range(j+1,n) if k != i]
				shifts-=1
				break
			if j==0 and arr[i]<arr[0]:
				arr=[arr[i]]+[arr[k] for k in range(n) if k != i]
	return shifts

print(runningTime([2, 1, 3, 1, 2]))
print('#####')
print(runningTime([406, 157, 415, 318, 472, 46, 252, 187, 364, 481, 450, 90, 390, 35, 452, 74, 196, 312, 142, 160, 143, 220, 483, 392, 443, 488, 79, 234, 68, 150, 356, 496, 69, 88, 177, 12, 288, 120, 222, 270, 441, 422, 103, 321, 65, 316, 448, 331, 117, 183, 184, 128, 323, 141, 467, 31, 172, 48, 95, 359, 239, 209, 398, 99, 440, 171, 86, 233, 293, 162, 121, 61, 317, 52, 54, 273, 30, 226, 421, 64, 204, 444, 418, 275, 263, 108, 10, 149, 497, 20, 97, 136, 139, 200, 266, 238, 493, 22, 17, 39]))
