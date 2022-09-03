from sys import stdin
from collections import deque, defaultdict

input = stdin.readline

def dfs(graph, start):
    need_visit, visited = list([start]), dict()

    while need_visit:
        key = need_visit.pop()

        if key not in visited:
            visited[key] = 0
            need_visit.extend(sorted(graph[key], reverse=True))

    print(' '.join(map(str, visited)))

def bfs(graph, start):
    need_visit, visited = deque([start]), dict()

    while need_visit:
        key = need_visit.popleft()

        if key not in visited:
            visited[key] = 0
            need_visit.extend(sorted(graph[key]))

    print(' '.join(map(str, visited)))

def create_graph(temp):
    graph = defaultdict(list)

    for item in temp:
        graph[item[0]].append(item[1])
        graph[item[1]].append(item[0])

    return graph

v, edge, start_node = map(int, input().split())
graph = create_graph([list(map(int, input().split())) for _ in range(edge)])

dfs(graph, start_node)
bfs(graph, start_node)
