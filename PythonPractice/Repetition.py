def repetition(s):
    for i, e in enumerate(s):
        if i>0:
            if e==s[i-1] and e.isalnum():
                return e
    return -1

if __name__ == '__main__':
    R=repetition(s=input())
    print(R)


#devuelve el primer caracter del cual se encuentran dos repeticiones seguidas
