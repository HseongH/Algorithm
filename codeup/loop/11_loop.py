m = list(map(int, input().split()))

for i in range(len(m)):
    if m[i] % 2 == 1:
        m[i] = (m[i] // 2) + (m[i] % 2)
    else:
        m[i] = (m[i] // 2) * 10

print(m[0] + m[1])
