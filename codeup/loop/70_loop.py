n, k = map(int, input().split())

for i in range(n):
    for j in range(n):
        if j == 0 or j == n - 1 or (j + 1 + i) % k == 0 or i == 0 or i == n - 1:
            print('*', end='')
            continue
        print(' ', end='')
    print()
