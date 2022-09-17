class EvenStream(object):
    def __init__(self):
        self.current = 0

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return

class OddStream(object):
    def __init__(self):
        self.current = 1

    def get_next(self, init=0):
        to_return = self.current
        self.current += 2
        return to_return

def print_from_stream(n, stream=EvenStream()):
	if stream.__class__.__name__=='EvenStream':
		stream.current=0
	else:
		stream.current=1
	for i in range(n):
		print(stream.get_next())


queries = 1
for _ in range(queries):
	data =[['odd', '10'],['even', '7'],['odd', '4'], ['odd', '10'], ['even', '2']]#input().split()
	for i in data:
		n = int(i[1])
		if i[0] == "even":
			print_from_stream(n)
		else:
			print_from_stream(n, OddStream())
