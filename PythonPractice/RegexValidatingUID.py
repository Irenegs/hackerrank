import re

def validating(string):
	patUpper=r'.*[A-Z].*[A-Z]'
	patDigit=r'.*\d.*\d.*\d'
	patAlphaNum=r'.*(\W|\_)'
	if len(string)==10:
		print('Size')
		if len(set(string))==len(string):#no hay repeticiones
			print('Repetitions')
			if bool(re.match(patUpper,string)):
				print('Upper')
				if bool(re.match(patDigit, string)):
					print('Digit')
					if not bool(re.match(patAlphaNum,string)):
						return 'Valid'
	return 'Invalid'
	


if __name__=='__main__':
	for _ in range(int(input())):
		print(validating(input()))
