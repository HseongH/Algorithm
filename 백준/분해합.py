n = int(input())
result = 0

for i in range(n):
    n_split = sum(list(map(int, str(i))))
    if i + n_split == n:
        result += i
        break

print(result)
