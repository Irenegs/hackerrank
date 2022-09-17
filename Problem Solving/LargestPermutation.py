#https://www.hackerrank.com/challenges/largest-permutation/problem

# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def largestPermutation(k, arr):
	n=len(arr)
	ch=0
	dictionary={}
	for i in range(n):
		dictionary[arr[i]]=i
	for i in range(n):
		if arr[i]!=n-i and ch<k:
			temp=arr[i]
			arr[dictionary[n-i]]=temp
			arr[i]=n-i
			dictionary[temp]=dictionary[n-i]
			dictionary[n-i]=i
			ch+=1
		if ch==k:
			break
	return arr

print(largestPermutation(1,[4,2,3,5, 1]))











'''	
	L=list(0 for i in range(n))
	ch=0
	for i in range(n):
		if arr[i]!=n-i and ch<k:
			ch+=1
			L[i]=n-i
			L[arr.index(n-i)]=arr[i]
		elif L[i]==0:
			L[i]=arr[i]
	return L
		
	ch=0
	i=0
	while ch<k and i<=n:
		if arr.index(n-ch)!=i:
			print('cambio',arr[arr.index(n-ch)],arr[i])#¿por qué no cambia el array?
			ch+=1
			arr[arr.index(n-ch)]=arr[i]
			arr[i]=n-ch
			print(arr)
		i+=1
	return arr


print(largestPermutation(1,[4,2,3,5, 1]))

fichero=open('DatosLP.txt')
lineas=fichero.readlines()
n,k=list(map(int,lineas[0].split()))
array=list(map(int,lineas[1].split()))
f = open("myfile.txt", "w") 
f.write(str(largestPermutation(k,array))+'\n')
f.close()
fichero.close()
'''
