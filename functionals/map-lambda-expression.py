# https://www.hackerrank.com/challenges/map-and-lambda-expression/problem?isFullScreen=true

cube = lambda x: x ** 3

def fibonacci(n):
    # return a list of fibonacci numbers
    if n == 0:
        return []
    if n == 1:
        return [0]
    fib = [0, 1]
    for i in range(2, n):
        c = fib[i-2] + fib[i-1]
        fib.append(c)
    return fib

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))