n = int(input())
heights = list(map(int, input().split()))

if sum(heights) % 3 != 0:
    print('NO')
else:
    date = 0

    for height in heights:
        date += height // 2

    if date >= sum(heights) // 3:
        print('YES')
    else:
        print('NO')
