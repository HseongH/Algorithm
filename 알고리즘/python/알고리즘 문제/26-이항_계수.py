from sys import stdin

input = stdin.readline

n, k = map(int, input().split())

fibonacci = [0] * (n + 1)
if n >= 1: fibonacci[1] = 1

for i in range(2, n + 1):
    fibonacci[i] = fibonacci[i - 1] * i

print(fibonacci[n] // (fibonacci[k] * fibonacci[n - k])) if k and k != n else print(1)
