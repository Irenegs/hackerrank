'''
Start : Tag1
End   : Tag1
Start : Tag2
-> Attribute2[0] > Attribute_value2[0]
-> Attribute2[1] > Attribute_value2[1]
-> Attribute2[2] > Attribute_value2[2]
Start : Tag3
-> Attribute3[0] > None
Empty : Tag4
-> Attribute4[0] > Attribute_value4[0]
End   : Tag3
End   : Tag2

Start : html
Start : head
Start : title
End   : title
End   : head
Start : body
-> data-modal-target > None
-> class > 1
Start : h1
End   : h1
Empty : br
End   : body
'''

from html.parser import HTMLParser

parser=HTMLParser

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
	def handle_starttag(self, tag, attrs):
		print("Start :", tag)
		if len(attrs)!=0:
			for i in attrs:
				print('-> '+str(i[0])+' > '+str(i[1]))
	def handle_endtag(self, tag):
		print("End   :", tag)
	def handle_startendtag(self,tag,attrs):
		print('Empty :', tag)
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
