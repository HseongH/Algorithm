n, m = map(int, input().split())
arr = [[0 for _ in range(m)] for _ in range(n)]
cnt = 1

for i in range(n + m - 1):
    for x in range(m):
        for y in range(n):
            if x + y == i:
                arr[y][x] = cnt
                cnt += 1

for i in arr:
    for j in i:
        print(j, end=' ')
    print()
