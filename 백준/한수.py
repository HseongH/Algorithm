n = int(input())
count = 0

for i in range(1, n + 1):
    num_list = list(map(int, str(i)))
    div_list = []

    for i in range(1, len(num_list)):
        div_list.append(num_list[i - 1]  - num_list[i])

    if not div_list:
        count += 1
        continue

    if div_list[0] * len(div_list) == sum(div_list):
        count += 1

print(count)
