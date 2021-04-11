arr = list(map(int, input().split()))
condition = [
    arr[0] <= 170,
    arr[1] <= 170,
    arr[2] <= 170
]

if True in condition:
    crash = arr[condition.index(True)]
    print('CRASH %d' % crash)
else:
    print('PASS')
