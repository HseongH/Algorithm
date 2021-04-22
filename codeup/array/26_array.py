n, m = map(int, input().split())

for i in range(n):
    if (i + n) % 2 == 0:
        for j in range(m - 1, -1, -1):
            print(n * m - (j + m * i), end=' ')
        print()
        continue
    for j in range(m):
        print(n * m - (j + m * i), end=' ')
    print()
