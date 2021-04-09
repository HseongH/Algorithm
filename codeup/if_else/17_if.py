y, s = map(int, input().split())
year = y // 10000

if s == 1 or s == 2:
    year += 1900
else:
    year += 2000

print(2013 - year)
