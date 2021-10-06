from sys import stdin

input = stdin.readline

arr = [int(input()) for _ in range(9)]
overflow = sum(arr) - 100

for i in range(8):
    if arr[i] > overflow:
        continue

    for j in range(i + 1, 9):
        if (arr[i] + arr[j] == overflow):
            arr = sorted(list(filter(lambda x: x != arr[i] and x != arr[j], arr)))
            break

    if (len(arr) == 7):
        break

print(*arr, sep='\n')
