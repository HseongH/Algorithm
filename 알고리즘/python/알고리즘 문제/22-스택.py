from sys import stdin

input = stdin.readline

n = int(input())
stack = list()

for _ in range(n):
    command = input().split()

    if command[0] == 'push':
        stack.append(command[1])
        continue
    elif command[0] == 'pop':
        if stack:
            print(stack.pop())
            continue
        print(-1)
        continue
    elif command[0] == 'size':
        print(len(stack))
        continue
    elif command[0] == 'empty':
        print(int(len(stack) == 0))
        continue
    elif command[0] == 'top':
        if stack:
            print(stack[-1])
            continue
        print(-1)
        continue
