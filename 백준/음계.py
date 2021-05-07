arr = list(map(int, input().split()))

ascending = True
descending = True

for i in range(len(arr) - 1):
    if arr[i] < arr[i + 1]:
        descending = False
    if arr[i] > arr[i + 1]:
        ascending = False

if ascending:
    print('ascending')
elif descending:
    print('descending')
else:
    print('mixed')
