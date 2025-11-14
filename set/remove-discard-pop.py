# https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem?isFullScreen=true

n = int(input())
s = set(map(int, input().split()))
m = int(input())
for i in range(m):
    text_command = input().strip().split()
    if len(text_command) > 1:
        command, argument = text_command[0], text_command[1]
        str_command = f"s.{command}({int(argument)})"
    else:
        command = text_command[0]
        str_command = f"s.{command}()"
    try:
        exec(str_command)
    except KeyError:
        continue
print(s)
print(sum(s))