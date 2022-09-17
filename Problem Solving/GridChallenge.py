#https://www.hackerrank.com/challenges/grid-challenge/problem


def gridChallenge(grid):
    # Write your code here
    for i in range(len(grid)):
        grid[i]=sorted(grid[i])
    for i in range(len(grid[0])):
        for j in range(1,len(grid)):
            if grid[j-1][i]>grid[j][i]:
                return 'NO'
    return 'YES'

print(gridChallenge(['abc','lmp','qrt']))
