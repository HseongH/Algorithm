n, m = map(int, input().split())
arr = [[0 for _ in range(m)] for _ in range(n)]
x = 0
y = 0
size = 0
num = 1

while num <= n:
    for j in range(m - size):
        arr[y][j] = num
        num += 1
        x = j

    y = 0
    
    size += 1

    for i in range(n - size):
        arr[i][x] = num
        num += 1
        y = i

    x = 0

for i in arr:
    for j in i:
        print(j, end=' ')
    print()
