m = int(input())
date = int(input())
percent = list(map(int, input().split()))
money = m

for i in percent:
    money = money + (money * (i / 100))

result = round(money) - m
print(result)

if result < 0:
    print('bad')
elif result > 0:
    print('good')
else:
    print('same')
