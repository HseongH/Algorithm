# 너비 우선 탐색(Breadth-first Search)
# 정점들과 같은 위치에 있는 정점들(형제 노드)을 우선 탐색하는 기법

def bfs(graph, start_node):
    need_visit, visited = list(), list()
    need_visit.append(start_node)

    while need_visit:
        node = need_visit.pop(0)

        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])

    return visited

graph = dict()

graph['A'] = ['B', 'C']
graph['B'] = ['A', 'D']
graph['C'] = ['A', 'G', 'H', 'I']
graph['D'] = ['B', 'E', 'F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C', 'J']
graph['J'] = ['I']

print(bfs(graph, 'A'))
