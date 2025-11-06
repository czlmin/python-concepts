#
# A = input().split()
# B = input().split()
#
# op = []
# for i in A:
#     for j in B:
#         product = str((i, j))
#         op.append(product)
#
# ostr = " ".join(op)
# print(ostr)

from itertools import product

if __name__ == "__main__":
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    print(A, B)

    result = product(A, B)
    print(*result)