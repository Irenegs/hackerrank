import operator

def person_lister(f):
	def inner(people):
		for i in people:
			i[2]=int(i[2])
		L=[]
		people.sort(key=operator.itemgetter(2))
		for i in people:
			L.append(f(i))
		return L
	return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]+' '+str(person[2])

if __name__ == '__main__':
	people = [["Jake", "Jake", "42", "M"],["Jake", "Kevin", "57", "M"],["Jake", "Michael", "91", "M"],["Kevin", "Jake", "2", "M"],["Kevin", "Kevin", "44", "M"],["Kevin", "Michael", "100", "M"],["Michael", "Jake", "4", "M"],["Michael", "Kevin", "36", "M"],["Michael", "Michael", "15", "M"],["Micheal", "Micheal", "6", "M"]]
	print(*people, sep='\n')
	print(*name_format(people), sep='\n')
	
'''people = [input().split() for i in range(int(input()))]---print(*name_format(people), sep='\n')'''
