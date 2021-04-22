n = int(input())

arr = [[j + 1 + (i - 1) for j in range(0, n * n, n)] for i in range(n, 0, -1)]

for i in arr:
    for j in i:
        print(j, end=' ')
    print()
