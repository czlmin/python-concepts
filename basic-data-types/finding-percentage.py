# https://www.hackerrank.com/challenges/finding-the-percentage/problem?isFullScreen=true

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    student_mark = student_marks[query_name]
    ave_mark = sum(student_mark) / len(student_mark)
    print(f'{ave_mark:.2f}')