# https://www.hackerrank.com/challenges/zipped/problem?isFullScreen=true

# A = [1,2,3]
# B = [6,5,4]
# C = [7,8,9]
# X = [A] + [B] + [C]
#
# print(X)
# print(*X)
#
# scores = (1, 6, 7)
# print(sum(scores) / len(scores))

N, X = map(int, input().split())
scores = []
for _ in range(X):
    score = list(map(float, input().split()))
    scores.append(score)

# print(scores)
zipped_scores = list(zip(*scores))
# print(zipped_scores)
for i in range(N):
    print(f"{sum(zipped_scores[i]) / len(zipped_scores[i]):.1f}")
