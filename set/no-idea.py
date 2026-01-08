# https://www.hackerrank.com/challenges/no-idea/problem?isFullScreen=true

n, m = map(int, input().split())
l = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))

happiness = 0
for i in l:
    if i in A:
        happiness += 1
    elif i in B:
        happiness -= 1
print(happiness)