n = int(input())

print('*' * n)

for i in range(1, n - 1):
    print('*', end='')
    print(' ' * (n - 2), end='')
    print('*')

print('*' * n)
