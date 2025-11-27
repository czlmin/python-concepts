# https://www.hackerrank.com/challenges/incorrect-regex/problem?isFullScreen=true

import re

if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        pattern = input().strip()
        try:
            # Emulate CPython's "multiple repeat" error:
            # reject any run of 2+ of *, +, ? in a row, e.g. ".*+"
            if re.search(r'(\*|\+|\?){2,}', pattern):
                print(False)
            else:
                re.compile(pattern)
                print(True)
        except re.error:
            print(False)
