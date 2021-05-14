# 다익스트라 알고리즘
# 그래프의 최단 경로 알고리즘 중 단일 출발 최단 경로 문제의 해를 찾는 알고리즘이다.
# 우선순위 큐를 이용한 알고리즘이다.

import heapq

def dijkstra(graph, start_node):
    distances = {node: float('inf') for node in graph}
    distances[start_node] = 0

    queue = list()
    heapq.heappush(queue, [distances[start_node], start_node])

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if distances[current_node] < current_distance:
            continue

        for node, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[node]:
                distances[node] = distance
                heapq.heappush(queue, [distance, node])

    return distances

# TEST CODE
graph = {
    'A': {'B': 8, 'C': 1, 'D': 2},
    'B': {},
    'C': {'B': 5, 'D': 2},
    'D': {'E': 3, 'F': 5},
    'E': {'F': 1},
    'F': {'A': 5}
}

print(dijkstra(graph, 'A'))
