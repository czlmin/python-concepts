# https://www.hackerrank.com/challenges/alphabet-rangoli/problem?isFullScreen=true
import string

def print_rangoli(size):
    # your code goes here
    s = string.ascii_lowercase[:size]
    fill_char = '-'
    width = 4*size - 3
    # print(s)

    # # Top half (excluding middle line)
    for i in range(1, size):
        line = s[::-1][0:i]+s[size-i+1:size]
        line = "-".join(line)
        print(line.center(width, fill_char))
    line = s[::-1][0:size]+s[1:size]
    line = "-".join(line)
    print(line.center(width, fill_char))
    for i in range(size-1, 0, -1):
        line = s[::-1][0:i]+s[size-i+1:size]
        line = "-".join(line)
        print(line.center(width, fill_char))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)