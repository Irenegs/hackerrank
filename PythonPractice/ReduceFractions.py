from fractions import Fraction
from functools import reduce

'''
reduce aplica la función DE DOS ELEMENTOS indicada (en este caso lambda) a los dos primeros elementos de la lista [fracs] y luego el resultado con el siguiente elemento y así hasta acabar la lista
'''

def product(fracs):
	t = Fraction(reduce(lambda x,y: Fraction(x.numerator*y.numerator, x.denominator*y.denominator), fracs))
	return t.numerator, t.denominator

if __name__ == '__main__':
	fracs = []
	for _ in range(int(input())):
		F=Fraction(*map(int, input().split()))
		fracs.append(F)
	result = product(fracs)
	print(*result)
