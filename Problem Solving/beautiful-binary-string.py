#https://www.hackerrank.com/challenges/beautiful-binary-string/problem
import re



#
# Complete the 'beautifulBinaryString' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING b as parameter.
#

def beautifulBinaryString(b):
	if bool(re.search('010',b)):
		a=len(re.findall('010',b))
		return a
	return 0

print(beautifulBinaryString('000000'))

print(beautifulBinaryString('010000'))

print(beautifulBinaryString('010010'))

print(beautifulBinaryString('010100'))
