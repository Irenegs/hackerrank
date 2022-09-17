#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'stdDev' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def stdDev(arr):
    # Print your answers to 1 decimal place within this function
    s=0
    S2=0
    for i in range(n):
        s+=arr[i]
        S2+=pow(arr[i],2)
    Var=S2/n-pow(s/n,2)
    print('{0:.1f}'.format(pow(Var,0.5)))

if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    stdDev(vals)
