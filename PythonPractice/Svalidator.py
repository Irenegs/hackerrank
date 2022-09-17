if __name__ == '__main__':
    s = input()
    AN=False
    AB=False
    D=False
    L=False
    U=False
    for i in s:
        if i.isalnum():
            AN=True
            if i.isalpha():
                AB=True
                if i.isupper():
                    U=True
                else:
                    L=True
            else:
                D=True
        if AN and AB and D and L and U:
            break
    print(AN)
    print(AB)
    print(D)
    print(L)
    print(U)
