n = int(input())

for i in range(n, 0, -1):
    for j in range(n):
        if j % 2 == 1:
            print((j + 1) * n - i + 1, end=' ')
            continue
        print((j * n) + i, end=' ')
    print()
