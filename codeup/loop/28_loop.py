import math

n = int(input())
sqrt = math.ceil(math.sqrt(n)) - 1
k = n - (sqrt * sqrt)

print(k, sqrt)
