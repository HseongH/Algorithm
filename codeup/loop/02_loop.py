f1, f2 = map(float, input().split())

while f1 <= f2:
    print('%.2f' % f1, end=' ')

    f1 += 0.01
