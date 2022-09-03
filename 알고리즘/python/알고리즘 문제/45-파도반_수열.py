from sys import stdin
input = stdin.readline

t = int(input())

triangle = [0] * 100
triangle[0], triangle[1], triangle[2], triangle[3], triangle[4] = 1, 1, 1, 2, 2

for i in range(5, 100):
    triangle[i] = triangle[i - 1] + triangle[i - 5]

for _ in range(t):
    n = int(input())
    print(triangle[n - 1])
