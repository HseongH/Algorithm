n, m = map(int, input().split())
arr = [[0 for _ in range(m)] for _ in range(n)]
num = 1

for i in range(n):
    for j in range(m, i + 1):
        arr[i][m - j] = num
        num += 1

for i in arr:
    for j in i:
        print(j, end=' ')
    print()
