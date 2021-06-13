n, m = map(int, input().split())
cards = list(map(int, input().split()))
result = 0

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            point = cards[i] + cards[j] + cards[k]

            if point <= m:
                result = max(result, point)

print(result)
