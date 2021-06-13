import sys

def recur(y, x, n):
    global count

    if n == 2:
        if x == X and y == Y:
            print(count)
            return
        count += 1
        if x == X and y + 1 == Y:
            print(count)
            return
        count += 1
        if x + 1 == X and y == Y:
            print(count)
            return
        count += 1
        if x + 1 == X and y + 1 == Y:
            print(count)
            return
        count += 1
        return
    n //= 2
    recur(y, x, n)
    recur(y, x + n, n)
    recur(y + n, x, n)
    recur(y + n, x + n, n)

n, Y, X = map(int, sys.stdin.readline().split())
count = 0
recur(0, 0, 2 ** n)
