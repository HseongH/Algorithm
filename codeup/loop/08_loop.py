a, b, c, n = map(int, input().split())
result = a

for _ in range(n - 1):
    result = result * b + c

print(result)
