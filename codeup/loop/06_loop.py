n = int(input())
input_list = list(map(int, input().split()))
sum = 0

for i in input_list:
    if i % 5 != 0:
        continue
    sum += i

print(sum)
