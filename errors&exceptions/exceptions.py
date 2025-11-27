# https://www.hackerrank.com/challenges/exceptions/problem?isFullScreen=true

n = int(input())
for i in range(n):
    a, b = input().split()
    try:
        result = int(a) // int(b)
        print(result)
    except Exception as e:
        print(f"Error Code: {e}")