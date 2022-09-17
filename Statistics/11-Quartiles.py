#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'quartiles' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def quartiles(arr):
    # Write your code here
    arr.sort()
    if n%2==0:
        Q2=(arr[n//2-1]+arr[n//2])//2
        if n%4==0:
            Q1=(arr[n//4-1]+arr[n//4])//2
            Q3=(arr[n//4*3-1]+arr[n//4*3])//2
        else:
            Q1=arr[n//4]
            Q3=arr[n//4*3+1]
    else:
        Q2=arr[n//2]
        if n%4==1:
            Q1=(arr[n//4-1]+arr[n//4])//2
            Q3=(arr[n//4*3]+arr[n//4*3+1])//2
        else:
            Q1=arr[n//4]
            Q3=arr[3*n//4+2]
    return [Q1,Q2,Q3]



if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    data = list(map(int, input().rstrip().split()))

    res = quartiles(data)
print(res)
 #   fptr.write('\n'.join(map(str, res)))
 #   fptr.write('\n')

#    fptr.close()
