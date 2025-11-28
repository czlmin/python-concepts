# https://www.hackerrank.com/challenges/introduction-to-regex/problem?isFullScreen=true

N = int(input())
for _ in range(N):
    expression = input()
    try:
        x = float(expression)
        if expression.isnumeric():
            ret = 'True'
        else:
            ret = 'False'
    except Exception as e:
        ret = 'False'