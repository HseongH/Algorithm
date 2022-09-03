from sys import stdin

input = stdin.readline

n = int(input())
result = list()

def hanoi(top, start, end, assist):
    if top > 1:
        hanoi(top - 1, start, assist, end)

    result.append((start, end))

    if top > 1:
        hanoi(top - 1, assist, end, start)

hanoi(n, 1, 3, 2)

print(len(result))

for item in result:
    print(item[0], item[1])
