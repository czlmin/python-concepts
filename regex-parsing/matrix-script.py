# https://www.hackerrank.com/challenges/matrix-script/problem?isFullScreen=true
import re

N, M = map(int, input().split())
matrix = []
for _ in range(N):
    s = input()
    matrix.append(s)
# print(list(zip(*matrix)))
decoded = ''.join([''.join(item) for item in zip(*matrix)])
print(decoded)
regex_pattern = r"([a-zA-Z0-9])[^a-zA-Z0-9]{1,}([a-zA-Z0-9])"
replacement = r'\1 \2'
new_text = re.sub(regex_pattern, replacement, decoded)
print(new_text)