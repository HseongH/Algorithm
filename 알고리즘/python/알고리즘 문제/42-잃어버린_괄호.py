from sys import stdin

input = stdin.readline

operator = [list(map(int, command.split('+'))) for command in input().split('-')]

result = sum(operator[0])

for i in range(1, len(operator)):
    result -= sum(operator[i])

print(result)
