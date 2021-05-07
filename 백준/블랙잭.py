n, m = map(int, input().split())
count = list(map(int, input().split()))
result = []

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            sum = count[i] + count[j] + count[k]
            if sum <= m:
                result.append(sum)

print(max(result))
