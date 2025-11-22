from collections import Counter

if __name__ == "__main__":
    _ = int(input())  # number of shoes (unused directly)
    shoes = Counter(map(int, input().split()))

    n_customers = int(input())
    earnings = 0

    for _ in range(n_customers):
        size, price = map(int, input().split())
        if shoes[size] > 0:  # shoe available
            earnings += price
            shoes[size] -= 1  # reduce stock

    print(earnings)
