from sys import stdin

input = stdin.readline

T = int(input())

for _ in range(T):
    n, m = map(int, input().split())

    fibonacci = [0] * (m + 1)

    if m >= 1: fibonacci[1] = 1

    for i in range(2, m + 1):
        fibonacci[i] = fibonacci[i - 1] * i

    print(fibonacci[m] // (fibonacci[n] * fibonacci[m - n])) if n and m != n else print(1)
