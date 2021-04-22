n, m = map(int, input().split())

for i in range(n):
    if (n + i) % 2 == 0:
        for j in range(m):
            print(n * m - (j + (i * m)), end=' ')
        print()
        continue
    for j in range(m - 1, -1, -1):
        print(n * m - (j + (i * m)), end=' ')
    print()
