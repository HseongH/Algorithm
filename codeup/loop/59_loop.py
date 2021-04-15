h, k, d = input().split()
h, k = int(h), int(k)

if d == 'L':
    for i in range(h):
        print(' ' * i, end='')
        print('*' * k)
else:
    for i in range(h - 1, -1, -1):
        print(' ' * i, end='')
        print('*' * k)
