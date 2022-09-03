from sys import stdin
input = stdin.readline

n = int(input())
people = sorted(list(map(int, input().split())))
result = people[0]

for i in range(1, n):
    people[i] += people[i - 1]
    result += people[i]

print(result)
