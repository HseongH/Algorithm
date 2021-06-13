from sys import stdin
from collections import defaultdict

n = int(stdin.readline())
k = int(stdin.readline())

arr = defaultdict(int)

idx = 0

for i in range(1, n + 1):
    for j in range(1, n + 1):
        arr[i * j] += 1

for key, value in arr.items():
    idx += value
    if idx >= k:
        print(key)
        break
