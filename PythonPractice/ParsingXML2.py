import xml.etree.ElementTree as etree

maxdepth = 0
def depth(elem, level):
	global maxdepth
	D=[]
	for child in elem:
		D.append(depth(child,level+1))
	if len(D)!=0:
		dep=max(D)+1
	else:
		dep=0
	if maxdepth<dep:
		maxdepth=dep
	return dep

#def read(file):	PARA LEER INPUT DESDE UN ARCHIVO
#	with open(file,'r') as f:
#		txt=f.read()
#	return txt
	
	

if __name__ == '__main__':
	n = int(input())
	xml =''
	for i in range(n):
		xml =  xml + input() + "\n"
#	xml=read(ruta fichero)
	tree = etree.ElementTree(etree.fromstring(xml))
	depth(tree.getroot(), -1)
	print(maxdepth)
