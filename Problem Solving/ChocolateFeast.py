
import math
import os
import random
import re
import sys



def chocolateFeast(n, c, m):
    b=n//c
    w=b
    while w>=m:
        a=w//m
        b+=a
        w=w%m+a
    return b
	




N,C,M=map(int, input().split())

print(chocolateFeast(N,C,M))
