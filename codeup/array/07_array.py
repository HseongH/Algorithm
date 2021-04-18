n = int(input())
arr = [None] * n

for _ in range(n - 1):
    value = int(input())
    arr[value - 1] = value

print(arr.index(None) + 1)
