# https://www.hackerrank.com/challenges/collections-counter/problem?isFullScreen=true
from collections import Counter

X = int(input())
shoes = list(map(int, input().split()))
shoes_counts = Counter(shoes)
N = int(input())
shoe_purchase = []
sales = 0
for i in range(N):
    shoe_size, price = map(int, input().split())
    if shoe_size in shoes_counts.keys() and shoes_counts[shoe_size] > 0:
        sales += price
        shoes_counts[shoe_size] -= 1

print(sales)
