# https://www.hackerrank.com/challenges/np-concatenate/problem?isFullScreen=true

# import numpy
#
# array_1 = numpy.array([[1,2,3],[0,0,0]])
# array_2 = numpy.array([[0,0,0],[7,8,9]])
#
# print(numpy.concatenate((array_1, array_2), axis = 0))

import numpy

N, M, P = map(int, input().strip().split())
array1 = []
for _ in range(N):
    array1.append(list(map(int, input().strip().split())))
my_array1 = numpy.array(array1)
my_array1.reshape(N, P)
# print(my_array1)
array2 = []
for _ in range(M):
    array2.append(list(map(int, input().strip().split())))
my_array2 = numpy.array(array2)
my_array2.reshape(M, P)
# print(my_array2)

print(numpy.concatenate((my_array1, my_array2)))