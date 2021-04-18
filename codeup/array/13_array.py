n = input()
arr = list(map(int, input().split()))

for i in range(len(arr)):
    print('%d:' % (i + 1), end=' ')
    for j in range(len(arr)):
        if i == j:
            continue
        if arr[i] > arr[j]:
            print('>', end=' ')
        elif arr[i] < arr[j]:
            print('<', end=' ')
        else:
            print('=', end=' ')
    print()
