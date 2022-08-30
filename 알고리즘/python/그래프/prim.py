# 프림 알고리즘 (Prim's algorithm)
# 크루스칼 알고리즘과 같이 최소 신장 트리를 구성하는 대표적인 알고리즘이다.

# 시작 노드를 정하고 그 노드에 연결되어 있는 간선 중 가중치가 가장 작은 간선을 선택해 연결한다.
# 지금까지 연결된 노드의 간선 중 사이클이 생기지 않고 가중치가 작은 간선을 선택해 연결한다.
#   사이클 발생 여부 확인: 연결된 노드 집합을 만들고, 연결하고자 하는 간선의 인접 노드가 연결된 노드 집합에 있는 지 확인해 없다면 간선을 연결한다.

from heapq import *
from collections import defaultdict

def basic_prim(edges, start_node):
    mst, adjacent_edges = list(), defaultdict(list)

    for weight, n1, n2 in edges:
        adjacent_edges[n1].append((weight, n1, n2))
        adjacent_edges[n2].append((weight, n2, n1))

    connected_nodes, candidate_edge_list = set(start_node), adjacent_edges[start_node]
    heapify(candidate_edge_list)

    while candidate_edge_list:
        weight, n1, n2 = heappop(candidate_edge_list)

        if n2 not in connected_nodes:
            connected_nodes.add(n2)
            mst.append((weight, n1, n2))

            for edge in adjacent_edges[n2]:
                if edge[2] not in connected_nodes:
                    heappush(candidate_edge_list, edge)

    return mst

# TEST CODE
edges = [
    (7, 'A', 'B'), (5, 'A', 'D'),
    (8, 'B', 'C'), (9, 'B', 'D'), (7, 'B', 'E'),
    (5, 'C', 'E'),
    (7, 'D', 'E'), (6, 'D', 'F'),
    (8, 'E', 'F'), (9, 'E', 'G'),
    (11, 'F', 'G')
]

print(basic_prim(edges, 'A'))

# 개선된 프림 알고리즘
# 기본 프림 알고리즘은 간선을 중심으로 mst를 구성하기 때문에 시간 복잡도가 (E log E)이다.
# 그래프에서 간선의 수가 정점(노드)의 수보다 더 많은 경우가 빈번하기 때문에 정점(노드)를 중심으로 mst를 구성하면 시간 복잡도를 (E log V)로 줄여볼 수 있다.

from heapdict import heapdict

def prim(graph, start_node):
    mst, keys, pi, total_weight = list(), heapdict(), dict(), 0

    for node in graph:
        keys[node] = float('inf')
        pi[node] = None

    keys[start_node], pi[start_node] = 0, start_node

    while keys:
        current_node, current_weight = keys.popitem()
        mst.append([pi[current_node], current_node, current_weight])
        total_weight += current_weight

        for adjacent, weight in graph[current_node].items():
            if adjacent in keys and weight < keys[adjacent]:
                keys[adjacent] = weight
                pi[adjacent] = current_node

    return mst, total_weight

# TEST CODE
mygraph = {
    'A': {'B': 7, 'D': 5},
    'B': {'A': 7, 'D': 9, 'C': 8, 'E': 7},
    'C': {'B': 8, 'E': 5},
    'D': {'A': 5, 'B': 9, 'E': 7, 'F': 6},
    'E': {'B': 7, 'C': 5, 'D': 7, 'F': 8, 'G': 9},
    'F': {'D': 6, 'E': 8, 'G': 11},
    'G': {'E': 9, 'F': 11}    
}

mst, total_weight = prim(mygraph, 'A')
print ('MST:', mst)
print ('Total Weight:', total_weight)  
