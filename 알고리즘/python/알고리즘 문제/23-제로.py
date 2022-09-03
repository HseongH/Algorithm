from sys import stdin

input = stdin.readline

k = int(input())
stack = list()

for _ in range(k):
    command = int(input())

    if command == 0:
        stack.pop()
        continue
    stack.append(command)

print(sum(stack))
