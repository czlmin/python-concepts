# https://www.hackerrank.com/challenges/find-angle/problem?isFullScreen=true

import math


def find_theta(a, b):
    c = (a ** 2 + b ** 2) ** 0.5
    angle = math.degrees(math.asin(a / c))
    angle = round(angle)

    return angle


a = float(input())
b = float(input())
print(str(find_theta(a, b)) + "\N{DEGREE SIGN}")
