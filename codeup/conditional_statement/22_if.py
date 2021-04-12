h, m = map(int, input().split())
h = h if m - 30 >= 0 else h - 1
m = (m + 30) % 60

if h == -1:
    h = 23

print(h, m)
