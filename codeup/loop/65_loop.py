n, m = map(int, input().split())

for i in range(m):
    if i == 0 or i == m - 1:
        print('+', end='')
        print('-' * (n - 2), end='')
        print('+')
        continue
    print('|', end='')
    print(' ' * (n - 2), end='')
    print('|')
