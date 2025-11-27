# https://www.hackerrank.com/challenges/python-print/problem?isFullScreen=true

if __name__ == '__main__':
    n = int(input())

    s = ""
    for i in range(n):
        i += 1
        s += str(i)

    print(s)