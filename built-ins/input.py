# https://www.hackerrank.com/challenges/input/problem?isFullScreen=true

x, k = input().split()
P = input()

command = P.replace('x', x)
print(float(eval(command)) == float(k))