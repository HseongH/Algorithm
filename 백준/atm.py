n = int(input())
p = list(map(int, input().split()))

p.sort()
total = p[0]

for i in range(1, n):
    p[i] += p[i - 1]
    total += p[i]

print(total)
