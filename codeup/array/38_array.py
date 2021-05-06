n, m = map(int, input().split())
arr = [[0 for i in range(m)] for i in range(n)]
num = 1
y = 0
i = 0
j = 0

while num <= n * m:
    arr[i][j] = num
    num += 1

    if i == y and j < m - 1:
        j += 1
    elif (i >= y and i < n - 1) and j == m - 1:
        i += 1
    elif i == n - 1 and (j > 0 and j <= m - 1):
        j -= 1
    elif i > y and j == 0:
        i -= 1

    if i == n - 1 and j == m - 1:
        y += 1

for i in arr:
    for j in i:
        print(j, end=' ')
    print()
