from sys import stdin

input = stdin.readline

n = int(input())

for i in range(10, n):
    split_num = list(map(int, str(i)))

    if i + sum(split_num) == n:
        print(i)
        break
else:
    print(0)
