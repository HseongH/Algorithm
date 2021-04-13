import math

n = int(input())
sqrt = math.ceil(math.sqrt(n)) if math.sqrt(n) % 1 != 0 else math.ceil(math.sqrt(n)) + 1
factor = []

for i in range(1, sqrt):
    if n % i == 0:
        print(i, end=' ')
        factor.insert(0, i)

for i in factor:
    if i != n // i:
        print(n // i, end=' ')
