from sys import stdin

input = stdin.readline

n, m = map(int, input().split())
trees = list(map(int, input().split()))

start, end = 0, max(trees)
result = list()

while start <= end:
    center = (start + end) // 2
    cut = sum(tree - center for tree in trees if tree > center)

    if cut == m:
        result.append(center)
        break
    elif cut > m:
        result.append(center)
        start = center + 1
    else:
        end = center - 1

print(max(result))
