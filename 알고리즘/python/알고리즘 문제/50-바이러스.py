from sys import stdin
from collections import deque, defaultdict
input = stdin.readline

def bfs(graph, start_node):
    need_visit, visited = deque([start_node]), dict()

    while need_visit:
        key = need_visit.popleft()

        if key not in visited:
            visited[key] = 0
            need_visit.extend(graph[key])

    print(len(visited) - 1)

def create_graph(temp):
    graph = defaultdict(list)

    for item in temp:
        graph[item[0]].append(item[1])
        graph[item[1]].append(item[0])

    return graph

v, edge = int(input()), int(input())
graph = create_graph([list(map(int, input().split())) for _ in range(edge)])

bfs(graph, 1)
