import re


def transformation(LIST):
	result=[]
	for i in LIST:
		u=re.sub(r" \|\|(?= )", " or",re.sub(r" &&(?= )", " and", i))#r'(?<= )&&(?= )' no consume los espacios, aunque exige que exista. Realmente es una mejor solución.
		result.append(u)
	return result



if __name__ == '__main__':
	Code=[]
	for _ in range(int(input())):
		Code.append(input())
	print(*transformation(Code), sep='\n')
