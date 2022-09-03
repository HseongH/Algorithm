from sys import stdin
from collections import deque
input = stdin.readline

n = int(input())
apartment = [list(input()) for _ in range(n)]

dy, dx = [-1, 1, 0, 0], [0, 0, 1, -1]
result = list()

def dfs(i, j):
    que = deque()
    que.append((i, j))
    apartment[i][j] = '0'
    count = 1

    while que:
        y, x = que.popleft()

        for i in range(4):
            pos_y, pos_x = y + dy[i], x + dx[i]

            if 0 <= pos_y < n and 0 <= pos_x < n and apartment[pos_y][pos_x] == '1':
                que.append((pos_y, pos_x))
                apartment[pos_y][pos_x] = '0'
                count += 1

    result.append(count)

for i in range(n):
    for j in range(n):
        if apartment[i][j] == '1':
            dfs(i, j)

result.sort()
print(len(result))
print(*result, sep='\n')
