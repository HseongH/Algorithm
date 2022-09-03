from sys import stdin

input = stdin.readline

T = int(input())

for _ in range(T):
    string = input()
    stack = list()

    for char in string:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                print('NO')
                break
            stack.pop()
    else:
        print('NO') if stack else print('YES')
