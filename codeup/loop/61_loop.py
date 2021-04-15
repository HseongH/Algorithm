n = int(input())

for i in range(n):
    print(' ' * (n - (i + 1)), end='')
    print('*', end='')
    print(' ' * (i * 2), end='')
    print('*')

for i in range(n - 1, -1, -1):
    print(' ' * (n - (i + 1)), end='')
    print('*', end='')
    print(' ' * (i * 2), end='')
    print('*')
