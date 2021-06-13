from sys import stdin
from copy import deepcopy

def recur(arr, n):
    if len(arr) == n:
        operator_list.append(deepcopy(arr))
        return

    arr.append(' ')
    recur(arr, n)
    arr.pop()

    arr.append('+')
    recur(arr, n)
    arr.pop()

    arr.append('-')
    recur(arr, n)
    arr.pop()

test_case = int(stdin.readline())

for _ in range(test_case):
    n = int(stdin.readline())
    integer_list = [i for i in range(1, n + 1)]
    operator_list = list()

    recur(list(), n - 1)

    for operator in operator_list:
        string = ''

        for i in range(n - 1):
            string += str(integer_list[i]) + operator[i]
        string += str(integer_list[-1])

        if eval(string.replace(' ', '')) == 0:
            print(string)
    print()
