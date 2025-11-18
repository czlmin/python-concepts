# https://www.hackerrank.com/challenges/py-set-mutations/problem?isFullScreen=true

M = int(input())
A = set(input().split())
N = int(input())
# print(A)

for i in range(N):
    operator, value = input().split()
    s = set(input().split())
    # print(s)
    str_command = f"A.{operator}({s})"
    exec(str_command)

print(sum(map(int, A)))