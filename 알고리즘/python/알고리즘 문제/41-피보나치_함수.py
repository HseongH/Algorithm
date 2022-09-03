from sys import stdin

input = stdin.readline

t = int(input())

fibo = [0] * 41
fibo[1] = 1

for i in range(2, 41):
    fibo[i] = fibo[i - 1] + fibo[i - 2]

for _ in range(t):
    n = int(input())

    if n == 0:
        print(1, 0)
        continue
    if n == 1:
        print(0, 1)
        continue
    print(fibo[n - 1], fibo[n])
