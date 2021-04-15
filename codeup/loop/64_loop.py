for i in range(1, 10):
    for j in range(2, 6):
        if j == 5:
            print('%d x %d = %2d' % (j, i, j * i))
            continue
        print('%d x %d = %2d\t' % (j, i, j * i), end='')
