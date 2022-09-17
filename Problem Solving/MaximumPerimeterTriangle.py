#https://www.hackerrank.com/challenges/maximum-perimeter-triangle/problem

# The function is expected to return an INTEGER_ARRAY.-non decreasing
# The function accepts INTEGER_ARRAY sticks as parameter.
#

def maximumPerimeterTriangle(sticks):
	sticks.sort(reverse=True)#suficiente pues len(sticks)<50
	for i in range(len(sticks)-2):
		for j in range(i+1,len(sticks)-1):
			for k in range(j+1,len(sticks)):
				if sticks[i]<sticks[j]+sticks[k]:
					return [sticks[k],sticks[j], sticks[i]]
	return -1

print(maximumPerimeterTriangle([1,1,1,2,3,5]))
