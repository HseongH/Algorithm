# n = int(input())
# loop = (n - 2) // 2

# print('*' * n)

# for i in range(loop):
#     print('*', end='')
#     print(' ' * i, end='')
#     print('*', end='')
#     print(' ' * (n - 4 - (i * 2)), end='')
#     print('*', end='')
#     print(' ' * i, end='')
#     print('*')

# if n % 2 == 1:
#     print('*', end='')
#     print(' ' * loop, end='')
#     print('*', end='')
#     print(' ' * loop, end='')
#     print('*')

# for i in range(loop, 0, -1):
#     print('*', end='')
#     print(' ' * (i - 1), end='')
#     print('*', end='')
#     print(' ' * (n - 2 - (i * 2)), end='')
#     print('*', end='')
#     print(' ' * (i - 1), end='')
#     print('*')

# print('*' * n)

n = int(input())

print('*' * n)

for i in range(n - 2):
    for j in range(n):
        if j == 0 or j == n - 1 or j == i + 1 or j == n - 2 - i:
            print('*', end='')
            continue
        print(' ', end='')
    print()

print('*' * n)
