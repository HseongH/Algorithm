from sys import stdin
from collections import deque

input = stdin.readline

n = int(input())
que = deque()

for _ in range(n):
    command = input().split()

    if command[0] == 'push':
        que.append(command[1])
        continue
    elif command[0] == 'pop':
        print(que.popleft()) if que else print(-1)
        continue
    elif command[0] == 'size':
        print(len(que))
        continue
    elif command[0] == 'empty':
        print(int(len(que) == 0))
        continue
    elif command[0] == 'front':
        print(que[0]) if que else print(-1)
        continue
    elif command[0] == 'back':
        print(que[-1]) if que else print(-1)
