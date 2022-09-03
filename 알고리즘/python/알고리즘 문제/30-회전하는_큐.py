from sys import stdin
from collections import deque

input = stdin.readline

n, m = map(int, input().split())
que = deque([i for i in range(1, n + 1)])
numbers = list(map(int, input().split()))
count = 0

for num in numbers:
    while que[0] != num:
        idx = que.index(num)

        que.rotate(-1) if idx <= len(que) // 2 else que.rotate()
        count += 1
    que.popleft()

print(count)
