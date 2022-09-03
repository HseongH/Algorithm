from sys import stdin

input = stdin.readline

n, m = map(int, input().split())

def recur(result, start):
    if len(result) == m:
        print(' '.join(map(str, result)))
        return

    for i in range(start, n + 1):
        if i not in result:
            result.append(i)
            recur(result, i + 1)
            result.pop()

recur(list(), 1)
