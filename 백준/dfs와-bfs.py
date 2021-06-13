from collections import defaultdict, deque

def dfs(graph, start_node):
    need_visit, visited = list([start_node]), dict()

    while need_visit:
        node = need_visit.pop()

        if node not in visited:
            visited.setdefault(node)
            graph[node].sort(reverse=True)
            need_visit.extend(graph[node])
    
    return ' '.join(list(map(str, visited)))

def bfs(graph, start_node):
    need_visit, visited = deque([start_node]), dict()

    while need_visit:
        node = need_visit.popleft()

        if node not in visited:
            visited.setdefault(node)
            graph[node].sort()
            need_visit.extend(graph[node])
    
    return ' '.join(list(map(str, visited)))

def createGraph(temp):
    graph = defaultdict(list)

    for i in range(edge):
        graph[temp[i][0]].append(temp[i][1])
        graph[temp[i][1]].append(temp[i][0])

    return graph

vertex, edge, start = map(int, input().split())
graph = createGraph([list(map(int, input().split())) for _ in range(edge)])

print(dfs(graph, start))
print(bfs(graph, start))
