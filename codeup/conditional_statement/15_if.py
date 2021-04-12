y = int(input())
condition = [
    y % 4 == 0 and y % 100 != 0,
    y % 400 == 0
]

print('yes') if True in condition else print('no')
