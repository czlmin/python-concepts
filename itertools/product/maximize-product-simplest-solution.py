from itertools import product

def main():
    K, M = map(int, input().split())
    lists = []
    for _ in range(K):
        data = list(map(int, input().split()))
        lists.append(data[1:])  # skip the first number (length)

    # Precompute squares modulo M to keep numbers small
    lists_mod = [[(x * x) % M for x in lst] for lst in lists]

    best = 0
    for combo in product(*lists_mod):
        best = max(best, sum(combo) % M)

    print(best)

if __name__ == "__main__":
    main()
