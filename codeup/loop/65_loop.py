n, m = map(int, input().split())

print('+', end='')
print('-' * (n - 2), end='')
print('+')

for i in range(m):
    if i % 2 == 0:
        print()
        continue
    print('|', end='')
    print(' ' * (n - 2), end='')
    print('|')

print('+', end='')
print('-' * (n - 2), end='')
print('+')
