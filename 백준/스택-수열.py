import sys

n = int(sys.stdin.readline())

stack, result = list(), list()
count = 1

for _ in range(n):
    data = int(sys.stdin.readline())

    while count <= data:
        stack.append(count)
        result.append('+')
        count += 1
    if data == stack[-1]:
        stack.pop()
        result.append('-')
    else:
        sys.stdout.write('NO')
        exit(0)

sys.stdout.write('\n'.join(result))
