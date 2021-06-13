from collections import defaultdict, deque

def bfs(graph, start):
    need_visit, visited = deque([start]), list()

    while need_visit:
        node = need_visit.popleft()

        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])
            
    return len(visited) - 1

def create_graph(temp):
    graph = defaultdict(list)

    for i in range(p):
        graph[temp[i][0]].append(temp[i][1])
        graph[temp[i][1]].append(temp[i][0])

    return graph

n = int(input())
p = int(input())
graph = create_graph([list(map(int, input().split())) for _ in range(p)])

print(bfs(graph, 1))
