def solve(s):
    l=s.split(' ')
    L=[]
    for i in l:
        L.append(i.capitalize())
    return " ".join(L)

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)
    print(result)
    #fptr.write(result + '\n')

