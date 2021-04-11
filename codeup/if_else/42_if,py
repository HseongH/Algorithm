formula = input()
sign = ['+', '-', '*', '/']
idx = 0
s = ''

for i in range(len(sign)):
    idx = formula.find(sign[i])
    if idx != -1:
        s = sign[i]
        break

f_num, s_num = int(formula[:idx]), int(formula[idx + 1:])

if s == '+':
    print(f_num + s_num)
elif s == '-':
    print(f_num - s_num)
elif s == '*':
    print(f_num * s_num)
else:
    print('%.2f' % float(f_num / s_num))
