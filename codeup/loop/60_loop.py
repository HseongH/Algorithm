h, r = map(int, input().split())

for i in range(r):
    for j in range(h):
        print(' ' * j, end='')
        print('*')
    for j in range(h - 2, -1, -1):
        print(' ' * j, end='')
        print('*')
