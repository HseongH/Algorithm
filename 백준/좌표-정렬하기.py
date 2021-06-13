import sys

n = int(sys.stdin.readline())
arr = sorted([list(map(int, sys.stdin.readline().split())) for _ in range(n)])

for item in arr:
    sys.stdout.write(' '.join(map(str, item)) + '\n')
