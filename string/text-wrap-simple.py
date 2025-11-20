# https://www.hackerrank.com/challenges/text-wrap/problem?isFullScreen=true

import textwrap

def wrap(string, max_width):
    new_string =  textwrap.wrap(string, max_width)
    new_text = ''
    for word in new_string:
        new_text += word
        new_text += '\n'
    return new_text

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
