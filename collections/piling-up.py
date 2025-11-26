# https://www.hackerrank.com/challenges/piling-up/problem?isFullScreen=true

from collections import deque

def piling_up(blocks):
    d = deque(map(int, blocks))
    top = float('inf')          # nothing on stack yet; any first pick allowed

    while d:
        left, right = d[0], d[-1]
        pick = None

        # Prefer the larger end; it gives more room for future picks
        if max(left, right) <= top:
            if left >= right:
                pick = d.popleft()
            else:
                pick = d.pop()
        else:
            return "No"

        top = pick

    return "Yes"