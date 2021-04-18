n, c = map(int, input().split())
height = list(map(int, input().split()))

height.sort()

for i in range(len(height)):
    print(height[i], end=' ')

    if (i + 1) % c == 0:
        print()
