n = int(input())

for i in range(n):
    for j in range(n):
        if j % 2 == 1:
            print((j + 1) * n - i, end=' ')
            continue
        print((j * n) + i + 1, end=' ')
    print()
