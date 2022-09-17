for i in range(int(input())):
    a, b=input().split()
    if not(a.isdigit()):
        print('Error Code: invalid literal for int() with base 10: '+chr(39)+a+chr(39))
    elif not(b.isdigit()):
        print('Error Code: invalid literal for int() with base 10: '+chr(39)+b+chr(39))
    else:
        if int(b)==0:
            print("Error Code: integer division or modulo by zero")
        else:
            print(int(a)//int(b))
