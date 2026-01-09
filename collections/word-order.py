# https://www.hackerrank.com/challenges/word-order/problem?isFullScreen=true

from collections import Counter

n = int(input())
words = []
for i in range(n):
    words.append(input())

feq = Counter(words)
print(len(feq))
s1 = [str(feq[word]) for word in feq.keys()]
# s2 = ' '.join(s1)
# print(s2)
print(*s1)
# print(*s1, ' ')