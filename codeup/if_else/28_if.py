n1, n2 = map(int, input().split())
arr = [
    n1 + n2,
    n2 + n1,
    n1 - n2,
    n2 - n1,
    n1 * n2, 
    n1 / n2,
    n2 / n1, 
    n1 ** n2,
    n2 ** n1
]

max = max(arr)

print('%.6f' % float(max))
