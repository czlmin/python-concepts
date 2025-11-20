# https://www.hackerrank.com/challenges/python-string-formatting/problem?isFullScreen=true

def print_formatted(number):
    # your code goes here
    width = len(f"{number:b}")

    for i in range(1, number+1):
        # print(i, oct(i)[2:], hex(i)[2:], bin(i)[2:])
        print(str(i).rjust(width), f"{i:o}".rjust(width), f"{i:X}".rjust(width), f"{i:b}".rjust(width))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
