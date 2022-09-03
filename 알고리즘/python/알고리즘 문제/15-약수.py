from sys import stdin

input = stdin.readline

n = int(input())
num_list = list(map(int, input().split()))

print(max(num_list) * min(num_list))
