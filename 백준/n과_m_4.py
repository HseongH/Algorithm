from sys import stdin
input = stdin.readline

n, m = map(int, input().split())

def recur(result):
    if len(result) == m:
        print(*result)
        return

    for i in range(1, n + 1):
        if not result or i >= result[-1]:
            result.append(i)
            recur(result)
            result.pop()

recur(list())
