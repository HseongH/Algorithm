n, m = map(int, input().split())
arr = [[0 for _ in range(m)] for _ in range(n)]
num = 0

for i in range(n + m - 1):
    for j in range(n):
        for k in range(m):
            if j + k == i:
                num += 1
                arr[n - j - 1][m - k - 1] = num
                break

for i in arr:
    for j in i:
        print(j, end=' ')
    print()
