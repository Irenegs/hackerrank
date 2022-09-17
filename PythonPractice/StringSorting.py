
def ginsort(string):
	LC=[]#lowercase
	UC=[]#uppercase
	OD=[]#odd
	ED=[]#even
	for i in string:
		if i.isalpha():
			print('alpha')
			if i.islower():
				LC.append(i)
			else:
				UC.append(i)
		else:
			if int(i)%2!=0:
				OD.append(i)
			else:
				ED.append(i)
	return ''.join(sorted(LC))+''.join(sorted(UC))+''.join(sorted(OD))+''.join(sorted(ED))
	


if __name__=='__main__':
	print(ginsort(input()))
