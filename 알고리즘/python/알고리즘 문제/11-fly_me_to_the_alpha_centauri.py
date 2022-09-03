from sys import stdin

input = stdin.readline

def number_of_operations(distance):
    square_root = distance ** 0.5

    if square_root <= round(square_root):
        return round(square_root) * 2 - 1
    return round(square_root) * 2

n = int(input())

for _ in range(n):
    x, y = map(int, input().split())
    distance = y - x
    count = number_of_operations(distance)

    print(count)
