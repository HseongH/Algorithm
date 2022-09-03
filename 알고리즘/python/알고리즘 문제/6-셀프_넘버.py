num_list = [i for i in range(10001)]

def self_number(num):
    self_num = num

    while self_num < 10000:
        spl_num = list(map(int, str(self_num)))
        self_num = self_num + sum(spl_num)

        if self_num <= 10000:
            num_list[self_num] = 0

for num in num_list:
    if num:
        self_number(num)

print('\n'.join(map(str, list(filter(bool, num_list)))))
