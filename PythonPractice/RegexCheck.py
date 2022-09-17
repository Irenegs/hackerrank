import re

for i in range(int(input())):
    try:
        pattern='r'+chr(39)+input()+chr(39)
        print(bool(re.compile(pattern)))
    except re.error:
        print(False)
