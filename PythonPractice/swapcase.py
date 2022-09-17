def swap_case(s):
    res=[]
    for i in s:
        if i.isalpha()!=True:
            j=i
        elif i.isupper():
            j=i.lower()
        else:
            j=i.upper()
        res.append(j)
    cadena=''.join(res)
    return cadena

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
