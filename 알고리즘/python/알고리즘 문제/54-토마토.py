from sys import stdin
from collections import deque
input = stdin.readline

m, n = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(n)]
result = 0

dy, dx = [-1, 1, 0, 0], [0, 0, 1, -1]

que = deque()

for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            que.append((i, j))

if not que:
    print(-1)
    exit()

while que:
    y, x = que.popleft()

    for i in range(4):
        pos_y, pos_x = y + dy[i], x + dx[i]

        if 0 <= pos_y < n and 0 <= pos_x < m and box[pos_y][pos_x] == 0:
            box[pos_y][pos_x] = box[y][x] + 1
            result = box[pos_y][pos_x] - 1
            que.append((pos_y, pos_x))

for item in box:
    if 0 in item:
        print(-1)
        exit()

print(result)
