# https://www.hackerrank.com/challenges/py-set-add/problem?isFullScreen=true

n = int(input())
countries = set()
for i in range(n):
    countries.add(input().strip())
print(len(countries))