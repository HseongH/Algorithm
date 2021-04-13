import math

n = int(input())
sqrt = math.ceil(math.sqrt(n))

def is_prime(n):
    arr = [False] * n
    sqrt = math.ceil(math.sqrt(n))

    for i in range(2, sqrt + 1):
        if arr[i]: continue

        for j in range(2 * i, n + 1, i):
            try:
                arr[j] = True
            except:
                break

    for i in range(2, len(arr)):
        if not arr[i]:
            if n % i == 0 and not arr[n // i]:
                print(i, n // i)
                break
    else:
        print('wrong number')

for i in range(2, sqrt):
    if n % i == 0:
        is_prime(n)
        break
else:
    print('wrong number')
