import sys
from collections import deque

test_case = int(sys.stdin.readline())

for _ in range(test_case):
    n, idx = map(int, sys.stdin.readline().split())
    important = list(map(int, sys.stdin.readline().split()))
    important = deque((key, i) for i, key in enumerate(important))
    count = 1

    while True:
        if important[0][0] == max(important)[0]:
            if important[0][1] == idx:
                print(count)
                break
            important.popleft()
            count += 1
        else:
            important.append(important.popleft())
