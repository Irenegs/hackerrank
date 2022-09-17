if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    conjunto=set(arr)
    orden=sorted(conjunto)
    m=len(orden)
    i=orden[m-2]
    print(i)
