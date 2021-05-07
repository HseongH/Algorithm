n = int(input())

stack = []
result = []
count = 1

for i in range(1, n + 1):
    data = int(input())
    while count <= data:
        stack.append(count)
        result.append('+')
        count += 1
    if stack[-1] == data:
        stack.pop()
        result.append('-')
    else:
        print('NO')
        break
else:
    print('\n'.join(result))
