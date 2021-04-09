arr = list(map(int, input().split()))
n = len(arr)

for i in range(n -1):
    for j in range(n - 1, i, -1):
        if arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]

print(arr[0], arr[1], arr[2])
