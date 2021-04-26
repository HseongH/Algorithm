n, m = map(int, input().split())
arr = [[0 for _ in range(m)] for _ in range(n)]
num1 = 1
num2 = n * m

for i in range(n):
    for j in range(i, -1, -1):
        arr[j][i - j] = num1
        arr[n - j - 1][m - (i - j) - 1] = num2
        num1 += 1
        num2 -= 1

for i in arr:
    for j in i:
        print(j, end=' ')
    print()
