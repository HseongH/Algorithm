from sys import stdin

n, k = map(int, stdin.readline().split())
arr = sorted(list(map(int, stdin.readline().split())))

print(arr[k - 1])
