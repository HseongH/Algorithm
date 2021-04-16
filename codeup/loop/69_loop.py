n = int(input())

print('*' * n)

for i in range(n - 2):
    for j in range(n):
        if j == 0 or j == n - 1 or (i + 2) == (n // 2 + 1) or j == (n // 2) or j - 1 == i or j == n - 2 - i:
            print('*', end='')
            continue
        print(' ', end='')
    print()

print('*' * n)
