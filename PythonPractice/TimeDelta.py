import math
import os
import random
import re
import sys
import datetime

# Complete the time_delta function below.
def time_delta(t1,t2):
	form='%a %d %b %Y %H:%M:%S %z'
	T1=datetime.datetime.strptime(t1, form)
	T2=datetime.datetime.strptime(t2, form)
	return  str(abs(int((T1-T2).days*3600+(T1-T2).seconds)))#int((T1-T2).total_seconds()) hay que pasarlo a entero para que no tome los milisegundos

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1,t2)
        print(delta + '\n')
#fptr.write(delta + '\n')
#fptr.close()
