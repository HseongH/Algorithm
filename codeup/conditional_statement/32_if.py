a, b, c = map(int, input().split())
max = (a if a > b else b) if (a if a > b else b) > c else c
condition = max < (a + b + c) - max

print('yes') if condition else print('no')
