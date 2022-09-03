from sys import stdin
from collections import Counter

input = stdin.readline

n = int(input())
num_list = sorted([int(input()) for _ in range(n)])

mean = round(sum(num_list) / n)
median = num_list[n // 2]
mode_list = sorted(Counter(num_list).most_common(), key=lambda x: (-x[1], x[0]))
mode = mode_list[0][0] if len(mode_list) == 1 or mode_list[0][1] > mode_list[1][1] else mode_list[1][0]
rag = max(num_list) - min(num_list)

print(mean)
print(median)
print(mode)
print(rag)
