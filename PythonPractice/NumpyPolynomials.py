import numpy

print(numpy.polyval(list(map(float, input().split())),float(input())))
'''
numpy.poly([raíces])- devuelve los coeficientes del polinomio
numpy.roots([coeficientes]) - devuelve las raíces
numpy.polyder([coeficientes]) - devuelve los coeficientes del polinomio derivado
numpy.polyint([coeficientes]) - devuelve los coeficientes del polinomio primitivo(sin término independiente)
numpy.polyval([coef], valor) - calcula el valor numérico del polinomio para dicho valor de la indeterminada
numpy.polyfit([dataX],[dataY],grado) - devuelve el polinomio aproximado a los data por mínimos cuadrados del grado indicado
polyadd, polysub, polymul, polydiv ([coef. polinomio 1],[coef. polinomio 2]) - devuelve la suma/resta/multiplicación/división de los coeficientes de ambos polinomios
'''
