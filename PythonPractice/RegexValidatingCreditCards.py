import re

def validating(string):
	pat1=re.compile(r'^(\d{4}-{1}){3}\d{4}$')#falta símbolo para el comienzo
	pat2=re.compile(r'^\d{16}$')
	pat3=re.compile(r'^(4|5|6).*')
	pat4=re.compile(r'(\d)\1{3,}')#repeticiones del mismo character
	if bool(re.match(pat1, string)) or bool(re.match(pat2,string)):
		st=re.sub('-','',string)
		if bool(re.match(pat3, st)) and not bool(re.search(pat4, st)):
				return 'Valid'
	return 'Invalid'
	


if __name__=='__main__':
	for _ in range(int(input())):
		print(validating(input()))
