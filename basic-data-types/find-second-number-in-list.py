# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    s_arr = set(arr)
    sorted_arr = sorted(s_arr, reverse=True)
    if len(sorted_arr) > 1:
        print(sorted_arr[1])
