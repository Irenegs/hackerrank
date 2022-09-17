import statistics
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    SC=student_marks[query_name]
    A=statistics.mean(SC)
    print('{:.2f}'.format(A))
