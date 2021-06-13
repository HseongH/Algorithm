import sys

n = sys.stdin.readline()
arr1 = set(map(int, sys.stdin.readline().split()))
m = sys.stdin.readline()
arr2 = list(map(int, sys.stdin.readline().split()))

for item in arr2:
    if item in arr1:
        sys.stdout.write('1\n')
    else:
        sys.stdout.write('0\n')
