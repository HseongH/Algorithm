from sys import stdin

input = stdin.readline

n, m = map(int, input().split())
prime_list = [True] * (m + 1)
prime_list[0], prime_list[1] = False, False

for i in range(2, int(m ** 0.5) + 1):
    if prime_list[i]:
        for j in range(2 * i, m + 1, i):
            prime_list[j] = False

for i in range(n, m + 1):
    if prime_list[i]:
        print(i)
