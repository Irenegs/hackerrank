def average(array):
    # your code goes here
    s=set(array)
    av=sum(s)/len(s)
    return float("{:.3f}".format(av))

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
