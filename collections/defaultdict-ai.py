from collections import defaultdict

if __name__ == "__main__":
    n, m = map(int, input().split())

    groups = defaultdict(list)

    # Read Group A words and store their positions
    for i in range(1, n + 1):
        word = input().strip()
        groups[word].append(i)

    # For each Group B word, print indices or -1
    for _ in range(m):
        word = input().strip()
        if groups[word]:
            print(*groups[word])
        else:
            print(-1)
