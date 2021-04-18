n = int(input())
result = []

if n > 0:
    while n > 0:
        result.append(str(n % 2))
        n //= 2

    result = list(reversed(result))
    result = ''.join(result)
    print(result)
else:
    print(n)
