import re
#import email.utils

def fun(s):
	emailpattern=re.compile(r'^[a-zA-Z][\w\-\_]*@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$')
	return bool(emailpattern.match(s))

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)

'''
A filter takes a function returning True or False and applies it to a sequence, returning a list of only those members of the sequence where the function returned True. A Lambda function can be used with filters.

Let's say you have to make a list of the squares of integers from to

(both included).

>> l = list(range(10))
>> l = list(map(lambda x:x*x, l))

Now, you only require those elements that are greater than 10 but less than 80.

.

>> l = list(filter(lambda x: x > 10 and x < 80, l))
'''
