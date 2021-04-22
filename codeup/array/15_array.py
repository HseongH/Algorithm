n = int(input())
arr = [[j + (n * i) for j in range(n, 0, -1)] for i in range(n)]

for i in arr:
    for j in i:
        print(j, end=' ')
    print()
