def print_formatted(number):
    l=len(bin(number))-1
    for i in range(1, number+1):
        o=(oct(i).replace("0o","")).upper()
        h=(hex(i).replace("0x","")).upper()
        b=(bin(i).replace("0b","")).upper()
        print(str(i).rjust(l,' '),o.rjust(l,' '),h.rjust(l,' '),b.rjust(l,' '))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
