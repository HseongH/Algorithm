from sys import stdin

input = stdin.readline

n, m = map(int, input().split())
cards = list(map(int, input().split()))
result = 0

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            total_point = cards[i] + cards[j] + cards[k]
            if total_point <= m:
                result = max(result, total_point)

print(result)
