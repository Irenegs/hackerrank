import textwrap

def wrap(string, max_width):
    l=len(string)
    m=max_width
    n=int(l/m)
    s=''
    for i in range(n):
        s=s+string[i*m:(i+1)*m]+'\n'
    s=s+string[n*m:]
    return s

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
