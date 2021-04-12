f, s = map(int, input().split())
sum = f + s

if f % 2 == 0:
    print('짝수+', end='')
else:
    print('홀수+', end='')

if s % 2 == 0:
    print('짝수=', end='')
else:
    print('홀수=', end='')

if sum % 2 == 0:
    print('짝수')
else:
    print('홀수')
