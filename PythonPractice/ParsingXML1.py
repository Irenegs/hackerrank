import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
	c=0
	family = node.iter()
	for i in family:
		c+=len(i.attrib)
	return c

if __name__ == '__main__':
	xml = "<feed xml:lang='en'>    <title>HackerRank</title>    <subtitle lang='en'>Programming challenges</subtitle>    <link rel='alternate' type='text/html' href='http://hackerrank.com/'/>    <updated>2013-12-25T12:00:00</updated></feed>"
#for i in range(int(input())):
#		xml += input().rstrip()
#		xml += '\n'
#sys.stdin.readline()
#xml = sys.stdin.read()
	tree = etree.ElementTree(etree.fromstring(xml))
	root = tree.getroot()
	print(get_attr_number(root))
