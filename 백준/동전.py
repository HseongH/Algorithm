n, k = map(int, input().split())
coins = list()
count = 0

for _ in range(n):
    coin = int(input())
    if coin <= k:
        coins.append(coin)

for coin in reversed(coins):
    count += (k // coin)
    k %= coin
    if k <= 0:
        break

print(count)
