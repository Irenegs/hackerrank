def merge_the_tools(string, k):
    # your code goes here
    L=[(string[i:i+k]) for i in range(0, len(string), k)]
    for w in L:
        CL=w[0]
        for i in range(1,k):
            if w[i] not in CL:
                CL=CL+w[i]
        print(CL)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
