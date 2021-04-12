i_num = int(input())

p_num = ((((i_num % 10) * 10) + (i_num // 10)) * 2) % 100
print(p_num)
print('GOOD') if p_num <= 50 else print('OH MY GOD')
