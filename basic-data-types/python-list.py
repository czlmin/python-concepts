# https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true

N = int(input())
l = []
for i in range(N):
    text_command = input().strip().split()
    if len(text_command) == 3:
        command, argument_1, argument_2 = text_command[0], text_command[1], text_command[2]
        str_command = f"l.{command}({int(argument_1)}, {int(argument_2)})"
    elif len(text_command) == 2:
        command, argument_1 = text_command[0], text_command[1]
        str_command = f"l.{command}({int(argument_1)})"
    else:
        command = text_command[0]
        if command == "print":
            str_command = f"{command}({l})"
        else:
            str_command = f"l.{command}()"
    try:
        exec(str_command)
    except KeyError:
        continue