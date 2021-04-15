a, b = map(int, input().split())

for i in range(a, b + 1):
    for j in range(1, 10):
        print('%d*%d=%d' % (i, j, i * j))
