n, m = map(int, input().split())

for i in range(n):
    for j in range(m):
        if (j + m) % 2 == 1:
            print(n * m - ((j + 1) * n) + (i + 1), end=' ')
            continue
        print(n * m - i - (j * n), end=' ')
    print()
