num_list = [i for i in range(10001)]

def d(num):
    temp = num
    constructor = 0

    while temp > 0:
        constructor += temp % 10
        temp //= 10

    num = num + constructor

    if num > 10000:
        return
    num_list[num] = 0
    d(num)

for i in range(1, 10001):
    if num_list[i] != 0:
        d(num_list[i])

for num in num_list:
    if num:
        print(num)
