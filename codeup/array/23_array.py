n = int(input())

for i in range(n):
    if i % 2 == 1:
        for j in range(1, n + 1):
            print(j + i * n, end=' ')
        print()
        continue
    for j in range(n, 0, -1):
        print(j + i * n, end=' ')
    print()
