from sys import stdin

input = stdin.readline

while True:
    string = input().rstrip()
    stack = list()

    if string == '.':
        break

    for char in string:
        if char == '(' or char == '[':
            stack.append(char)
        elif char == ')' or char == ']':
            if not stack:
                print('no')
                break
            bracket = stack.pop()

            if char == ')' and bracket == '[' or char == ']' and bracket == '(':
                print('no')
                break
    else:
        print('no') if stack else print('yes')
