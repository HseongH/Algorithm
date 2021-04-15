n = int(input())
sum = 0

for i in range(1, n + 1):
    sum += int(i * (i + 1) / 2)

print(sum)
