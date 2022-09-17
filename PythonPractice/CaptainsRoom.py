from collections import Counter

if __name__ == '__main__':
    k=int(input())
    r=map(int, input().split())
    R=Counter(r)
    sr=sorted(R.items(), key=lambda pair: pair[1])
    print(sr[0][0])
