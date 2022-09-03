from sys import stdin
input = stdin.readline

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
coins = list(filter(lambda x: x <= k, coins))
count = 0

while k:
    count += k // coins[-1]
    k %= coins[-1]

    coins.pop()

print(count)
