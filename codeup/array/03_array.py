n = input()
arr = input().split()

for _ in range(len(arr)):
    for i in arr:
        print(i, end=' ')
    print()
    arr.append(arr[0])
    del arr[0]
