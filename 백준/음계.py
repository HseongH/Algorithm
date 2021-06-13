scale = list(map(int, input().split()))
ascending = True
descending = True

for i in range(len(scale) - 1):
    if scale[i] > scale[i + 1]:
        ascending = False
    elif scale[i] < scale[i + 1]:
        descending = False

if ascending:
    print('ascending')
elif descending:
    print('descending')
else:
    print('mixed')
