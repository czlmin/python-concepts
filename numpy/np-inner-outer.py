# https://www.hackerrank.com/challenges/np-inner-and-outer/problem?isFullScreen=true

import numpy

my_array1 = numpy.array([list(map(int, input().strip().split()))])
my_array2 = numpy.array([list(map(int, input().strip().split()))])

print(*numpy.inner(my_array1, my_array2)[0])
print(numpy.outer(my_array1, my_array2))
