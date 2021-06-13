from collections import deque
from copy import deepcopy

r, c, t = map(int, input().split())
arr = [list(input()) for _ in range(r)]
arr2 = deepcopy(arr)
count = 0
result = list()

for i in range(r):
    if 'G' in arr[i]:
        y, x = i, arr[i].index('G')
        break

search_x, search_y = [1, -1, 0, 0], [0, 0, 1, -1]
visited = [[-1] * c for _ in range(r)]

visited[y][x] = 0
queue = deque()
queue.append([y, x])

while queue:
    y, x = queue.popleft()

    if visited[y][x] == t: break
    
    for i in range(4):
        ny, nx = y + search_y[i], x + search_x[i]

        if 0 <= ny < r and 0 <= nx < c and arr2[ny][nx] != '#':
            if visited[ny][nx] == -1:
                visited[ny][nx] = visited[y][x] + 1
                queue.append([ny, nx])
            if arr2[ny][nx] == 'S':
                arr2[ny][nx] = '.'
                count += 1

    arr2 = deepcopy(arr)
    result.append(count)
    count = 0

print(max(result))
 