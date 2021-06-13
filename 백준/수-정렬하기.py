import sys

n = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for _ in range(n)]

for i in range(n - 1):
    swap = False
    
    for j in range(n - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            swap = True

    if not swap:
        break

sys.stdout.write('\n'.join(map(str, arr)))
