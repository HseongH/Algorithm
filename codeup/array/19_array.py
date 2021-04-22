n, m = map(int, input().split())
arr = [[j + ((i - 1) * m) for j in range(1, m + 1)] for i in range(n, 0, -1)]

for i in arr:
    for j in i:
        print(j, end=' ')
    print()
