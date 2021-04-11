a, b = map(int, input().split())

if a < b:
    a, b = b, a

print('%d*%d=%d' % (b, a // b, a)) if a % b == 0 else print('none')
