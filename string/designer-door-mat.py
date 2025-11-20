# https://www.hackerrank.com/challenges/designer-door-mat/problem?isFullScreen=true

if __name__ == "__main__":
    N, M = map(int, input().split())   # N is rows (odd), M is columns (3*N)

    pattern_char = '.|.'
    fill_char = '-'

    # Top half (excluding middle line)
    for i in range(1, N, 2):
        pattern = pattern_char * i
        print(pattern.center(M, fill_char))

    # Middle line
    print("WELCOME".center(M, fill_char))

    # Bottom half (mirror of top)
    for i in range(N - 2, 0, -2):
        pattern = pattern_char * i
        print(pattern.center(M, fill_char))
