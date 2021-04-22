n, m = map(int, input().split())
arr = [[j - i for j in range(n * m, 0, -n)] for i in range(n)]

for i in arr:
    for j in i:
        print(j, end=' ')
    print()
