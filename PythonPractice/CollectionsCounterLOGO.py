import math
import os
import random
import re
import sys
from collections import Counter


if __name__ == '__main__':
    s = input()
    l=Counter(sorted(list(s)))
    for i in l.most_common(3):
        print(i[0]+' '+str(i[1]))
    '''no ha sido necesario al hacerlo sobre una sorted list
    if l[l.most_common(3)[0][0]]==l[l.most_common(3)[1][0]]:
        if l[l.most_common(3)[1][0]]==l[l.most_common(3)[0][0]]:
            #ordenar sorted(l.most_common(3), key= , reverse? t?  )
            print()
        else:
            #ordenar los dos primeros
    elif:
        if l[l.most_common(3)[1][0]]==l[l.most_common(3)[0][0]]:
            #ordenar los dos últimos
        else:
            print(l.most_common(3))#revisar formato'''
