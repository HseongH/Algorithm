n = int(input())

def factorial(n):
    if n > 0:
        return n * factorial(n - 1)
    return 1

print(factorial(n))
