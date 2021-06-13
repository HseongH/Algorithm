import sys

arr = list(sys.stdin.readline().strip())

arr.sort(reverse=True)

sys.stdout.write(''.join(arr))
