from sys import stdin

input = stdin.readline

T = int(input())

def gcd(x, y):
    if x % y == 0:
        return y
    return gcd(y, x % y)

for _ in range(T):
    x, y = map(int, input().split())

    if x < y: x, y = y, x

    divisor = gcd(x, y)
    print(divisor * (x // divisor) * (y // divisor))
