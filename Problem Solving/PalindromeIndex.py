#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'palindromeIndex' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def palindromeIndex(s):
	if s==s[::-1]:
		return -1
	else:
		for i in range(len(s)//2):
			if s[i]!=s[len(s)-(i+1)]:
				t=s[:i]+s[i+1:]
				u=s[:len(s)-(i+1)]+s[len(s)-i:]
				if t==t[::-1]:
					return i
				elif u==u[::-1]:
					return len(s)-(i+1)
				else:
					break
					return -1
'''	else:
		if s[0]==s[len(s)-1]:
			return 1+palindromeIndex(s[1:len(s)-1])
		elif s[0]==s[len(s)-2]:
			t=s[:len(s)-1]
			if t==t[::-1]:
				return 0
			else:
				return -1
		else:
			t=s[1:]
			if t==t[::-1]:
				return 0
			else:
				return -1

	if s==s[::-1]:
		return -1
	else:
		for i in range(len(s)):
			t=s[:i]+s[(i+1):]
			print(t)
			if t==t[::-1]:
				print(i)
				return i
				break
	return -1
'''
st=input()
print(palindromeIndex(st))
'''
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        fptr.write(str(result) + '\n')

    fptr.close()
'''
'''
revisar:
10
quyjjdcgsvvsgcdjjyq
hgygsvlfwcwnswtuhmyaljkqlqjjqlqkjlaymhutwsnwcflvsgygh
fgnfnidynhxebxxxfmxixhsruldhsaobhlcggchboashdlurshxixmfxxxbexhnydinfngf
bsyhvwfuesumsehmytqioswvpcbxyolapfywdxeacyuruybhbwxjmrrmjxwbhbyuruycaexdwyfpaloyxbcpwsoiqtymhesmuseufwvhysb
fvyqxqxynewuebtcuqdwyetyqqisappmunmnldmkttkmdlnmnumppasiqyteywdquctbeuwenyxqxqyvf
mmbiefhflbeckaecprwfgmqlydfroxrblulpasumubqhhbvlqpixvvxipqlvbhqbumusaplulbrxorfdylqmgfwrpceakceblfhfeibmm
tpqknkmbgasitnwqrqasvolmevkasccsakvemlosaqrqwntisagbmknkqpt
lhrxvssvxrhl
prcoitfiptvcxrvoalqmfpnqyhrubxspplrftomfehbbhefmotfrlppsxburhyqnpfmqlaorxcvtpiftiocrp
kjowoemiduaaxasnqghxbxkiccikxbxhgqnsaxaaudimeowojk
'''
