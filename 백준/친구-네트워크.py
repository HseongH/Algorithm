import sys

def find(f):
    if f != parent[f]:
        parent[f] = find(parent[f])
    return parent[f]

def union(f, s):
    f, s = find(f), find(s)

    if f != s:
        parent[s] = f
        network[f] += network[s]

test_case = int(sys.stdin.readline())

for _ in range(test_case):
    n = int(sys.stdin.readline())
    parent, network = dict(), dict()

    for _ in range(n):
        f, s = sys.stdin.readline().split()

        if f not in parent:
            parent[f] = f
            network[f] = 1
        if s not in parent:
            parent[s] = s
            network[s] = 1

        union(f, s)
        sys.stdout.write(str(network[parent[f]]) + '\n')
