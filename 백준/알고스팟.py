from heapq import heappush, heappop

m, n = map(int, input().split())
maze = [list(map(int, input())) for _ in range(n)]

# 상하좌우 탐색을 위한 리스트
search_x = [1, -1, 0, 0]
search_y = [0, 0, 1, -1]
# 한 번 방문한 곳 체크
visited = [[0 for _ in range(m)] for _ in range(n)]

que = []
heappush(que, (0, 0, 0))

while que:
    weight, y, x = heappop(que)

    if y == n - 1 and x == m - 1:
        print(weight)
        break

    for i in range(4):
        pos_y, pos_x = y + search_y[i], x + search_x[i]

        # 리스트에서 유효한 인덱스인지 체크
        if 0 <= pos_y < n and 0 <= pos_x < m and visited[pos_y][pos_x] == 0:
            # 이동할 곳이 벽이라면 가중치를 1 더해서 탐색 순서를 뒤로 미룸
            heappush(que, (weight + 1 if maze[pos_y][pos_x] == 1 else weight, pos_y, pos_x))
            visited[pos_y][pos_x] = 1
