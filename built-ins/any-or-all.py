# https://www.hackerrank.com/challenges/any-or-all/problem?isFullScreen=true

N = int(input())
nums = list(map(int, input().split()))
if all(num > 0 for num in nums):
    print(any([num for num in nums if str(num) == str(num)[::-1]]))
else:
    print(False)