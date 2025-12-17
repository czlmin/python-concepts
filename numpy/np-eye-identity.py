# https://www.hackerrank.com/challenges/np-eye-and-identity/problem?isFullScreen=true

import numpy

numpy.set_printoptions(legacy='1.13')

N, M = map(int, input().strip().split())
print(numpy.eye(N, M))