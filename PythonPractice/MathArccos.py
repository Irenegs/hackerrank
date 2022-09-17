import math
import numpy

def Angle(P,Q,R,S):
	PQ=numpy.subtract(Q,P)
	QR=numpy.subtract(R,Q)
	RS=numpy.subtract(S,R)
	X=numpy.cross(PQ,QR)
	Y=numpy.cross(QR,RS)
	a=numpy.dot(X,Y)
	b=numpy.linalg.norm(X)*numpy.linalg.norm(Y)
	return '{:.2f}'.format(math.acos(a/b)*180/math.pi)


if __name__ == '__main__':
	p1=numpy.array(list(map(int, input().split())))
	p2=numpy.array(list(map(int, input().split())))
	p3=numpy.array(list(map(int, input().split())))
	p4=numpy.array(list(map(int, input().split())))
	print(Angle(p1,p2,p3,p4))
