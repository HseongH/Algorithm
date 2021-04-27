n, m = map(int, input().split())
arr = [[0 for i in range(m)] for i in range(n)]
num = 0

for i in range(n):
    for j in range(m):
        num += 1
        arr[i][j] = num

for i in arr:
    for j in i:
        print(j, end=' ')
    print()
