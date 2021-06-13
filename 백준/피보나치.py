n = int(input())
test_case = [int(input()) for _ in range(n)]

def fib(n):
    if n <= 0:
        return n

    fib_list = [0, 1]
    i = 2

    while (fib_list[i - 1] + fib_list[i - 2]) <= n:
        fib_list.append(fib_list[i - 1] + fib_list[i - 2])
        i += 1

    return fib_list[-1]

for test in test_case:
    num_list = []

    while test > 0:
        num = fib(test)
        num_list.append(num)
        test -= num

    for num in reversed(num_list):
        print(num, end=' ')
        
    print()
