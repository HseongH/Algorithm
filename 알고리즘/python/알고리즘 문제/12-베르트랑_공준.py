from sys import stdin

input = stdin.readline

while True:
    n = int(input())

    if n == 0:
        break
    
    maximum = 2 * n
    num_list = [True] * (2 * n + 1)

    for i in range(2, int(maximum ** 0.5) + 1):
        if num_list[i]:
            for j in range(2 * i, maximum + 1, i):
                num_list[j] = False

    print(len(list(filter(bool, num_list[n + 1:]))))
