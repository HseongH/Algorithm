n = input()
input_list = list(map(int, input().split()))
c = 0

for i in input_list:
    if i % 2 != 0:
        continue
    c += 1

print(c)
