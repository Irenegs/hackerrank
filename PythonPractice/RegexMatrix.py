#!/bin/python3

import math
import os
import random
import re
import sys




first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

L=''


for j in range(m): #transforma en cadena de texto
	for i in range(n):
		L=L+matrix[i][j]
T=re.sub('(?<=[a-zA-Z0-9])[\W|_]+(?=[a-zA-Z0-9])',' ',L)#transforma no alfanuméricos en espacios
print(T)



	
