from sys import stdin
input = stdin.readline

n, k = map(int, input().split())
numbers = [i for i in range(1, n + 1)]
result = list()
ptr = 0

while numbers:
    ptr = (ptr + (k - 1)) % len(numbers)

    result.append(numbers[ptr])
    del numbers[ptr]

print('<%s>' % ', '.join(map(str, result)))
