n, m = map(int, input().split())
arr = [[0 for _ in range(m)] for _ in range(n)]
num = 0

for i in range(n + m - 1):
    for j in range(m):
        for k in range(n):
            if j + k == i:
                num += 1
                arr[k][m - j - 1] = num
                break

for i in arr:
    for j in i:
        print(j, end=' ')
    print()
