#https://www.hackerrank.com/challenges/detect-html-tags-attributes-and-attribute-values/problem
from html.parser import HTMLParser

parser=HTMLParser

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
	def handle_starttag(self, tag, attrs):
		print(tag)
		if len(attrs)!=0:
			for i in attrs:
				print('-> '+str(i[0])+' > '+str(i[1]))
#	def handle_endtag(self, tag):
#		print("End   :", tag)
	def handle_startendtag(self,tag,attrs):
		print(tag)
		if len(attrs)!=0:
			for i in attrs:
				print('-> '+str(i[0])+' > '+str(i[1]))
#	def handle_data(self, data):
#		print('-> '+data[0]+' > '+data[1])

# instantiate the parser and fed it some HTML
html = ""       
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()
