n = int(input())
loop = (n - 3) // 2

print('*' * n)

for i in range(loop):
    print('*', end='')
    print(' ' * i, end='')
    print('*', end='')
    print(' ' * (n - 4 - (i * 2)), end='')
    print('*', end='')
    print(' ' * i, end='')
    print('*')

print('*', end='')
print(' ' * loop, end='')
print('*', end='')
print(' ' * loop, end='')
print('*')

for i in range(loop - 1, -1, -1):
    print('*', end='')
    print(' ' * i, end='')
    print('*', end='')
    print(' ' * (n - 4 - (i * 2)), end='')
    print('*', end='')
    print(' ' * i, end='')
    print('*')


print('*' * n)
