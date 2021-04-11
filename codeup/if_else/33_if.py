y, m = map(int, input().split())
month = [
    [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
    [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
]
condition = [
    y % 400 == 0,
    y % 4 == 0 and y % 100 != 0
]

print(month[1][m - 1]) if True in condition else print(month[0][m - 1])
