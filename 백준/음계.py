inp = list(map(int, input().split()))

if inp[0] == 1:
    for i, scale in enumerate(inp):
        try:
            if scale + 1 != inp[i + 1]:
                print('mixed')
                break
        except IndexError:
            pass
    else:
        print('ascending')
elif inp[0] == 8:
    for i, scale in enumerate(inp):
        try:
            if scale - 1 != inp[i + 1]:
                print('mixed')
                break
        except IndexError:
            pass
    else:
        print('descending')
else:
    print('mixed')
