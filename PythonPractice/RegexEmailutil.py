import re
import email.utils

T=int(input())
emailpattern=re.compile(r'^[a-z][\w\-\.\_]*@[a-z]+\.[a-z]{1,3}$')

for _ in range(T):
    data=email.utils.parseaddr(input())
    if bool(emailpattern.match(data[1])):
        print(email.utils.formataddr(data))
