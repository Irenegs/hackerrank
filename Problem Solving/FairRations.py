#https://www.hackerrank.com/challenges/fair-rations/problem
'''
B=list of loaves of bread that citizen i has.
Rules:
1- Every time you give a loaf of bread to some person i, you must also give a loaf of bread to the person immediately in front of or behind them in the line (i.e., persons i+1 or
i-1).
2- After all the bread is distributed, each person must have an even number of loaves.
RETURNS: string with the minimum number of loaves of bread needed or 'NO'
'''

def fairRations(B):
	if sum(B)%2!=0:
		return 'NO'
	else:
		bread=0
		LOD=-1
		for i in range(len(B)):
			if B[i]%2!=0:
				if LOD==-1:
					LOD=i
				else:
					bread+=(i-LOD)*2
					LOD=-1
	return str(bread)



B=list(map(int,input().split()))

print(fairRations(B))
