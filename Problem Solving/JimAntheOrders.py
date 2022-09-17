#https://www.hackerrank.com/challenges/jim-and-the-orders/problem


# The function is expected to return an INTEGER_ARRAY.
# The function accepts 2D_INTEGER_ARRAY orders as parameter.
#

def jimOrders(orders):
	L=[]
	for i in range(len(orders)):
		L.append([orders[i][0]+orders[i][1],i+1])
	L.sort()
	return [x[1] for x in L]

print(jimOrders([[1, 3], [2, 3], [3, 3]]))
