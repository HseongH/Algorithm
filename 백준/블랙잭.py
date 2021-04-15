n, m = map(int, input().split())
card = list(map(int, input().split()))
score = []

for i in card:
    for j in card:
        if i == j:
            continue
        for k in card:
            if j == k or i == k:
                continue

            total = i + j + k

            if m - total >= 0:
                score.append(total)

print(max(score))
