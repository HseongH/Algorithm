a, b = map(int, input().split())
sum = 0

if a % 2 == 1:
    print(a, end='')
    sum += a
else:
    print('-%d' % a, end='')
    sum -= a

for i in range(a + 1, b + 1):
    if i % 2 == 0:
        sum -= i
        print('-%d' % i, end='')
    else:
        sum += i
        print('+%d' % i, end='')

print('=%d' % sum)
