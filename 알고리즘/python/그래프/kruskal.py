# 최소 신장 트리 (Minimum Spanning Tree, MST): 신장 트리 중에서 간선의 가중치의 합이 가장 작은 신장 트리를 말한다.
# 크루스칼 알고리즘 (Kruskal's algorithm): 최소 신장 트리를 구하는 대표적인 알고리즘
#   1. 모든 정점을 개별 집합으로 초기화한다.
#   2. 간선을 가중치 순서대로 정렬한다.
#   3. 가중치가 작은 간선 순으로 정점을 연결하는데, 사이클이 생긴다면 그 간선은 제외한다.
#   4. 모든 노드들이 연결될 때까지 3의 작업을 반복 수행한다.

# Union Find 알고리즘: 크루스칼 알고리즘에서 사이클 발생 여부를 확인하고 서로 다른 트리를 연결하는 알고리즘이다.
#   1. Union: 연결하려는 트리 중 하나의 트리의 루트 노드를 전체 트리의 루트 노드로 놓고 다른 트리를 그 루트 노드에 연결한다.
#   2. Find: 연결하려는 두 노드의 루트 노드를 비교해 서로 같다면 같은 트리로 간주하고 Union 작업을 수행하지 않는다.

# Union Find 알고리즘에서 고려할 점: 최악의 경우 O(N)의 시간 복잡도를 가진 링크드 리스트의 형태로 트리가 구성될 수 있다.
# 해결방법
#   1. union-by-rank
#       - 연결하려는 두 트리의 높이(rank)를 비교한다.
#           - 높이가 다르다면: 높이가 낮은 트리를 높은 트리의 루트 노드에 연결한다.
#           - 높이가 같다면: 두 트리 중 하나의 트리의 높이를 1증가 시키고 다른 트리를 그 트리의 루트 노드에 연결한다.
#   2. path compression
#       - find 로직을 수행한 노드들은 그 노드의 루트 노드에 직접 연결한다.
#       - 이후 같은 노드에 find 연산을 수행 시 그 노드의 루트 노드를 바로 찾을 수 있다.

class MinSpanningTree:
    def __init__(self):
        self.parent = dict()
        self.rank = dict()

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, node_v, node_u):
        v_root = self.parent[node_v]
        u_root = self.parent[node_u]

        if self.rank[v_root] > self.rank[u_root]:
            self.parent[u_root] = v_root
        else:
            self.parent[v_root] = u_root
            if self.rank[v_root] == self.rank[u_root]:
                self.rank[u_root] += 1

    def make_set(self, node):
        self.parent[node] = node
        self.rank[node] = 0

    def kruskal(self, graph):
        mst = list()

        for node in graph['vertices']:
            self.make_set(node)

        edges = graph['edges']
        edges.sort()

        for edge in edges:
            weight, node_v, node_u = edge

            if self.find(node_v) != self.find(node_u):
                self.union(node_v, node_u)
                mst.append(edge)

        return mst

# TEST CODE
graph = {
    'vertices': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
    'edges': [
        (7, 'A', 'B'),
        (5, 'A', 'D'),
        (7, 'B', 'A'),
        (8, 'B', 'C'),
        (9, 'B', 'D'),
        (7, 'B', 'E'),
        (8, 'C', 'B'),
        (5, 'C', 'E'),
        (5, 'D', 'A'),
        (9, 'D', 'B'),
        (7, 'D', 'E'),
        (6, 'D', 'F'),
        (7, 'E', 'B'),
        (5, 'E', 'C'),
        (7, 'E', 'D'),
        (8, 'E', 'F'),
        (9, 'E', 'G'),
        (6, 'F', 'D'),
        (8, 'F', 'E'),
        (11, 'F', 'G'),
        (9, 'G', 'E'),
        (11, 'G', 'F')
    ]
}

mst = MinSpanningTree()
print(mst.kruskal(graph))
