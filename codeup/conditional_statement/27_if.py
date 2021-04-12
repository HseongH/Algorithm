integer = int(input())
o_num = ['st', 'nd', 'rd', 'th']

try:
    if integer // 10 == 1:
        print('%dth' % integer)
    else:
        print('%d%s' % (integer, o_num[integer % 10 -1]))
except IndexError:
    print('%dth' % integer)
