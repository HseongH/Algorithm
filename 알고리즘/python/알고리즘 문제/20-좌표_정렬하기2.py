from sys import stdin

input = stdin.readline

n = int(input())
position = sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x: (x[1], x[0]))

for item in position:
    print(item[0], item[1])
