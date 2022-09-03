from sys import stdin

input = stdin.readline

n = int(input())
stack = list()
result = list()
count = 1

for _ in range(n):
    data = int(input())

    while count <= data:
        stack.append(count)
        result.append('+')
        count += 1

    if stack[-1] != data:
        print('NO')
        exit()

    stack.pop()
    result.append('-')

print('\n'.join(result))
