import sys

def piling(num,LIST):
    sel=sys.maxsize#otra opción float(inf)
    for i in range(len(LIST)):
        m=max(LIST[0],LIST[-1])
        if m<=sel:
            sel=m
            if m==LIST[0]:
                LIST.pop(0)
            else:
                LIST.pop()
        else:
            return "No"
    return "Yes"

if __name__=='__main__':
    for _ in range(int(input())):
        n=int(input())
        L=list(map(int, input().split()))
        print(piling(n,L))
