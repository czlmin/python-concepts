# https://www.hackerrank.com/challenges/python-tuples/problem?isFullScreen=true
# Python 2 to run in HackerRank

n = int(input())
numbers = tuple(map(int, input().split()))
print(hash(numbers))