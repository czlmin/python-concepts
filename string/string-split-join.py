# https://www.hackerrank.com/challenges/python-string-split-and-join/problem?isFullScreen=true

def split_and_join(s):
    words = s.strip().split()
    return '-'.join(words)

def strip_replace(line):
    # write your code here
    return line.strip().replace(' ', '-')

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)