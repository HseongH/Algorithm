from sys import stdin

n = int(stdin.readline())
heights = list(map(int, stdin.readline().split()))
stack = []
result = []

for i in range(n):
    while stack:
        if stack[-1][1] > heights[i]:
            result.append(stack[-1][0] + 1)
            break
        else:
            stack.pop()
    if not stack:
        result.append(0)
    stack.append([i, heights[i]])

print(' '.join(map(str, result)))
