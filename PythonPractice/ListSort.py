#!/bin/python3

import math
import os
import random
import re
import sys
import operator

def sorting(LIST, num):
    LIST.sort(key=operator.itemgetter(num))    


if __name__ == '__main__':
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    k = int(input())
    sorting(arr, k)
    for i in arr:
        print(*i)
