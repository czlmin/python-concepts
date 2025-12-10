import re

pattern = re.compile(r'(?<=[:\s,])#(?:[0-9A-Fa-f]{3}|[0-9A-Fa-f]{6})\b')

if __name__ == "__main__":
    n = int(input().strip())
    for _ in range(n):
        line = input()
        matches = pattern.findall(line)
        for m in matches:
            print(m)
