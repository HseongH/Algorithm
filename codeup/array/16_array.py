n = int(input())

arr = [[j + 1 + i for j in range(0, n * n, n)] for i in range(n)]

for i in arr:
    for j in i:
        print(j, end=' ')
    print()
