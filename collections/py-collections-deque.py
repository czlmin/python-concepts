# https://www.hackerrank.com/challenges/py-collections-deque/problem?isFullScreen=true

from collections import deque

N = int(input())
d = deque()
for i in range(N):
    text_command = input().strip().split()
    if len(text_command) > 1:
        command, argument = text_command[0], text_command[1]
        str_command = f"d.{command}({int(argument)})"
    else:
        command = text_command[0]
        str_command = f"d.{command}()"
    try:
        exec(str_command)
    except KeyError:
        continue
print(*d)