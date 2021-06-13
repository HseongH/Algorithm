import sys

n = int(sys.stdin.readline())
arr = sorted([sys.stdin.readline().split() for _ in range(n)], key=lambda x: int(x[0]))

for item in arr:
    sys.stdout.write(' '.join(map(str, item)) + '\n')
