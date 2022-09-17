#https://www.hackerrank.com/challenges/tower-breakers-1/problem





# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#

def towerBreakers(n, m):
	if m==1:
		return 2
	elif n%2==0:
		return 2
	return 1


fichero=open('DatosTB.txt')
lineas=fichero.readlines()
n=int(lineas[0].split()[0])

f = open("myfile.txt", "w") 
for i in range(1,n+1):
	data=list(map(int,lineas[i].split()))
	if i<3:
		print(data[0],data[1])
	f.write(str(towerBreakers(data[0],data[1]))+'\n')
f.close()
fichero.close()
