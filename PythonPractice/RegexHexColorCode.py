import re

def colors(S):
	pat=r'\#[\d|ABCDEFabcdef]{3,6}\W'
	L=re.findall(pat, S)
	for i in re.findall(pat, S):
		pat2=r'\{[^\}]*'+i[:len(i)-1]#cuando termina en ) se ralla porque no le cuadran los paréntesis ¬¬
		if re.search(pat2,S):
			print(i[:len(i)-1])
			
if __name__ == '__main__':
	Code=''#'11#BED{color: #FfFdF8; background-color:#aef;font-size: 123px;background: -webkit-linear-gradient(top, #f9f9f9, #fff);}#Cab{background-color: #ABC;border: 2px dashed #fff;}'
	for _ in range(int(input())):
		Code=Code+input()
	colors(Code)
