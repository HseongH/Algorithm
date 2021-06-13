from collections import deque

n, m = map(int, input().split())
maze = [list(map(int, input())) for _ in range(n)]

visited = [[0] * m for _ in range(n)]
visited[0][0] = 1

search_y, search_x = [0, 0, -1, 1], [-1, 1, 0, 0]

queue = deque([[0, 0]])

while queue:
    y, x = queue.popleft()

    if y == n - 1 and x == m - 1:
        print(visited[y][x])
        break

    for i in range(4):
        move_y, move_x = y + search_y[i], x + search_x[i]

        if 0 <= move_y < n and 0 <= move_x < m and maze[move_y][move_x] == 1:
            if visited[move_y][move_x] == 0:
                visited[move_y][move_x] = visited[y][x] + 1
                queue.append([move_y, move_x])
