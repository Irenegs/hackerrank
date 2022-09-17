#https://www.hackerrank.com/challenges/separate-the-numbers/problem
'''

separateNumbers has the following parameter:

    s: an integer value represented as a string

Prints
- string: Print a string as described above. Return nothing. 

'''

def separateNumbers(s):
	N=len(s)
	if s[0]=='0':
		print('NO')
		return None
	for n in range(1,N//2+1):#n es la longitud de la primera subcadena
		print('n=',n)
		k=n#tamaño de la cadena con la que se compara
		K=n#tamaño a priori de las subcadenas siguientes
		a=0#comienzo de la primera de las dos subcadenas a comparar
		while a+K+k<=N:
			if s[a:a+k]=='9'*n:
				print('hola')
				k=n+1
			print('a=',a,'k=',k, 'K=',K)
			print(a+k,'=',int(s[a:a+K]),a+K+k,'=',int(s[a+K:a+K+k]))
			if int(s[a:a+K])+1==int(s[a+K:a+K+k]) and s[a+K]!='0':
				print('Vamos bien')
				if a+K+k==N:
					print('YES',int(s[0:n]),sep=' ')
					return None
				a+=K
				K=k
			else:
				break
	print('NO')
	
separateNumbers('91')	
#separateNumbers('1')
