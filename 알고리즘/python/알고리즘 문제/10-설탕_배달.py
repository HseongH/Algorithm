weight = int(input())
count = 0

while weight % 5:
    weight -= 3
    count += 1

    if weight < 0:
        print(-1)
        exit()

print(count + (weight // 5))
