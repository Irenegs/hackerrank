def happiness(setsize1, setsize2, LIST,set1, set2):
    hap=0
    for i in LIST:
        if i in set1:
            hap=hap+1
        elif i in set2:
            hap=hap-1
    return(hap)

if __name__ == '__main__':
    n,m=map(int, input().split())
    numbers=list(map(int, input().split()))
    A=set(map(int, input().split()))
    B=set(map(int, input().split()))
    print(happiness(n,m,numbers,A,B))
