def count_substring(string, sub_string):
    n=0
    occur=False
    for i in range(len(string)-len(sub_string)+1):
        for j in range(len(sub_string)):
            if sub_string[j]==string[i+j]:
                occur=True
            else:
                occur=False
                break
        if occur==True:
            n=n+1
    return n

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
