input_int = list(map(int, input().split()))

for i in input_int:
    if i % 5 != 0:
        continue
    print(i)
    break
else:
    print(0)