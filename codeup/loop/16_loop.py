n = int(input())
result = 0

while n > 0:
    n //= 10
    result += 1

print(result)
