n = int(input())
arr = list(map(int, input().split()))
arr = list(reversed(arr))

for i in arr:
    print(i, end=' ')
