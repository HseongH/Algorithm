arr = list(map(int, input().split()))

def is_triangle():
    if arr[0] + arr[1] <= arr[2]:
        print('삼각형아님')
        return

    count = 0
    shape = ['정삼각형', '이등변삼각형', '직각삼각형']

    for i in arr:
        if arr[1] == i:
            count += 1

    condition = [
        count == 3,
        count == 2,
        (arr[0] ** 2) + (arr[1] ** 2) == (arr[2] ** 2)
    ]

    try:
        idx = condition.index(True)
        print(shape[idx])
    except ValueError:
        print('삼각형')

is_triangle()
