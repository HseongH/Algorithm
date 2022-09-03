from sys import stdin

input = stdin.readline

T = int(input())

for _ in range(T):
    h, w, n = map(int, input().split())

    print(n % h * 100 + (n // h + 1)) if n % h else print(h * 100 + (n // h))
