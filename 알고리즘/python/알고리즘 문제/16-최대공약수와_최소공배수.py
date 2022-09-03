from sys import stdin

input = stdin.readline

def gcd(x, y):
    if x % y == 0:
        return y
    return gcd(y, x % y)

x, y = map(int, input().split())

if x < y: x, y = y, x

divisor = gcd(x, y)
mutiple = divisor * (x // divisor) * (y // divisor)

print(divisor)
print(mutiple)
