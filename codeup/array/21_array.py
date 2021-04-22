n, m = map(int, input().split())
arr = [[(j - i) + 1 for j in range(n * m, 0, -n)] for i in range(n, 0, -1)]

for i in arr:
    for j in i:
        print(j, end=' ')
    print()
