# https://www.hackerrank.com/challenges/polar-coordinates/problem?isFullScreen=true

from cmath import phase

c_number = input()
print(abs(complex(c_number)))
print(phase(complex(c_number)))