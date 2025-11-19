# https://www.hackerrank.com/domains/python?filters%5Bsubdomains%5D%5B%5D=py-sets

T = int(input())
for i in range(T):
    n = int(input())
    A = set(map(int, input().split()))
    m = int(input())
    B = set(map(int, input().split()))

    if len(A - B) == 0:
        print('True')
    else:
        print('False')