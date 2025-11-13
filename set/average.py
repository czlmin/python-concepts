# https://www.hackerrank.com/challenges/py-introduction-to-sets/problem?isFullScreen=true
# Basically, sets are used for membership testing and eliminating duplicate entries.

def average(array):
    # your code goes here
    heights = set(array)
    n = len(heights)
    sum_heights = sum(heights)
    ave = round(sum_heights / n, 3)

    return ave


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)