from sys import stdin
from heapq import heappush, heappop
input = stdin.readline

n = int(input())
heap = list()

for _ in range(n):
    command = int(input())

    if command == 0:
        print(-heappop(heap)) if heap else print(0)
        continue
    heappush(heap, -command)
